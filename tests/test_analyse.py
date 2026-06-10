from unittest.mock import AsyncMock, patch



@patch("app.api.analyse.analyse_bulk_reviews")
def test_analyse_success(mock_analyse, client):
    mock_analyse.return_value = {
        "sentiment": "positive",
        "praised_features": [
            "battery",
            "display",
            "design"
        ],
        "complaints": [
            "camera",
            "speaker",
            "charging"
        ],
        "summary": "Overall positive."
    }

    response = client.post('/analyse', json={"reviews":["Iphone 15 is amazing! Battery life is great","Just that it heats very much","The camera is outstanding!"]})

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True


def test_missing_reviews(client):
    response = client.post(
        "/analyse",
        json={}
    )

    assert response.status_code == 422

def test_empty_reviews(client):
    response = client.post(
        "/analyse",
        json={
            "reviews":[]
        }
    )

    assert response.status_code == 422


def test_invalid_reviews_type(client):
    response = client.post(
        "/analyse",
        json={
            "reviews":"This should be a list, not a string"
        }
    )

    assert response.status_code == 422


def test_more_than_50_reviews(client):
    reviews = [
        "review"
        for _ in range(51)
    ]


    response = client.post(
        "/analyse",
        json={
            "reviews": reviews
        }
    )
    assert response.status_code == 422


@patch("app.api.analyse.analyze_reviews", new_callable=AsyncMock)
def test_internal_server_error(mock_analyse, client):
    mock_analyse.side_effect = Exception(
        "Groq Failed to process the request"
    )

    response = client.post(
        "/analyse",
        json={
            "reviews": [
                "Iphone 15 is amazing! Battery life is great",
                "Just that it heats very much",
                "The camera is outstanding!"
            ]
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is False
    assert body["status_code"] == 500
    assert body["message"] == "Internal Server Error: Groq Failed to process the request"
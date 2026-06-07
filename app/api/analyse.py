from app.schema.response import  ApiResponse
from ..schema.request import AnalyseRequest
from ..services.llm_service import analyze_reviews


# Define the API endpoint for analyzing bulk reviews
async def analyse_bulk_reviews(request: AnalyseRequest) -> ApiResponse:
    try:
        # Validate the input reviews
        result = await analyze_reviews(request.reviews)

        # Return the analysis result as a successful API response
        return ApiResponse(
            success=True,
            status_code=200,
            message="Reviews analyzed successfully",
            data=result
        )
    except ValueError as e:
        return ApiResponse(
            success=False,
            status_code=400,
            message=str(e)
        )
    except Exception as e:
        # Handle any exceptions that might occur during review analysis
        return ApiResponse(
            success=False,
            status_code=500,
            message="Internal Server Error: " + str(e)
        )
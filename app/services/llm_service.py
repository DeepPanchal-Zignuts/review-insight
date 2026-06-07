from ..schema.response import AnalyseResponse
from ..schema.request import AnalyseRequest
from app.config.config import settings
from groq import AsyncGroq
from app.config.prompts import ANALYSIS_PROMPT


client = AsyncGroq(api_key=settings.OPENAI_API_KEY)


"""analyze_reviews takes a list of reviews and returns an analysis of the reviews using the OpenAI API. 
It uses the ANALYSIS_PROMPT to guide the model in generating the analysis. 
The response is returned as an AnalyseResponse object."""
async def analyze_reviews(reviews: AnalyseRequest) -> AnalyseResponse:

    # Convert the list of reviews into a format suitable for the model.
    review_texts = "\n".join([f"- {review}" for review in reviews])

    # Call the OpenAI API to get the analysis of the reviews
    completions = await client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": ANALYSIS_PROMPT
            },
            {
                "role": "user",
                "content": review_texts
            }
        ],
        response_format={
            "type": "json_object"
        },
        temperature=0
    )

    # Return the analysis as an AnalyseResponse object
    return AnalyseResponse.model_validate_json(
        completions.choices[0].message.content
    )


from pydantic import BaseModel, Field


class AnalyseRequest(BaseModel):
    reviews: list[str] = Field(..., min_length=1, max_length=50, description="A list of customer reviews to be analyzed.")
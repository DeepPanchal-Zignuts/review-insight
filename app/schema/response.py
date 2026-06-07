from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from fastapi.responses import JSONResponse


# This class defines the structure of the response data for the review analysis endpoint, including sentiment, praised features, complaints, and a summary score.
class AnalyseResponse(BaseModel):
    sentiment: str
    praised_features: list[str]
    complaints: list[str]
    summary: str


# This class defines a standard structure for API responses, including fields for success status, message, data, and errors.
class ApiResponse(BaseModel):
    success: bool
    status_code: Optional[int] = None
    message: Optional[str] = None
    data: AnalyseResponse = None
    errors: Optional[List[Dict[str, Any]]] = None



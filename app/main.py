from fastapi import FastAPI
from .schema.response import ApiResponse
from app.routers.analyse_router import router as analyse_router

# Initialize the FastAPI application
app = FastAPI(  
    title="ReviewInsight API",
    description="Product Review Analysis using Groq LLM",
    version="1.0.0"
)

# Include the router for review analysis
app.include_router(analyse_router)


# Define a simple health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return ApiResponse(
        success=True,
        status_code=200,
        message="Service is up and running :)",
    )
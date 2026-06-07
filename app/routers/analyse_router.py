from fastapi import APIRouter
from app.api.analyse import analyse_bulk_reviews


# Define the router for review analysis
router = APIRouter(
    prefix="/analyse",
    tags=["Review Analysis"],
)

# Add the route for bulk review analysis
router.add_api_route(
    "", 
    analyse_bulk_reviews,
    methods=["POST"],
)
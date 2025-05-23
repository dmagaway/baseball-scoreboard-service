from fastapi import APIRouter

router = APIRouter(prefix="/scores", tags=["scores"])

@router.get("/tigers")
def get_tigers_score():
    return "5-0"
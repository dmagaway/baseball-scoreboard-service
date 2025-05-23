from fastapi import Depends, FastAPI

# from .dependencies import get_query_token, get_token_header
from .routers import scores

app = FastAPI()


app.include_router(scores.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
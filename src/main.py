from fastapi import FastAPI
from src.test.users import router as user_router

app = FastAPI() 

app.include_router(user_router)

@app.get("/") 
def home_page():
    return {"Hello": "World"}


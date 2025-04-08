from fastapi import FastAPI
from services.recommender import Recommender

app = FastAPI()
recommender = Recommender()

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Shopping AI"}

@app.get("/recommend/{product_name}")
def get_recommendations(product_name: str):
    recommendations = recommender.recommend(product_name)
    return {"product": product_name, "recommendations": recommendations}

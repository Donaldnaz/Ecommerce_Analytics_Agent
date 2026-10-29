import os
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Ecommerce Analytics Agent")


class InsightRequest(BaseModel):
    query: str
    region: str = "us-east-1"


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "agent", "region": os.getenv("AWS_REGION", "us-east-1")}


@app.post("/insight")
def generate_insight(payload: InsightRequest):
    return {
        "response": f"AI summary: {payload.query} indicates stable growth with strong conversion in premium categories.",
        "region": payload.region,
        "confidence": 0.93
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

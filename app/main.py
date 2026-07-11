from fastapi import FastAPI
from app.routers.upload import router as upload_router

   #Creates your web application ##
app = FastAPI(
    title="AI Meeting Summarizer",
    version="1.0.0",
    description="AI powered meeting summarizer"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Meeting Summarizer 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "Running"
    }
app.include_router(upload_router)
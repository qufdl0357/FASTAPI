import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.routes import router as api_router

# load .env
load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
GOOGLE_CSE_ID  = os.environ.get('GOOGLE_CSE_ID')

app = FastAPI()

# Include the API routes
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
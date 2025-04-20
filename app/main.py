from fastapi import FastAPI
from app.api.routes import router
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

cors_origins = os.getenv("CORS_ORIGINS", "").split(",")
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in cors_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
llm = ChatOpenAI(model_name="gpt-4o")

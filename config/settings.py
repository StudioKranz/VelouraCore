from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    HUGGINGFACE_TOKEN: str = os.getenv('HUGGINGFACE_TOKEN', '')
    # Add more environment variables as needed

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()

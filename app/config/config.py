import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define a settings class to hold configuration values
class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

# Create an instance of the Settings class to be used throughout the application
settings = Settings()
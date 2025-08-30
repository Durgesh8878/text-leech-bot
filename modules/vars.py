import os

API_ID    = os.environ.get("API_ID", "23056713")
API_HASH  = os.environ.get("API_HASH", "db3159297b3705b543b85937fd84e9a2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8484513783:AAEOBC8qmn9u6_zbHExT4LLYjbS4cEgkcMM") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

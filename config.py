import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# gemini-1.5-pro (used in the project PDF) has been shut down; change the model in .env if needed
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
API_URL = os.getenv("API_URL", "http://localhost:8000")
LOGO_PATH = BASE_DIR / "Image" / "Logo.png"   # optional: drop your logo here
FOOTER_TEXT = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."

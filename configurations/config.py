import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("TEST_URL")

USERNAME = os.getenv("TEST_USERNAME")
PASSWORD = os.getenv("TEST_PASSWORD")

BASE_DIR = Path(__file__).resolve().parent.parent
SCENARIO_DIR = os.path.join(BASE_DIR, "testdata")

common_data = {
    "url": URL,
    "username": USERNAME,
    "password": PASSWORD,

}

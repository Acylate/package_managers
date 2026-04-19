import os
from dotenv import load_dotenv


load_dotenv()

class Config():
    TOKEN = os.getenv("TOKEN")
    PROXY_USER = os.getenv("PROXY_USER")
    PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
    PROXY_HOST = os.getenv("PROXY_HOST")
    PROXY_PORT = os.getenv("PROXY_PORT")
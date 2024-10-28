import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '10'))
    CACHE_ENABLED = os.getenv('CACHE_ENABLED', 'false').lower() == 'true'


settings = Settings()
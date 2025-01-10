import os
from dotenv import load_dotenv


class EnvHelper:
    def __init__(self, **kwargs) -> None:
        load_dotenv()

        self.base_url = os.getenv('base_url', '')
        self.consumer_key = os.getenv('consumer_key', '')
        self.consumer_secret = os.getenv('consumer_secret', '')
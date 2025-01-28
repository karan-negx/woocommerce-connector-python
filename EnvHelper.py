import os
from dotenv import load_dotenv


class EnvHelper:
    def __init__(self, **kwargs) -> None:
        load_dotenv()

        self.base_url = os.getenv('base_url', '')
        self.consumer_key = os.getenv('consumer_key', '')
        self.consumer_secret = os.getenv('consumer_secret', '')
        self.smtp_server = os.getenv("smtp_server","")
        self.smtp_password = os.getenv("smtp_password","")
        self.smtp_port = os.getenv("smtp_port","")
        self.sender_email = os.getenv("sender_email","")
        self.company_email = os.getenv("company_email","")
        self.support_email = os.getenv("support_email","")
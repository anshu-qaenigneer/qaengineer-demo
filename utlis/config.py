import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))
    FACEBOOK_URL = os.getenv('FACEBOOK_URL', 'https://www.facebook.com/login.php/')
    FACEBOOK_EMAIL = os.getenv('FACEBOOK_EMAIL', '')
    FACEBOOK_PASSWORD = os.getenv('FACEBOOK_PASSWORD', '')

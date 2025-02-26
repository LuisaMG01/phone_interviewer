from dotenv import load_dotenv
import os

def load_config():
    load_dotenv(".env")
    config = {
        'MODEL_NAME': os.getenv('MODEL_NAME'),
        'BASE_URL': os.getenv('BASE_URL'),
        'OPENROUTER_API_KEY': os.getenv('OPENROUTER_API_KEY')
    }
    return config

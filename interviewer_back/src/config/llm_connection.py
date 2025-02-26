from langchain_openai import ChatOpenAI
from config import load_config

def get_llm_connection() -> ChatOpenAI:
    config = load_config()
    return ChatOpenAI(
        model_name=config["MODEL_NAME"],
        base_url=config["BASE_URL"],
        api_key=config["OPENROUTER_API_KEY"],
        temperature=0.7
    )

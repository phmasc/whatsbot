import os

from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME')
OPENAI_MODEL_TEMPERATURE = os.getenv('OPENAI_MODEL_TEMPERATURE')
AI_CONTEXTUALIZE_PROMPT = os.getenv('AI_CONTEXTUALIZE_PROMPT')
AI_SYSTEM_PROMPT = os.getenv('AI_SYSTEM_PROMPT')
VECTOR_STORE_PATH = os.getenv('VECTOR_STORE_PATH')
RAG_FILES_DIR = os.getenv('RAG_FILES_DIR')
EVOLUTION_API_URL = os.getenv('EVOLUTION_API_URL')
EVOLUTION_INSTANCE_NAME = os.getenv('EVOLUTION_INSTANCE_NAME')
EVOLUTION_AUTHENTICATION_API_KEY = os.getenv('AUTHENTICATION_API_KEY')
REDIS_URL = os.getenv('CACHE_REDIS_URI')

AUTORIZED_CHATS = set(
    chat.strip() for chat in os.getenv("AUTORIZED_CHATS", "").split(";")
)

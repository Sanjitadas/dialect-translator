import os
from dotenv import load_dotenv
import cohere

load_dotenv()  # Load variables from .env

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def translate_text(input_text, src_lang_code="auto", tgt_lang_code="en-US"):
    try:
        prompt = f"Translate this from {src_lang_code} to {tgt_lang_code} with fluent and native context:\n\n{input_text}"
        response = co.chat(model="command-r-plus", message=prompt)
        return response.text.strip()
    except Exception as e:
        return f"Translation Error: {str(e)}"




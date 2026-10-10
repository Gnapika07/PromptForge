import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.1-flash-lite"


def generate_response(prompt: str) -> str:
    """Generate a response with retries for temporary API failures."""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
            )

            if response.text:
                return response.text

            raise RuntimeError("Gemini returned an empty response.")

        except Exception as error:
            error_text = str(error)

            temporary_error = any(
                code in error_text
                for code in ["503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED"]
            )

            if not temporary_error or attempt == 2:
                raise

            wait_seconds = 2 ** (attempt + 1)
            print(
                f"Temporary Gemini issue. Retrying in "
                f"{wait_seconds} seconds..."
            )
            time.sleep(wait_seconds)

    raise RuntimeError("Gemini request failed after retries.")
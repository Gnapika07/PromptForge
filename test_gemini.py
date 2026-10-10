from llm_client import generate_response

try:
    answer = generate_response(
        "Explain prompt engineering in two simple sentences."
    )
    print("Gemini connection successful!")
    print(answer)

except Exception as error:
    print("Gemini connection failed.")
    print(type(error).__name__, error)
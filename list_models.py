from llm_client import client

print("Checking models available to your API key...\n")

try:
    for model in client.models.list():
        actions = model.supported_actions or []

        if "generateContent" in actions:
            print(model.name)

except Exception as error:
    print("Could not list models.")
    print(type(error).__name__, error)
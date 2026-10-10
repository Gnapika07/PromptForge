from prompt_optimizer import optimize_prompt, explain_techniques

original = "Explain machine learning"

try:
    improved = optimize_prompt(original, "Role Prompting")

    print("\n--- ORIGINAL PROMPT ---")
    print(original)

    print("\n--- OPTIMIZED PROMPT ---")
    print(improved)

    print("\n--- TECHNIQUES USED ---")
    print(explain_techniques(improved))

except Exception as error:
    print("Error:", type(error).__name__, error)
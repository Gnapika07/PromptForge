from prompt_evaluator import evaluate_prompt

examples = [
    "Explain machine learning",
    (
        "Act as an expert educator. Explain machine learning "
        "to a beginner student. Keep it under 200 words. "
        "Use headings and bullet points."
    ),
]

for prompt in examples:
    result = evaluate_prompt(prompt)

    print("\nPrompt:", prompt)
    print("Scores:", result["scores"])
    print("Total:", result["total"], "/ 100")
    print("Feedback:", result["feedback"])
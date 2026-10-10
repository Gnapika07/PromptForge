from llm_client import generate_response


def optimize_prompt(original_prompt: str, technique: str) -> str:
    """Improve a user's prompt using a selected technique."""

    instruction = f"""
You are an expert prompt engineer.

Your task is to improve the user's original prompt.

Selected technique: {technique}

Follow these rules:
1. Preserve the user's original intention.
2. Make the task specific and clear.
3. Add a suitable role or context when useful.
4. Include relevant constraints.
5. Specify an appropriate output format.
6. Do not answer the original prompt.
7. Return only the improved prompt.

Original prompt:
{original_prompt}
"""

    return generate_response(instruction)


def explain_techniques(optimized_prompt: str) -> str:
    """Explain the prompt engineering techniques used."""

    instruction = f"""
Analyze the following optimized prompt.

Identify the prompt engineering techniques it uses,
such as role prompting, contextual prompting,
instruction prompting, constraint-based prompting,
and output-format specification.

For each technique:
- Name it.
- Explain how it appears in the prompt.

Optimized prompt:
{optimized_prompt}

Return the explanation in clear bullet points.
"""

    return generate_response(instruction)
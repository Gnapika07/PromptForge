# PromptForge — Intelligent Prompt Engineering Assistant

PromptForge is a Python web application that helps users refine prompts for generative AI systems. It uses the Google Gemini API to generate an optimized prompt and a rule-based evaluator to inspect five structural criteria.

## Features
- AI-assisted prompt optimization using Gemini.
- Six selectable optimization techniques.
- Five-criterion structural evaluation: role clarity, context, task specificity, constraints, and output format.
- Criterion-level feedback and technique explanations.
- Prompt download and a light-themed Streamlit dashboard.

## Technology Stack
Python, Streamlit, Google Gen AI Python SDK, Gemini API, `python-dotenv`, and regular expressions.

## Project Structure
```text
PromptForge/
├── app.py
├── llm_client.py
├── prompt_optimizer.py
├── prompt_evaluator.py
├── test_optimizer.py
├── test_evaluator.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── report/
    └── PromptForge_Report.pdf
```

## Setup

### 1. Clone the repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd PromptForge
```

### 2. Create and activate a virtual environment

Windows PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key
Copy `.env.example` to `.env` and replace the placeholder with your own key:
```text
GEMINI_API_KEY=your_gemini_api_key_here
```
Never commit `.env` or publish your API key. `.gitignore` excludes it.

### 5. Run the app
```bash
streamlit run app.py
```

## Tests
Run evaluator tests:
```bash
python test_evaluator.py
```

Run the optimizer test after configuring a valid Gemini API key:
```bash
python test_optimizer.py
```
The optimizer test calls an external API, so it may depend on connectivity, quota, and model availability.

## Evaluation Method
Each criterion contributes up to 20 points, for a total of 100. The current evaluator uses keyword and pattern matching. A score of 100/100 means that the rules detected patterns for all five criteria; it does not prove semantic prompt quality or guarantee accurate, safe, or useful generated answers.

## Preliminary Testing
The following are the latest manually reported scores after updates to evaluator keyword rules:

| Sample prompt | Original | Optimized |
|---|---:|---:|
| Explain machine learning | 10/100 | 100/100 |
| Write Python code to sort a list | 10/100 | 100/100 |
| Help me prepare for a job interview | 0/100 | 100/100 |
| Analyze sales data | 0/100 | 100/100 |
| Detailed machine-learning prompt | 100/100 | 100/100 |

These are preliminary results, not an independent benchmark. Some scores were lower before the evaluator changed. The results show that the prompts matched the current structural rules, not that downstream answers were independently shown to improve.

## Limitations
- Keyword matching can produce false positives and false negatives.
- Effective prompts may not contain the exact patterns expected by the evaluator.
- Model outputs can vary between requests.
- Preserving intent and avoiding unsupported assumptions are goals, not formal guarantees.
- No large benchmark or independent human evaluation of downstream answers has been conducted.
- The application depends on the Gemini API.

## Future Improvements
- Build a larger fixed test set.
- Add positive, negative, and paraphrase tests for each criterion.
- Compare evaluator versions on the same prompts.
- Collect human ratings for intent preservation and usefulness.
- Evaluate downstream answers with task-specific metrics.
- Add prompt history and side-by-side comparison.

## Security
Never commit `.env`, API keys, tokens, or the virtual environment. If a secret is accidentally published, revoke or rotate it immediately.

## License
No license has been selected yet. Until one is added, do not assume others have permission to reuse or redistribute this project.

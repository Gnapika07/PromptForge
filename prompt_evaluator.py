
import re


def evaluate_prompt(prompt: str) -> dict:
    """
    Evaluate five structural prompt-quality criteria.

    Each criterion receives 20 points when its heuristic
    checks detect relevant wording. This is a rule-based
    estimate, not a semantic quality assessment.
    """
    text = prompt.strip().lower()
    words = re.findall(r"\b[\w'-]+\b", text)

    scores = {
        "Role clarity": 0,
        "Context": 0,
        "Task specificity": 0,
        "Constraints": 0,
        "Output format": 0,
    }

    feedback = []

    if not text:
        return {
            "scores": scores,
            "total": 0,
            "feedback": [
                "Enter a prompt to evaluate its structure."
            ],
        }

    # 1. Role clarity
    role_patterns = [
        r"\bact as\b",
        r"\byou are\b",
        r"\brole\s*:",
        r"\bexpert\b",
        r"\bdeveloper\b",
        r"\beducator\b",
        r"\bresearcher\b",
        r"\bengineer\b",
        r"\banalyst\b",
        r"\bteacher\b",
    ]

    if any(re.search(pattern, text) for pattern in role_patterns):
        scores["Role clarity"] = 20
    else:
        feedback.append("Add a relevant role when useful.")

    
    # 2. Context
    context_patterns = [
        r"\bcontext\b",
        r"\bbackground\b",
        r"\bbeginner\b",
        r"\bnovice\b",
        r"\bno prior\b",
        r"\btarget audience\b",
        r"\baudience\b",
        r"\bstudent\b",
        r"\breader\b",
        r"\buser\b",
        r"\btechnical background\b",
        r"\bexperience level\b",
        r"\bfor someone\b",
        r"\bfor a\b",
        r"\bintended for\b",
        r"\binput\b",
        r"\bprovided\b",
        r"\bgiven\b",
        r"\binteger\b",
        r"\blist of\b",
        r"\bdata\b",
        r"\buse case\b",
        r"\bscenario\b",
        r"\bpurpose\b",
    ]

    if any(re.search(pattern, text) for pattern in context_patterns):
        scores["Context"] = 20
    else:
        feedback.append(
            "Specify the audience or relevant background when useful."
        )


    # 3. Task specificity
    action_patterns = [
        r"\bexplain\b",
        r"\bdescribe\b",
        r"\bwrite\b",
        r"\bcreate\b",
        r"\bdevelop\b",
        r"\banalyze\b",
        r"\banalyse\b",
        r"\bcompare\b",
        r"\bsummarize\b",
        r"\bsummarise\b",
        r"\bdefine\b",
        r"\bimplement\b",
        r"\bsort\b",
        r"\bdesign\b",
        r"\bidentify\b",
        r"\bclassify\b",
        r"\bprovide\b",
        r"\bgenerate\b",
        r"\bprepare\b",
        r"\bdiscuss\b",
        r"\bevaluate\b",
        r"\bbuild\b",
    ]

    has_action = any(
        re.search(pattern, text) for pattern in action_patterns
    )

    if has_action and len(words) >= 12:
        scores["Task specificity"] = 20
    elif has_action:
        scores["Task specificity"] = 10
        feedback.append(
            "Add useful task details where they improve clarity."
        )
    else:
        feedback.append("State a clear action for the model.")

    # 4. Constraints
    constraint_patterns = [
        r"\bconstraint[s]?\b",
        r"\bunder\s+\d+\b",
        r"\bbelow\s+\d+\b",
        r"\bmaximum\b",
        r"\bminimum\b",
        r"\bat least\b",
        r"\bno more than\b",
        r"\bmust\b",
        r"\bmust not\b",
        r"\bdo not\b",
        r"\bdon't\b",
        r"\bavoid\b",
        r"\bwithin\b",
        r"\bexactly\b",
        r"\bword limit\b",
        r"\btime limit\b",
        r"\bwithout\b",
        r"\bnot use\b",
        r"\bcomplexity\b",
        r"\bpep 8\b",
        r"\bbetween\s+\d+\s+and\s+\d+\b",
    ]

    if any(
        re.search(pattern, text) for pattern in constraint_patterns
    ):
        scores["Constraints"] = 20
    else:
        feedback.append(
            "Add relevant constraints when the task needs them."
        )

    # 5. Output format
    format_patterns = [
        r"\boutput format\b",
        r"\bformat\b",
        r"\bbullet points?\b",
        r"\bnumbered list\b",
        r"\bheadings?\b",
        r"\btable\b",
        r"\bjson\b",
        r"\bmarkdown\b",
        r"\bparagraph\b",
        r"\bstep-by-step\b",
        r"\bcode block\b",
        r"\bcode snippet\b",
        r"\bpython code\b",
        r"\bstructured format\b",
        r"\bsingle\b.*\bcode block\b",
        r"\breturn\b.*\bformat\b",
    ]

    if any(re.search(pattern, text) for pattern in format_patterns):
        scores["Output format"] = 20
    else:
        feedback.append("Specify a suitable output format.")

    total = sum(scores.values())

    if not feedback:
        feedback.append(
            "All five structural criteria were detected."
        )

    return {
        "scores": scores,
        "total": total,
        "feedback": feedback,
    }

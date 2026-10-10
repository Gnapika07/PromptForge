
import streamlit as st

from prompt_optimizer import optimize_prompt, explain_techniques
from prompt_evaluator import evaluate_prompt


# ==============================================
# PAGE CONFIGURATION
# ==============================================

st.set_page_config(
    page_title="PromptForge",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==============================================
# LIGHT THEME STYLING
# ==============================================

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #FAF9FF;
        color: #25213B;
    }

    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #EAE5FA;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .brand {
        color: #7258D8;
        font-size: 1.7rem;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .hero {
        background: linear-gradient(
            120deg, #F0EBFF, #FFFFFF
        );
        border: 1px solid #E4DCF9;
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: #292044;
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -1.2px;
        margin-bottom: 10px;
    }

    .hero p {
        color: #6E6684;
        font-size: 1rem;
        margin-bottom: 0;
    }

    .section-heading {
        color: #30264D;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    div.stButton > button {
        background-color: #7258D8;
        color: white;
        border: 1px solid #7258D8;
        border-radius: 10px;
        font-weight: 600;
        min-height: 44px;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #5D43C4;
        border-color: #5D43C4;
        color: white;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #EAE5FA;
        border-radius: 14px;
        padding: 16px;
    }

    div[data-testid="stMetricLabel"] {
        color: #77708B;
    }

    div[data-testid="stMetricValue"] {
        color: #7258D8;
    }

    div[data-testid="stTabs"] button {
        font-weight: 600;
    }

    .info-card {
        background: white;
        border: 1px solid #EAE5FA;
        border-radius: 14px;
        padding: 18px;
        min-height: 125px;
    }

    .info-card h4 {
        color: #7258D8;
        margin-top: 0;
    }

    .info-card p {
        color: #6E6684;
        font-size: 0.92rem;
    }

    .footer {
        text-align: center;
        color: #8B849D;
        font-size: 0.8rem;
        padding-top: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==============================================
# SESSION STATE
# ==============================================

if "promptforge_result" not in st.session_state:
    st.session_state["promptforge_result"] = None

if "explanation" not in st.session_state:
    st.session_state["explanation"] = None


# ==============================================
# SIDEBAR
# ==============================================

with st.sidebar:

    st.markdown(
        '<div class="brand">⚡ PromptForge</div>',
        unsafe_allow_html=True,
    )

    st.caption("Intelligent Prompt Engineering Assistant")

    st.divider()

    st.markdown("### Optimization technique")

    technique = st.selectbox(
        "Choose a technique",
        [
            "Comprehensive Prompt Optimization",
            "Role Prompting",
            "Contextual Prompting",
            "Constraint-Based Prompting",
            "Output-Format Specification",
            "Few-Shot Prompting",
        ],
        help="Choose how PromptForge should improve your prompt.",
    )

    st.divider()

    st.markdown("### Quality criteria")

    criteria = [
        "Role clarity",
        "Context",
        "Task specificity",
        "Constraints",
        "Output format",
    ]

    for item in criteria:
        st.markdown(f"✓ {item}")

    st.divider()

    st.markdown("### About")

    st.caption(
        "PromptForge improves prompts using Gemini "
        "and evaluates five structural quality criteria."
    )


# ==============================================
# HEADER
# ==============================================

st.markdown(
    """
    <div class="hero">
        <h1>Make every prompt work harder.</h1>
        <p>
            Transform unclear instructions into structured prompts.
            Analyze their quality and explore the techniques used.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ==============================================
# INPUT SECTION
# ==============================================

st.markdown(
    '<div class="section-heading">Your original prompt</div>',
    unsafe_allow_html=True,
)

with st.form("promptforge_form"):

    original_prompt = st.text_area(
        "Enter your prompt",
        placeholder=(
            "Example: Explain machine learning "
            "in simple terms..."
        ),
        height=150,
        label_visibility="collapsed",
    )

    submitted = st.form_submit_button(
        "⚡ Optimize my prompt",
        use_container_width=True,
    )


# ==============================================
# OPTIMIZATION
# ==============================================

if submitted:

    if not original_prompt.strip():

        st.warning("Please enter a prompt before optimizing.")

    else:

        with st.spinner(
            "Improving your prompt and analyzing its quality..."
        ):

            try:

                improved_prompt = optimize_prompt(
                    original_prompt,
                    technique,
                )

                original_result = evaluate_prompt(
                    original_prompt
                )

                improved_result = evaluate_prompt(
                    improved_prompt
                )

                st.session_state["promptforge_result"] = {
                    "original_prompt": original_prompt,
                    "improved_prompt": improved_prompt,
                    "technique": technique,
                    "original_result": original_result,
                    "improved_result": improved_result,
                }

                st.session_state["explanation"] = None

            except Exception as error:

                st.error(
                    "Prompt optimization failed. "
                    "Check your Gemini API connection and try again."
                )

                with st.expander("Technical error details"):
                    st.code(str(error))


# ==============================================
# RESULTS
# ==============================================

result = st.session_state["promptforge_result"]


if result is not None:

    original_result = result["original_result"]
    improved_result = result["improved_result"]
    improved_prompt = result["improved_prompt"]
    original_text = result["original_prompt"]

    original_score = original_result["total"]
    improved_score = improved_result["total"]
    score_difference = improved_score - original_score

    st.divider()

    st.markdown("## Your results")

    st.caption(
        f"Selected technique: {result['technique']}"
    )

    # ------------------------------------------
    # METRICS
    # ------------------------------------------

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Original score",
            f"{original_score}/100",
        )

    with metric2:
        st.metric(
            "Optimized score",
            f"{improved_score}/100",
            delta=f"{score_difference:+} points",
        )

    with metric3:

        fully_met = sum(
            1
            for score in improved_result["scores"].values()
            if score == 20
        )

        st.metric(
            "Criteria fully met",
            f"{fully_met}/5",
        )

    st.caption(
        "Scores measure five structural indicators using "
        "a rule-based evaluator. They do not establish "
        "factual accuracy or guarantee better AI answers."
    )

    # ------------------------------------------
    # TABS
    # ------------------------------------------

    prompt_tab, quality_tab, techniques_tab = st.tabs(
        [
            "✨ Optimized prompt",
            "📊 Quality analysis",
            "🧠 Techniques used",
        ]
    )

    # ==========================================
    # TAB 1: OPTIMIZED PROMPT
    # ==========================================

    with prompt_tab:

        st.markdown("### Your improved prompt")

        st.caption(
            "Use the copy icon in the top-right corner "
            "of the prompt box to copy the entire prompt."
        )

        # Streamlit's built-in code block includes
        # a native copy-to-clipboard control.
        st.code(
            improved_prompt,
            language=None,
        )

        st.download_button(
            label="⬇️ Download optimized prompt",
            data=improved_prompt,
            file_name="promptforge_optimized_prompt.txt",
            mime="text/plain",
            use_container_width=True,
        )

        with st.expander("Compare with the original prompt"):

            st.markdown("**Original prompt**")

            st.text_area(
                "Original prompt text",
                value=original_text,
                height=130,
                disabled=True,
                key="original_comparison",
            )

            st.markdown("**Optimized prompt**")

            st.text_area(
                "Optimized prompt text",
                value=improved_prompt,
                height=180,
                disabled=True,
                key="optimized_comparison",
            )

    # ==========================================
    # TAB 2: QUALITY ANALYSIS
    # ==========================================

    with quality_tab:

        st.markdown("### Structural quality breakdown")

        st.caption(
            "Each criterion contributes up to 20 points."
        )

        for criterion, score in improved_result[
            "scores"
        ].items():

            st.markdown(
                f"**{criterion}** · {score}/20"
            )

            st.progress(
                max(0.0, min(1.0, score / 20))
            )

        st.divider()

        st.markdown("### Suggestions for your original prompt")

        if original_result["feedback"]:

            for suggestion in original_result["feedback"]:
                st.markdown(f"- {suggestion}")

        else:

            st.success(
                "The original prompt meets all five "
                "structural criteria detected by the evaluator."
            )

        st.divider()

        st.markdown("### Interpretation")

        if improved_score > original_score:

            st.success(
                f"The structural score increased by "
                f"{score_difference} points."
            )

        elif improved_score == original_score:

            st.info(
                "The structural score stayed the same. "
                "Review the prompt and individual criteria "
                "to determine whether further changes are useful."
            )

        else:

            st.warning(
                "The structural score decreased. "
                "Review the individual criteria and the "
                "optimized prompt before deciding whether "
                "the changes are useful."
            )

    # ==========================================
    # TAB 3: TECHNIQUES USED
    # ==========================================

    with techniques_tab:

        st.markdown("### Understand your optimized prompt")

        st.write(
            "Ask Gemini to explain which prompt engineering "
            "techniques appear in the improved prompt."
        )

        if st.button(
            "🧠 Explain techniques",
            use_container_width=True,
            key="explain_techniques",
        ):

            with st.spinner("Analyzing prompt techniques..."):

                try:

                    explanation = explain_techniques(
                        improved_prompt
                    )

                    st.session_state["explanation"] = (
                        explanation
                    )

                except Exception as error:

                    st.error(
                        "Could not generate the explanation. "
                        "Please try again."
                    )

                    with st.expander("Technical error details"):
                        st.code(str(error))

        if st.session_state["explanation"]:

            st.markdown("#### Explanation")

            st.markdown(
                st.session_state["explanation"]
            )

else:

    # ==========================================
    # EMPTY WORKSPACE
    # ==========================================

    st.divider()

    st.markdown("## How PromptForge helps")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="info-card">
                <h4>✨ Optimize</h4>
                <p>
                    Improve clarity and structure while
                    preserving the original task.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="info-card">
                <h4>📊 Evaluate</h4>
                <p>
                    Review five structural criteria and
                    identify opportunities for improvement.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            """
            <div class="info-card">
                <h4>🧠 Understand</h4>
                <p>
                    Explore the prompt engineering techniques
                    used in the optimized prompt.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==============================================
# FOOTER
# ==============================================

st.markdown(
    """
    <div class="footer">
        PromptForge · Intelligent Prompt Engineering Assistant
    </div>
    """,
    unsafe_allow_html=True,
)

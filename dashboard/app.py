import streamlit as st
import sys
import os
import pandas as pd

# 🔥 Fix path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from classifier import PromptClassifier
from evaluator import run_evaluation

# 🔥 Load model once
@st.cache_resource
def load_model():
    return PromptClassifier()

clf = load_model()

st.set_page_config(page_title="SmartGuard AI Firewall")

st.title("🛡️ SmartGuard - LLM Firewall")

# -----------------------------
# 🔧 THRESHOLD
# -----------------------------
threshold = st.slider(
    "🔧 Detection Strictness (Threshold)",
    min_value=0.1,
    max_value=0.9,
    value=0.6,
    step=0.05
)

# -----------------------------
# 📊 SESSION HISTORY (LIVE GRAPH)
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# 🔍 INPUT TESTING
# -----------------------------
user_input = st.text_area("Enter your prompt:")

if st.button("Analyze", key="analyze_btn"):
    result = clf.classify(user_input)

    label = result["label"]
    confidence = result["confidence"]

    # ✅ APPLY THRESHOLD LOGIC
    if label == "unsafe" and confidence >= threshold:
        final_label = "unsafe"
        st.error(f"🚨 UNSAFE (Confidence: {confidence})")
    else:
        final_label = "safe"
        st.success(f"✅ SAFE (Confidence: {confidence})")

    st.info(f"🧠 Reason: {result.get('reason', '-')}")
    st.progress(confidence)

    # 🔥 STORE RESULT FOR LIVE GRAPH
    st.session_state.history.append(final_label)

# -----------------------------
# 📊 LIVE GRAPH (REAL-TIME)
# -----------------------------
if st.session_state.history:
    st.markdown("### 📊 Live Detection Stats")

    safe_count_live = st.session_state.history.count("safe")
    unsafe_count_live = st.session_state.history.count("unsafe")

    live_chart = pd.DataFrame({
        "Safe": [safe_count_live],
        "Unsafe": [unsafe_count_live]
    })

    st.bar_chart(live_chart)

    if st.button("Reset Stats", key="reset_btn"):
        st.session_state.history = []

# -----------------------------
# 📊 EVALUATION (STATIC DATASET)
# -----------------------------
st.markdown("---")
st.subheader("📊 Model Evaluation")

if st.button("Run Evaluation", key="eval_btn"):

    accuracy, safe_count, unsafe_count, results, confusion = run_evaluation()

    st.success(f"Accuracy: {accuracy*100:.2f}%")

    # ✅ BAR CHART
    chart_data = pd.DataFrame({
        "Safe": [safe_count],
        "Unsafe": [unsafe_count]
    })

    st.bar_chart(chart_data)

    # ✅ CONFUSION MATRIX
    st.write("### 🔍 Confusion Matrix")

    cm_df = pd.DataFrame([
        [confusion["TN"], confusion["FP"]],
        [confusion["FN"], confusion["TP"]]
    ],
    columns=["Pred Safe", "Pred Unsafe"],
    index=["Actual Safe", "Actual Unsafe"])

    st.table(cm_df)

    # ✅ RESULTS TABLE
    st.write("### 📄 Detailed Results")
    st.dataframe(pd.DataFrame(results))
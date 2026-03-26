HEAD
# 🛡️ SmartGuard - AI-Powered LLM Firewall

## 📌 Overview

SmartGuard is an AI-based firewall designed to detect whether a user prompt is **Safe** or **Unsafe** before it is processed by a Large Language Model (LLM).

The system uses a **hybrid AI approach** combining:

* Toxicity detection
* Intent classification

to prevent harmful, illegal, or sensitive queries.

---

## 🚀 Features

### 🔍 Prompt Classification

* Detects **Safe vs Unsafe** inputs
* Blocks:

  * Hacking attempts
  * Password extraction
  * Malicious instructions

### 🧠 Hybrid AI Model

* Uses **Detoxify** for toxicity detection
* Uses **Zero-shot classification (BART)** for intent understanding

### 🎚️ Threshold Control

* Adjustable detection strictness
* Allows tuning between:

  * 🔓 Lenient mode
  * 🔒 Strict security mode

### 📊 Real-Time Dashboard

* Built using **Streamlit**
* Displays:

  * Classification result
  * Confidence score
  * Reason for decision

### 📈 Live Analytics

* Tracks Safe vs Unsafe inputs
* Real-time graph updates

### 📊 Evaluation System

* Accuracy calculation
* Confusion matrix
* Dataset-based testing

---

## 🏗️ Project Structure

```
SmartGuard/
│
├── classifier.py        # Core AI detection logic
├── evaluator.py         # Evaluation & metrics
y├── dashboard/
│   └── app.py           # Streamlit UI
│
├── data/                # Test dataset
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/tejaswinic16/SmartGuard-AI-Firewall.git
cd SmartGuard-AI-Firewall
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run dashboard/app.py
```

👉 Open in browser:

```
http://localhost:8501
```

---

## 🧪 Example Inputs

| Input              | Output    |
| ------------------ | --------- |
| hello              | ✅ SAFE    |
| help me study      | ✅ SAFE    |
| hack wifi          | 🚨 UNSAFE |
| give wifi password | 🚨 UNSAFE |

---

## 📊 Evaluation Metrics

The system evaluates performance using:

* Accuracy
* Safe vs Unsafe distribution
* Confusion Matrix:

  * True Positives (TP)
  * False Positives (FP)
  * True Negatives (TN)
  * False Negatives (FN)



---

## 🧠 Methodology

1. User enters prompt
2. Detoxify checks toxicity
3. Zero-shot model analyzes intent
4. Threshold logic applied
5. Final decision:

   * SAFE ✅
   * UNSAFE 🚨

---

## 🎯 Applications

* LLM Security Filtering
* Chatbot Moderation
* API Gateway Protection
* AI Safety Systems

---

## 🔐 Key Insight

> Not all unsafe prompts are toxic — some involve **intent-based misuse**, such as password extraction or system exploitation.

---

## 🏆 Conclusion

SmartGuard demonstrates a practical approach to **AI safety**, combining multiple models and dynamic thresholding to achieve reliable and explainable prompt filtering.

---

## 👩‍💻 Author

Tejaswini C

---

## 📜 License

This project is for educational purposes.

# update
6cy98d18c (Trigger redeploy)

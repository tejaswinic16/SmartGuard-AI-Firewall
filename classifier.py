from detoxify import Detoxify
from transformers import pipeline
import time

import torch
class PromptClassifier:
    def __init__(self):
        print("🔄 Loading models...")

        start_time = time.time()

        self.detox = Detoxify('original', )

        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=-1
        )

        end_time = time.time()
        print(f"✅ Models loaded in {end_time - start_time:.2f} seconds")

        # ✅ KEEP LABELS SIMPLE (IMPORTANT)
        self.labels = [
            "safe request",
            "hacking or illegal access",
            "password or sensitive information request",
            "dangerous instruction"
        ]

    def classify(self, text):
        try:
            # -----------------------------
            # 🔥 STEP 1: DETOXIFY
            # -----------------------------
            detox_result = self.detox.predict(text)
            toxicity_score = max(detox_result.values())

            if toxicity_score > 0.7:
                return {
                    "label": "unsafe",
                    "confidence": round(toxicity_score, 4),
                    "reason": "Toxic content detected"
                }

            # -----------------------------
            # 🔥 STEP 2: CLASSIFIER
            # -----------------------------
            result = self.classifier(
                text,
                self.labels,
                multi_label=True
            )

            scores = dict(zip(result["labels"], result["scores"]))

            # ✅ SAFE SCORE
            safe_score = scores.get("safe request", 0)

            # ✅ UNSAFE SCORE (SAFE ACCESS)
            unsafe_score = max(
                scores.get("hacking or illegal access", 0),
                scores.get("password or sensitive information request", 0),
                scores.get("dangerous instruction", 0)
            )

            # -----------------------------
            # 🔥 STEP 3: DECISION
            # -----------------------------
            if unsafe_score > 0.6:
                return {
                    "label": "unsafe",
                    "confidence": round(unsafe_score, 4),
                    "reason": "Detected unsafe intent"
                }

            if safe_score > 0.4:
                return {
                    "label": "safe",
                    "confidence": round(safe_score, 4),
                    "reason": "Safe request"
                }

            return {
                "label": "safe",
                "confidence": round(max(safe_score, unsafe_score), 4),
                "reason": "Uncertain → allowed"
            }

        except Exception as e:
            print("ERROR:", e)  # 🔥 DEBUG
            return {
                "label": "error",
                "confidence": 0.0,
                "error": str(e)
            }


# -----------------------------
# TEST
# -----------------------------
if __name__ == "__main__":
    clf = PromptClassifier()

    while True:
        text = input("\nEnter prompt (or 'exit'): ")

        if text.lower() == "exit":
            break

        result = clf.classify(text)

        print("\n🧾 Result:")
        print(f"Label      : {result['label']}")
        print(f"Confidence : {result['confidence']}")
        print(f"Reason     : {result.get('reason', '-')}")
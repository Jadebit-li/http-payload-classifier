# AI-WAF: Malicious Payload Detector

An application-layer (L7) intelligent Web Application Firewall (WAF) engine designed to detect malicious HTTP requests using statistical natural language processing and supervised machine learning. 

This system vectorizes payloads into a high-dimensional character feature space to identify structural and syntactic anomalies characteristic of code injection vulnerabilities.

---

## Technical Architecture & Core Stack

* **Layer Focus:** Layer 7 (Application Layer Protocol Security)
* **Pipeline Framework:** Scikit-Learn (Object-oriented ML pipelines)
* **Vectorization Engine:** Character-level Term Frequency-Inverse Document Frequency (TF-IDF)
* **Classification Model:** Logistic Regression (Max iterations: 1000)
* **Interface Layer:** Streamlit (Local web micro-service engine)
* **Data Layout:** Pandas and NumPy for vector mapping and tokenization

---

## Feature Engineering & Data Pipeline

Standard word-level tokenizers fail on web exploitation payloads because automated scripts and code injections rely on heavy punctuation configurations rather than standard natural language vocabularies. 

### Vectorization Matrix Strategy
* **Tokenization Type:** `analyzer='char'`
* **N-gram Range:** `(1, 4)` (Extracts overlapping character sequences from 1 to 4 characters long)
* **Max Feature Bounding:** `10,000` features

This architecture forces the model to track structural syntax patterns like `' OR 1==--`, `<script>`, and `../` as explicit numerical weights.

### Leakage Defense Protocol
The data pipeline implements a strict execution sequence to ensure zero data leakage:
1. Raw strings are scrubbed and audited for duplicate structures.
2. Data arrays are split into Training (80%) and Testing (20%) sets using stratified sampling to maintain identical attack-to-benign ratios.
3. The `TfidfVectorizer` is trained (`.fit_transform()`) **only** on the training data slice. The testing slice is strictly processed via `.transform()`.

---

## Dataset Profile

The model was trained and validated using a clean, audited version of the open-source **HttpParamsDataset** (Morzeux). 

* **Total Clean Rows:** 31,067 (Verified 0 duplicate payloads, 0 missing entries)
* **Benign Class (norm):** 19,304 records (62.13%)
* **Malicious Class (anom):** 11,763 records (37.86%)

### Target Vulnerability Breakdown
* **SQL Injection (SQLi):** 10,852 records
* **Cross-Site Scripting (XSS):** 532 records
* **Path Traversal:** 290 records
* **Command Injection (CmdI):** 89 records

---

## Performance Evaluation & Verification

The pipeline achieved the following mathematical metrics on the unseen validation test split (6,214 records):

| Metric | System Value |
| :--- | :--- |
| **Accuracy** | 99.89% |
| **Precision** | 100.00% |
| **Recall** | 99.70% |
| **F1 Score** | 99.85% |

### Confusion Matrix Output
```text
[[3861    0]   --> [True Negatives,  False Positives]
 [   7 2346]]  --> [False Negatives, True Positives]

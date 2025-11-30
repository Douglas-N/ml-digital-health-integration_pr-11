# 🌍 ML-Driven Digital Health Tools for Off-Site Oncology Care Integration  
### *Using Machine Learning to Improve Scalable, Accessible, and Efficient Oncology Care in LMIC Settings*

This repository contains a **machine-learning prototype** designed to demonstrate how digital health data from **off-site care centers in Senegal** (collected through the *med.ai* platform) can be used to improve oncology care coordination, early detection of deterioration, and resource allocation.

The prototype is aligned with the broader digital health transformation efforts supported by:

- **med.ai** → digital health toolkit for community and off-site care  
- **RKI (Robert Koch Institute)** → methodological analysis and redesign support  
- **p53-react Initiative** → global health implementation program (where this work is embedded)  
- **Planned AWS deployment** → scalable, cloud-based inference architecture  

This project serves as a **portfolio-ready demonstration** of how ML can support oncology care delivery in resource-limited settings.

---

# 🩺 1. Problem Overview

Off-site oncology care in LMIC contexts faces major challenges:

- Long patient travel distances  
- Overloaded central hospitals  
- Limited oncology specialists  
- Fragmented reporting from remote clinics  
- Late detection of deterioration  

Digital health platforms like **med.ai** collect patient data at off-site facilities, but **lack automated analytics** to:

- Prioritize high‑risk patients  
- Detect deterioration early  
- Trigger clinician alerts  
- Improve referral patterns  

This prototype demonstrates how a **lightweight ML model** can support these workflows.

---

# 🤖 2. ML Solution Summary

A **Random Forest Classifier** predicts:

### **“Is this patient at risk of clinical deterioration?”**  
(0 = low risk, 1 = high risk)

### Inputs used
- Symptom severity  
- Time since last visit  
- Treatment adherence  
- Side‑effect severity  
- Digital reporting activity (from med.ai logs)

### Capabilities
✔ Data preprocessing  
✔ ML model training  
✔ Inference demo  
✔ Feature importance visualization  
✔ AWS-ready workflow  

---

# 🗂️ 3. Repository Structure

```
├── README.md
├── main.py
├── data/
│   └── synthetic_medai_senegal.csv
├── requirements.txt
└── feature_importance.png
```

---

# 🧠 4. Methods

### Model
- **Random Forest Classifier (scikit-learn)**  
Chosen for simplicity, robustness, and interpretability.

### Metrics
- Precision  
- Recall  
- F1-score  
- Confusion matrix  

### Why useful for Oncology
- Supports triage  
- Detects deteriorating patients earlier  
- Reduces central hospital load  
- Supports follow-up scheduling  

---

# ☁️ 5. AWS Deployment Vision

```
 med.ai App (Senegal)
          │
          ▼
     S3 Data Lake
          │
          ▼
  AWS Lambda Inference
          │
          ▼
 RandomForest ML Model
          │
          ▼
   API Gateway → clinician dashboard
```

---

# ▶️ 6. Running the Project

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
python main.py
```

Outputs:
- classification report  
- feature importance plot  
- sample prediction  

---

# 🔮 7. Future Work

- Real med.ai data ingestion  
- Survival models (Cox, Weibull)  
- SHAP explainability  
- Sagemaker training pipelines  
- Model monitoring  
- Triage integration for LMIC oncology programs  

---

# 📝 License
MIT License

---

# ✨ Author
**Douglas Norberto**  
Digital Health • Data Science • Oncology Analytics  
Berlin, Germany  

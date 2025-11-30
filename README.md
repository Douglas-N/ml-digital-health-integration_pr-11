# ML-Driven Digital Health Tools for Off-Site Oncology Care Integration  
### Using Machine Learning to Improve Scalable, Accessible, and Efficient Oncology Care in LMIC Settings

This repository contains a machine-learning prototype demonstrating how digital health data from off-site care centers in Senegal (collected through the **med.ai** platform) can support oncology care coordination, early detection of patient deterioration, and more efficient referral workflows.

The prototype aligns with broader digital health transformation efforts supported by:

- **med.ai** – digital health toolkit for community and off-site care  
- **RKI (Robert Koch Institute)** – methodological analysis and redesign support  
- **p53-react Initiative** – implementation program where this work is embedded  
- Planned **AWS deployment** – cloud-based inference infrastructure  

This project serves as a demonstration of how ML can support oncology care delivery in resource-limited settings.

---

## 1. Problem Overview

Off-site oncology care in LMIC contexts faces significant challenges:

- Long patient travel distances  
- Overloaded central hospitals  
- Limited oncology specialists  
- Fragmented reporting from remote clinics  
- Delayed detection of clinical deterioration  

Digital health platforms like **med.ai** improve data collection but currently lack automated analytics to:

- Identify high-risk patients  
- Detect deterioration early  
- Trigger clinician alerts  
- Improve referral workflows  

This project demonstrates how a lightweight ML model can support these workflows.

---

## 2. Machine Learning Solution Summary

A **Random Forest Classifier** predicts the probability of a patient being at **high risk of clinical deterioration**.

**Prediction target**  
- 0 = Low-risk patient  
- 1 = High-risk patient  

**Features included**  
- Symptom severity score  
- Days since last clinical visit  
- Treatment adherence  
- Side-effect severity  
- Digital reporting activity (from med.ai logs)

**Pipeline capabilities**  
- Data preprocessing  
- Model training and validation  
- Feature importance visualization  
- Inference on sample patient data  
- AWS-ready structure for deployment  

---

## 3. Repository Structure

```
├── README.md
├── main.py
├── data/
│   └── synthetic_medai_senegal.csv
├── requirements.txt
└── feature_importance.png
```

---

## 4. Methods

### Model  
Random Forest Classifier (scikit-learn).  
Selected due to robustness, interpretability, and suitability for small, noisy datasets.

### Evaluation Metrics  
- Precision  
- Recall  
- F1-score  
- Confusion matrix  

### Relevance for Oncology Care  
- Supports triage  
- Enables earlier identification of deterioration  
- Reduces pressure on centralized oncology hospitals  
- Facilitates follow-up and care continuity  

---

## 5. AWS Deployment Vision

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
API Gateway → Clinician Dashboard
```

This architecture supports real-time inference and scalable deployment for global health applications.

---

## 6. Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run model training and evaluation:

```bash
python main.py
```

Outputs include:

- Model performance metrics (printed to console)  
- Feature importance plot (saved as `feature_importance.png`)  
- Example prediction for a single patient sample  

---

## 7. Future Work

- Integration with real med.ai datasets  
- Time-series models for symptom trajectory forecasting  
- Survival analysis models (CoxPH, Weibull)  
- Explainability via SHAP  
- AWS Sagemaker training pipelines  
- Model monitoring and retraining  
- Integration with digital triage tools for LMIC oncology programs  

---

## License  
MIT License

---

## Author  
**Douglas Norberto**  
Digital Health • Data Science • Oncology Analytics  
Berlin, Germany  

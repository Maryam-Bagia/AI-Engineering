# Diabetes Prediction ML

A beginner-friendly end-to-end machine-learning project that predicts diabetes risk from basic health information. It uses a **Random Forest** classifier because it performed well in your early experiments.

> Important: this is an educational project, not a medical tool. A prediction must never replace advice from a qualified healthcare professional.

## Project structure

```text
Diabetes-Prediction-ML/
│
├── dataset/
│   └── diabetes.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_PCA_KMeans.ipynb
│
├── models/
│   └── diabetes_model.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to run the project

Open PowerShell or a terminal in this project folder.

### Before you start: Python

You need Python 3.10 or newer. Check it with:

```powershell
python --version
```

If this shows a Microsoft Store message or does not show a version, install Python from the official Python website and select **Add Python to PATH** during installation. Then close and reopen PowerShell.

### 1. Create and activate a virtual environment (recommended)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the same terminal and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 2. Install the packages

```powershell
python -m pip install -r requirements.txt
```

### 3. Open the notebooks

```powershell
jupyter notebook
```

Run the notebooks in this order:

1. `01_EDA.ipynb` — explore the dataset.
2. `02_Preprocessing.ipynb` — prepare features for a model.
3. `03_Model_Training.ipynb` — train, evaluate, and save the Random Forest model.
4. `04_PCA_KMeans.ipynb` — a separate, optional PCA and K-Means exploration.

Run every cell in notebook 03 before starting the web app. It creates `models/diabetes_model.pkl`.

### 4. Start the web app

```powershell
python -m streamlit run app.py
```

Your browser should open automatically. Enter a person's health details and select **Predict risk**.

## What to study in the code

1. `01_EDA.ipynb` — how to inspect data before building a model.
2. `02_Preprocessing.ipynb` — why categories must become numbers for a model.
3. `03_Model_Training.ipynb` — `train_test_split`, `Pipeline`, Random Forest, and model evaluation.
4. `04_PCA_KMeans.ipynb` — how PCA reduces many features to two dimensions and how K-Means finds groups.
5. `app.py` — how `predict_proba` turns a model into a small web app.

## A note on accuracy

Diabetes is less common than non-diabetes in this dataset. Accuracy by itself can therefore be misleading. Read the precision, recall, and F1-score in notebook 03 too—especially for class `1` (diabetes).

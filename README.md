# 🧪 Data Analytics Lab Practical Guide (Step-by-Step)

This complete guide will help you perform all required practical tasks
for your lab:

------------------------------------------------------------------------

## 1️⃣ Install Anaconda & Verify Python Installation

### 🔹 What is Anaconda?

Anaconda is a Python distribution that includes Python, Jupyter
Notebook, and many data science libraries pre-installed.

### 🖥 Step 1: Download Anaconda

-   Go to: https://www.anaconda.com\
-   Download Python 3.x version\
-   Install with default settings

### 🔹 Step 2: Verify Python Installation

After installation:

Open Anaconda Prompt and type:

    python --version

You should see output like:

    Python 3.x.x

To check Conda version:

    conda --version

✅ If versions appear → Installation successful.

------------------------------------------------------------------------

## 2️⃣ Set Up Jupyter Notebook & Google Colab

### 🔹 A. Jupyter Notebook Setup

Jupyter comes pre-installed with Anaconda.

▶ To Launch:

Open Anaconda Navigator → Click Launch under Jupyter Notebook\
OR use command:

    jupyter notebook

Your browser will open Jupyter dashboard.

▶ Create First Notebook: - Click New\
- Select Python 3\
- Rename file (e.g., `Lab_Practical_1.ipynb`)

------------------------------------------------------------------------

### 🔹 B. Google Colab Setup

Google Colab is an online Jupyter notebook that runs in the browser (no
installation needed).

▶ Steps: - Visit: https://colab.research.google.com\
- Sign in with Google account\
- Click New Notebook

✅ Advantage: Free GPU & cloud execution.

------------------------------------------------------------------------

## 3️⃣ Install Essential Libraries

Required libraries: - pandas\
- NumPy\
- matplotlib\
- seaborn

### 🔹 Using Anaconda Prompt:

    conda install pandas numpy matplotlib seaborn

OR using pip:

    pip install pandas numpy matplotlib seaborn

### 🔹 Verify Installation in Notebook:

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries Installed Successfully")
```

If no errors → Installation successful ✅

------------------------------------------------------------------------

## 4️⃣ Create First Jupyter Notebook (Basic Python Operations)

Open new notebook and write:

``` python
# Basic operations

a = 10
b = 5

# Arithmetic
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# List example
numbers = [1, 2, 3, 4, 5]
print("List:", numbers)

# NumPy example
array = np.array(numbers)
print("NumPy Array:", array)

# Simple pandas DataFrame
data = {
    "Name": ["Ali", "Sara", "John"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)
```

📌 Run cell using **Shift + Enter**

------------------------------------------------------------------------

## 5️⃣ Data Analytics Use Cases Across Industries

Data Analytics is used in almost every industry.

### 🏥 1. Healthcare

-   Disease prediction\
-   Patient data analysis\
-   Medical imaging\
-   Example: Predicting diabetes using patient data

### 🏦 2. Banking & Finance

-   Fraud detection\
-   Risk analysis\
-   Credit scoring\
-   Stock market prediction

### 🛒 3. Retail & E-commerce

-   Customer behavior analysis\
-   Sales forecasting\
-   Recommendation systems\
-   Example: Amazon product recommendations

### 🚗 4. Transportation

-   Route optimization\
-   Traffic prediction\
-   Ride demand forecasting

### 🎓 5. Education

-   Student performance analysis\
-   Dropout prediction\
-   Personalized learning systems

### 🏭 6. Manufacturing

-   Quality control\
-   Predictive maintenance\
-   Supply chain optimization

------------------------------------------------------------------------

## 📊 Common Tools Used in Data Analytics

  Tool         Purpose
  ------------ ---------------------------
  Python       Data processing
  Pandas       Data manipulation
  NumPy        Numerical computing
  Matplotlib   Data visualization
  Seaborn      Statistical visualization
  SQL          Database querying

------------------------------------------------------------------------

### ✅ Final Lab Checklist

-   Install Anaconda\
-   Verify Python\
-   Launch Jupyter\
-   Open Google Colab\
-   Install required libraries\
-   Create first notebook\
-   Understand industry use cases

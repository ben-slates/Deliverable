# 🧪 Data Analytics Lab Practical Guide (Step-by-Step)

This complete guide will help you perform all required practical tasks for your lab:

------------------------------------------------------------------------

## 1️⃣ Install Anaconda & Verify Python Installation

### 🔹 What is Anaconda?

Anaconda is a Python distribution that includes Python, Jupyter Notebook, and many data science libraries pre-installed.

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

Google Colab is an online Jupyter notebook that runs in the browser (no installation needed).

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

| Tool       | Purpose                   |
|------------|---------------------------|
| Python     | Data processing           |
| Pandas     | Data manipulation         |
| NumPy      | Numerical computing       |
| Matplotlib | Data visualization        |
| Seaborn    | Statistical visualization |
| SQL        | Database querying         |

------------------------------------------------------------------------

### ✅ Final Lab Checklist

-   Install Anaconda\
-   Verify Python\
-   Launch Jupyter\
-   Open Google Colab\
-   Install required libraries\
-   Create first notebook\
-   Understand industry use cases

------------------------------------------------------------------------

## Python Data Processing Assignment

### Objectives

This assignment demonstrates the following Python concepts:

-   Python Data Structures (Lists, Dictionaries, Tuples, Sets)
-   Functions for Data Processing
-   Reading and Writing Files (CSV, JSON, Text)
-   List Comprehensions
-   Error and Exception Handling

### Dataset

-   Student grades dataset (CSV)
-   Sales dataset

### Deliverable

A Jupyter Notebook containing Python exercises and file processing examples.

### Technologies Used

-   Python
-   Jupyter Notebook
-   CSV / JSON file handling

## 6️⃣ Advanced Python Data Processing Techniques

This section delves into more sophisticated Python techniques essential for robust data processing and analysis.

### 🔹 7. Work with Python Data Structures

Understanding and effectively utilizing Python's built-in data structures is fundamental for efficient data manipulation. This includes:

-   **Lists**: Ordered, mutable collections of items.
-   **Dictionaries**: Unordered, mutable collections of key-value pairs.
-   **Tuples**: Ordered, immutable collections of items.
-   **Sets**: Unordered collections of unique items.

### 🔹 8. Write Functions for Data Processing

Functions are crucial for organizing code, promoting reusability, and performing specific data processing tasks. This involves defining custom functions to clean, transform, and analyze data.

### 🔹 9. Read and Write CSV, JSON, and Text Files

Data often originates from or needs to be stored in various file formats. Proficiency in handling these formats programmatically is vital:

-   **CSV (Comma Separated Values)**: Commonly used for tabular data.
-   **JSON (JavaScript Object Notation)**: Lightweight data-interchange format, often used for web data.
-   **Text Files**: General-purpose files for storing unstructured or semi-structured data.

### 🔹 10. Use List Comprehensions for Efficient Data Transformation

List comprehensions provide a concise way to create lists. They are often more readable and efficient than traditional `for` loops for certain data transformation tasks.

### 🔹 11. Handle Errors and Exceptions in Data Processing

Robust data processing requires anticipating and gracefully handling errors. This involves using `try-except` blocks to manage exceptions that may arise during file operations, data conversions, or calculations.

### Exercise Dataset

To practice these advanced techniques, the following datasets are recommended:

-   **Student Grades CSV File**: A dataset containing student scores and related information, ideal for practicing data cleaning, aggregation, and analysis.
-   **Simple Sales Data**: A dataset detailing sales transactions, suitable for exercises involving data filtering, transformation, and reporting.

### Deliverable

The culmination of these exercises will be a **Jupyter Notebook** containing Python code examples that demonstrate proficiency in all the advanced data processing concepts covered, along with practical file processing examples using the specified datasets.

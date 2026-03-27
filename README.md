# 📊 Data Analytics Laboratory: Comprehensive Practical Guide

This repository contains a series of laboratory exercises and projects designed to build a strong foundation in **Data Analytics** using Python. The curriculum progresses from environment setup and basic data structures to advanced numerical computing with **NumPy**, data cleaning with **Pandas**, and professional **Data Visualization**.

---

## 📂 Project Structure

The project is organized into five main laboratory modules, each focusing on specific aspects of the data analytics pipeline:

```text
.
└── Deliverable
    ├── lab_1/                         # Environment Setup & Introduction
    │   ├── lab_1.ipynb
    │   ├── Images/                    # Custom Images (0.png, 1.webp, ...)
    │   └── code_with_output_images/   # Code + Output Images (cell_1.png → cell_4.png)
    │
    ├── lab_2/                         # Advanced Python Data Processing
    │   ├── lab_2.ipynb
    │   ├── data/                      # CSV Datasets (sales.csv, students.csv)
    │   ├── images/                    # Conceptual Images
    │   ├── code_with_output_images/   # Code + Output Images (cell_1 → cell_8)
    │   ├── students.json              # JSON Dataset
    │   └── notes.txt                  # Notes
    │
    ├── lab_3/                         # Numerical Computing with NumPy
    │   ├── numpy_stock_analysis/
    │   │   ├── lab_3.ipynb
    │   │   ├── AAPL_stock_data.csv
    │   │   ├── AAPL_stock_data_cleaned.csv
    │   │   └── images/
    │   ├── Clean_data.py
    │   ├── create_clened_csv.py
    │   ├── Download_data.py
    │   ├── Images/                    # NumPy Concept Images
    │   └── requirements.txt
    │
    ├── lab_4/                         # Data Exploration & Cleaning
    │   ├── lab_4.ipynb
    │   ├── data.csv                   # Dataset
    │   ├── real_estate_cleaned.csv
    │   └── images/                    # Code Cell Images (cell_1 → cell_8)
    │
    ├── lab_5/                         # Data Visualization Portfolio
    │   ├── lab_5.ipynb
    │   ├── data.csv                   # Dataset
    │   └── images/                    # Code Cell Images (cell_1 → cell_14)
    │
    ├── manual/                        # Documentation (All Labs)
    │   ├── lab1/
    │   │   ├── lab_1.docx
    │   │   ├── lab_1.pdf
    │   │   └── Images/                # Code + Custom Images
    │   ├── lab2/
    │   │   ├── lab_2.docx
    │   │   ├── lab_2.pdf
    │   │   └── images/                # Code + Custom Images
    │   ├── lab3/
    │   │   ├── Lab_3.docx
    │   │   ├── Lab_3.pdf
    │   │   └── images/               # Code + Custom Images
    │   ├── lab4/
    │   │   ├── lab_4.docx
    │   │   ├── lab_4.pdf
    │   │   └── images/                # Code + Custom Images
    │   └── lab5/
    │       ├── lab_5.docx
    │       ├── lab_5.pdf
    │       └── images/              # Code + Custom Images
    │
    └── README.md                      # Project Documentation
```

---

## 🛠️ Phase 1: Environment Setup & Foundation (Lab 1)

The initial phase focuses on establishing a robust development environment for data science.

### 🔹 1. Installation & Verification
*   **Anaconda Distribution**: A comprehensive Python distribution including Jupyter Notebooks and essential data science libraries.
    *   Download: [Anaconda Official Site](https://www.anaconda.com)
*   **Verification**:
    ```bash
    python --version
    conda --version
    ```
*   **Alternative**: **Google Colab** for cloud-based execution without local installation.

### 🔹 2. Essential Library Stack
The following libraries are fundamental to the workflow:
| Library | Purpose |
| :--- | :--- |
| **Pandas** | High-performance data manipulation and analysis |
| **NumPy** | Fundamental package for scientific computing |
| **Matplotlib** | Comprehensive library for static, animated, and interactive visualizations |
| **Seaborn** | Statistical data visualization based on Matplotlib |

---

## 🐍 Phase 2: Advanced Python Data Processing (Lab 2)

This module transitions from basic syntax to sophisticated data handling techniques required for professional data engineering.

### 🔹 Key Learning Objectives
*   **Data Structures**: Mastering the use of Lists, Dictionaries, Tuples, and Sets for efficient data storage.
*   **Functional Programming**: Writing modular, reusable functions for data cleaning and transformation.
*   **File I/O Operations**: Programmatic interaction with various data formats (CSV, JSON, Text).
*   **Efficiency**: Utilizing **List Comprehensions** for concise and readable code.
*   **Robustness**: Implementing `try-except` blocks for graceful error and exception handling.

---

## 📈 Phase 3: Numerical Computing & Stock Analysis (Lab 3)

This module demonstrates high-performance numerical computing using **NumPy**, applied to historical financial data for Apple Inc. (AAPL).

### 🔹 Practical NumPy Tasks
1.  **Array Manipulation**: Creation and transformation of 1D, 2D, and 3D arrays.
2.  **Advanced Indexing**: Slicing and reshaping techniques for time-series data analysis.
3.  **Mathematical Operations**: Leveraging **Broadcasting** and element-wise operations.
4.  **Statistical Analysis**: Computing Mean, Median, Standard Deviation, and Percentiles.
5.  **Linear Algebra**: Applying dot products for portfolio weighting.

---

## 🔍 Phase 4: Data Exploration & Cleaning (Lab 4)

This module focuses on practical data exploration and cleaning using **Pandas** on a real estate transaction dataset.

### 🔹 Key Cleaning & Exploration Tasks
*   **Initial Inspection**: Using `head()`, `tail()`, `info()`, and `describe()` to understand data structure.
*   **Filtering & Selection**: Isolating specific data subsets based on complex conditions (e.g., price and location).
*   **Missing Data Management**: Identifying and imputing missing values using mean/mode strategies.
*   **Data Transformation**: Feature engineering (e.g., PricePerYear) and column normalization.
*   **Exporting**: Saving the final cleaned dataset for downstream analysis.

---

## 🎨 Phase 5: Data Visualization Portfolio (Lab 5)

The final module showcases professional data visualization techniques using **Matplotlib** and **Seaborn** on a global COVID-19 dataset.

### 🔹 Visualization Techniques Included
*   **Trend Analysis**: Line plots and area plots for time-series tracking.
*   **Categorical Comparison**: Bar charts and count plots for regional statistics.
*   **Distribution Analysis**: Histograms, box plots, and violin plots.
*   **Relationship Mapping**: Scatter plots with multi-dimensional encoding (color, size).
*   **Statistical Correlation**: Heatmaps for identifying variable dependencies.
*   **Multi-panel Figures**: Utilizing subplots for complex data storytelling.

---

## 🏥 Industry Use Cases

Data analytics techniques covered in these labs are applied across various sectors:

| Industry | Application Examples |
| :--- | :--- |
| **Healthcare** | Disease prediction, patient data analysis, and COVID-19 spread tracking. |
| **Finance** | Fraud detection, risk analysis, and stock market prediction. |
| **Retail** | Customer behavior analysis and recommendation systems. |
| **Real Estate** | Property valuation, market trend analysis, and investment risk assessment. |
| **Manufacturing** | Predictive maintenance and quality control optimization. |

---

## ✅ Final Lab Checklist

- [x] Successfully installed and verified Anaconda/Python environment.
- [x] Demonstrated proficiency in Python data structures (Lists, Dicts, Tuples).
- [x] Implemented file I/O for CSV and JSON datasets.
- [x] Executed complex numerical operations using NumPy on financial datasets.
- [x] Performed end-to-end data cleaning and exploration on real estate data.
- [x] Developed a comprehensive visualization portfolio with 10+ chart types.

---

*This project was developed as part of the Data Analytics Laboratory curriculum.*

## 👥 Project Contributors
- **Muhamad Umer Farooq**
- **Muhammad Ahmad**
- **Muhammad Zaid Tahir**

### Group Members
- **Muhammad Huzaifa Khalid**
- **Ali Hammad Subhani**

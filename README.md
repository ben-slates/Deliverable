# 📊 Data Analytics Laboratory: Comprehensive Practical Guide

This repository contains a series of laboratory exercises and projects designed to build a strong foundation in **Data Analytics** using Python. The curriculum progresses from environment setup and basic data structures to advanced numerical computing with **NumPy** and real-world financial data analysis.

---

## 📂 Project Structure

The project is organized into three main laboratory modules, each focusing on specific aspects of the data analytics pipeline:

```
.
└── Deliverable
    ├── lab 1/                 # Environment Setup & Introduction
    │   ├── Practical_Task_1.ipynb
    │   └── [Supporting Images & Documentation]
    ├── lab 2/                 # Advanced Python Data Processing
    │   ├── assignment.ipynb
    │   ├── data/              # CSV Datasets (Sales, Students)
    │   ├── images/            # Conceptual Diagrams
    │   └── students.json      # JSON Dataset
    ├── lab 3/                 # Numerical Computing with NumPy
    │   ├── numpy_stock_analysis/
    │   │   ├── numpy_stock_operations.ipynb
    │   │   └── AAPL_stock_data.csv
    │   ├── Clean_data.py
    │   ├── Download_data.py
    │   └── requirements.txt
    └── README.md              # Project Documentation
```

---

## 🛠️ Phase 1: Environment Setup & Foundation (Lab 1)

The initial phase focuses on establishing a robust development environment for data science.

### 🔹 1. Installation & Verification

- **Anaconda Distribution**: A comprehensive Python distribution including Jupyter Notebooks and essential data science libraries.
  - Download: [Anaconda Official Site](https://www.anaconda.com)

- **Verification**:

   ```bash
   python --version
   conda --version
   ```

- **Alternative**: **Google Colab** for cloud-based execution without local installation.

### 🔹 2. Essential Library Stack

The following libraries are fundamental to the workflow:

| Library | Purpose |
| --- | --- |
| **Pandas** | High-performance data manipulation and analysis |
| **NumPy** | Fundamental package for scientific computing |
| **Matplotlib** | Comprehensive library for static, animated, and interactive visualizations |
| **Seaborn** | Statistical data visualization based on Matplotlib |

---

## 🐍 Phase 2: Advanced Python Data Processing (Lab 2)

This module transitions from basic syntax to sophisticated data handling techniques required for professional data engineering.

### 🔹 Key Learning Objectives

- **Data Structures**: Mastering the use of Lists, Dictionaries, Tuples, and Sets for efficient data storage.

- **Functional Programming**: Writing modular, reusable functions for data cleaning and transformation.

- **File I/O Operations**: Programmatic interaction with various data formats:
  - **CSV**: Tabular data handling.
  - **JSON**: Working with semi-structured web data.
  - **Text**: Processing unstructured data.

- **Efficiency**: Utilizing **List Comprehensions** for concise and readable code.

- **Robustness**: Implementing `try-except` blocks for graceful error and exception handling.

---

## 📈 Phase 3: Numerical Computing & Stock Analysis (Lab 3)

The final module demonstrates high-performance numerical computing using **NumPy**, applied to historical financial data for Apple Inc. (AAPL).

### 🔹 Practical NumPy Tasks

1. **Array Manipulation**: Creation and transformation of 1D, 2D, and 3D arrays (representing Weeks × Days × Metrics).

1. **Advanced Indexing**: Slicing and reshaping techniques for time-series data analysis.

1. **Mathematical Operations**: Leveraging **Broadcasting** and element-wise operations for efficient computation.

1. **Statistical Analysis**: Computing Mean, Median, Standard Deviation, and Percentiles.

1. **Linear Algebra**: Applying dot products and matrix multiplications for portfolio weighting.

1. **Random Sampling**: Generating distributions for stochastic modeling.

### 🚀 Performance Benchmark

A key component of this lab is the performance comparison between **NumPy** and native **Python Lists**.

> **Finding**: NumPy operations are typically **50x to 100x faster** than standard lists for large-scale numerical tasks, illustrating why it is the industry standard for scientific computing.

---

## 🏥 Industry Use Cases

Data analytics techniques covered in these labs are applied across various sectors:

| Industry | Application Examples |
| --- | --- |
| **Healthcare** | Disease prediction, patient data analysis, and medical imaging. |
| **Finance** | Fraud detection, risk analysis, and stock market prediction. |
| **Retail** | Customer behavior analysis and recommendation systems (e.g., Amazon). |
| **Manufacturing** | Predictive maintenance and quality control optimization. |
| **Education** | Student performance analysis and personalized learning systems. |

---

## ✅ Final Lab Checklist

- [x] Successfully installed and verified Anaconda/Python environment.

- [x] Configured Jupyter Notebook and Google Colab environments.

- [x] Demonstrated proficiency in Python data structures (Lists, Dicts, Tuples).

- [x] Implemented file I/O for CSV and JSON datasets.

- [x] Executed complex numerical operations using NumPy on financial datasets.

- [x] Conducted performance benchmarking for vectorized operations.

---

*This project was developed as part of the Data Analytics Laboratory curriculum.*


## 👥 Project Contributors

This project was built by:
- **Muhamad Umer Farooq**
- **Muhammad Ahmed**
- **Zaid Tahir**

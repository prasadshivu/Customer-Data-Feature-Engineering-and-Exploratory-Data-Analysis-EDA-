# 📊 Customer Data Feature Engineering and Exploratory Data Analysis (EDA)

A Python-based data analysis project that demonstrates **Feature Engineering** and **Exploratory Data Analysis (EDA)** using customer data. The project focuses on understanding the dataset, handling missing values, analyzing feature relationships, visualizing data distributions, and detecting outliers using popular Python data science libraries.

---

# 🚀 Project Overview

This project performs data preprocessing and exploratory analysis on a customer dataset to prepare it for machine learning or business analytics. It includes:

* Dataset loading and validation
* Data cleaning
* Handling missing values
* Statistical analysis
* Data visualization
* Correlation analysis
* Outlier detection

---

# ✨ Features

* Load CSV dataset
* Validate dataset existence and size
* Remove duplicate header rows
* Convert columns to appropriate numeric data types
* Handle missing values using:

  * Median Imputation
  * Mean Imputation
* Generate descriptive statistics
* Plot spending distribution
* Create correlation heatmap
* Detect outliers using boxplots
* Identify customers with abnormal age values

---

# 📂 Dataset

**Dataset File:** `data.csv`

The dataset contains customer information such as:

* Customer_ID
* Age
* Spending
* Visits_Per_Month

---

# 🛠️ Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# 📦 Required Libraries

Install the required dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

---

# 📁 Project Structure

```text
Feature-Engineering-EDA/
│
├── data.csv
├── feature_engineering.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Project Workflow

1. Load the customer dataset
2. Validate the dataset
3. Remove duplicate header rows
4. Convert columns to numeric data types
5. Handle missing values
6. Generate descriptive statistics
7. Visualize spending distribution
8. Calculate feature correlations
9. Plot a correlation heatmap
10. Detect outliers using a boxplot
11. Display abnormal customer records

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/Feature-Engineering-EDA.git
```

Navigate to the project directory:

```bash
cd Feature-Engineering-EDA
```

Run the project:

```bash
python "feature _engineering.py"
```

---

# 📈 Output

The project generates:

* Dataset information
* Summary statistics
* Missing value report
* Spending distribution histogram
* Correlation matrix
* Correlation heatmap
* Age boxplot
* Outlier records

---

# 📚 Concepts Demonstrated

* Data Cleaning
* Data Validation
* Missing Value Imputation
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Data Visualization
* Correlation Analysis
* Outlier Detection

---

# 📊 Libraries Used

| Library    | Purpose                             |
| ---------- | ----------------------------------- |
| Pandas     | Data manipulation and preprocessing |
| NumPy      | Numerical operations                |
| Matplotlib | Data visualization                  |
| Seaborn    | Statistical visualizations          |

---

# 🔮 Future Improvements

* Add feature scaling using StandardScaler or MinMaxScaler
* Encode categorical variables
* Perform feature selection
* Build machine learning models
* Create interactive dashboards using Plotly or Streamlit
* Export cleaned data for further analysis

---

# 👨‍💻 Author

**Shivaprasad m s**

This project was created to demonstrate practical data preprocessing and exploratory data analysis techniques using Python. If you find this project helpful, feel free to ⭐ star the repository and contribute with improvements.

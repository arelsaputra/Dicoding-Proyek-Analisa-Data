Data Analysis Dashboard

This dashboard is created to analyze transaction data and customer reviews.

Project Description

This project aims to implement data exploration and analysis techniques using Python and libraries such as Pandas, Matplotlib, and Seaborn. This dashboard helps in data visualization to get clearer insights.

Analysis Stages:

1. **Data Understanding** – Understand the structure and characteristics of the dataset.

2. **Data Cleaning** – Handle missing or invalid data.

3. **Exploratory Data Analysis (EDA)** – Perform statistical analysis and data visualization.

4. **Dashboard Development** – Create an interactive dashboard for data analysis.

5. **Insight & Conclusion** – Summarize the analysis results to provide recommendations.

Technologies & Tools
- Python
- Pandas
- Matplotlib & Seaborn
- Streamlit / Dash for Dashboard
- Jupyter Notebook / Google Colab

Repository Structure
```
Submission Proyek Analisis Data
│── 📁 dataset/ # Datasets used
│── 📁 notebooks/ # Data analysis notebooks
│── 📁 dashboard/ # Code for analysis dashboard
│── 📄 README.md # Project description
│── 📄 requirements.txt # List of required libraries
```

Setup Environment

Using Google Colab
Make sure all required libraries are installed. Run the following command in Colab:
```python
!pip install -r requirements.txt
```

Using Virtual Environment (Local)
Run the following command to create and activate a virtual environment:
```bash
mkdir -Dicoding-Data-Scientist-Machine-Learning-Engineer
cd -Dicoding-Data-Scientist-Machine-Learning-Engineer

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Running the Dashboard
Run the following command in the terminal to open the dashboard:
```bash
streamlit run dashboard.py
```

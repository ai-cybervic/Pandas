# Smart Data Normalization and Cleaning Assistant

This project provides an interactive Streamlit web application that allows users to upload, inspect, clean, and normalize datasets in CSV, Excel, or JSON formats.  
It simplifies common data preprocessing tasks using Python, pandas, and numpy.

---

## Features

- Upload CSV, Excel, or JSON files  
- View dataset previews and descriptive statistics  
- Clean data with the following options:
  - Remove duplicate rows  
  - Handle missing values (drop, fill with mean/median/mode, or a custom value)  
  - Normalize numeric columns (scale 0–1)  
  - Encode categorical variables automatically  
- Download the cleaned dataset as a CSV file  

---

## Requirements

- Python 3.8 or higher
- pandas
- numpy
- streamlit

To install all dependencies, run:

```bash
pip install streamlit pandas numpy
Or, if you have a requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
2. Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Linux or macOS
# OR
venv\Scripts\activate      # On Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
If you don’t have a requirements file yet, generate one using:

bash
Copy code
pip freeze > requirements.txt
Running the Application
bash
Copy code
streamlit run test.py
Then open your browser and visit:

arduino
Copy code
http://localhost:8501
Usage
Upload your dataset file (.csv, .xlsx, .xls, or .json)

Review the dataset preview and summary

Select cleaning and normalization options

Click Clean and Normalize Data

Download the cleaned dataset

Example Code Snippet
python
Copy code
import streamlit as st
import pandas as pd
import numpy as np

st.title("Smart Data Normalization and Cleaning Assistant")

uploaded_file = st.file_uploader("Upload dataset", type=["csv", "xlsx", "xls", "json"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
Troubleshooting
Error:
pandas.errors.EmptyDataError: No columns to parse from file

Fix:

Ensure the uploaded file is not empty

Verify that the file format is correct (CSV, Excel, or JSON)

Confirm the file path or upload source

Technologies Used
Python

Streamlit

pandas

numpy

scikit-learn

matplotlib

seaborn

plotly

Author
Vic
Email: authkarimi1@gmail.com

For data science or machine learning collaborations, contact the author via email.

License
This project is licensed under the MIT License. See the LICENSE file for details.

yaml
Copy code

---

Would you like me to generate the **MIT LICENSE** file text next (so your GitHub repo is complete)?






You said:

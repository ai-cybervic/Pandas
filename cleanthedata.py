import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Normalization Assistant", layout="wide")

st.title("🧹 Smart Data Normalization & Cleaning Assistant")

# ------------------------------
# File Upload
# ------------------------------
uploaded_file = st.file_uploader("📂 Upload your dataset (CSV, Excel, or JSON)", type=["csv", "xlsx", "xls", "json"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()

    # ------------------------------
    # Auto-load based on file type
    # ------------------------------
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_type in ["xlsx", "xls"]:
        df = pd.read_excel(uploaded_file)
    elif file_type == "json":
        df = pd.read_json(uploaded_file)
    else:
        st.error("Unsupported file format.")
        st.stop()

    st.success(f"✅ Loaded {file_type.upper()} file successfully!")
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

    # ------------------------------
    # Show preview and info
    # ------------------------------
    with st.expander("👀 Preview Data"):
        st.dataframe(df.head())

    with st.expander("📊 Dataset Summary"):
        st.write(df.describe(include='all'))

    with st.expander("🧩 Column Info"):
        st.write(pd.DataFrame({
            "Data Type": df.dtypes,
            "Missing Values": df.isnull().sum(),
            "Unique Values": df.nunique()
        }))

    # ------------------------------
    # Cleaning Options
    # ------------------------------
    st.header("⚙️ Cleaning Options")

    remove_duplicates = st.checkbox("Remove duplicate rows", value=True)
    handle_missing = st.selectbox("Handle missing values", ["Do nothing", "Drop missing rows", "Fill with mean/median/mode", "Fill with custom value"])
    normalize_data = st.checkbox("Normalize numeric columns (scale 0-1)")
    encode_categorical = st.checkbox("Encode categorical variables")

    # ------------------------------
    # Apply cleaning
    # ------------------------------
    if st.button("🚀 Clean and Normalize Data"):
        df_cleaned = df.copy()

        # Remove duplicates
        if remove_duplicates:
            df_cleaned = df_cleaned.drop_duplicates()

        # Handle missing values
        if handle_missing == "Drop missing rows":
            df_cleaned = df_cleaned.dropna()
        elif handle_missing == "Fill with mean/median/mode":
            for col in df_cleaned.columns:
                if df_cleaned[col].dtype in [np.float64, np.int64]:
                    df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
                else:
                    df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
        elif handle_missing == "Fill with custom value":
            fill_val = st.text_input("Enter custom fill value:")
            if fill_val:
                df_cleaned = df_cleaned.fillna(fill_val)

        # Normalize numeric columns
        if normalize_data:
            numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
            df_cleaned[numeric_cols] = (df_cleaned[numeric_cols] - df_cleaned[numeric_cols].min()) / (df_cleaned[numeric_cols].max() - df_cleaned[numeric_cols].min())

        # Encode categorical variables
        if encode_categorical:
            cat_cols = df_cleaned.select_dtypes(include=["object", "category"]).columns
            df_cleaned = pd.get_dummies(df_cleaned, columns=cat_cols, drop_first=True)

        st.success("✅ Data cleaned successfully!")

        with st.expander("🔍 Cleaned Data Preview"):
            st.dataframe(df_cleaned.head())

        # ------------------------------
        # Download option
        # ------------------------------
        csv = df_cleaned.to_csv(index=False).encode("utf-8")
        st.download_button("💾 Download Cleaned Data", csv, "cleaned_data.csv", "text/csv")

else:
    st.info("👆 Please upload a file to start.")

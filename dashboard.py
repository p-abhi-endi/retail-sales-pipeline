import streamlit as st
import pandas as pd
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='your_user',
    password='your_password',
    account='your_account'
)

@st.cache
def load_data():
    query = "SELECT order_date, SUM(sales_amount) as total_sales FROM retail_db.raw.retail_sales GROUP BY order_date ORDER BY order_date"
    cur = conn.cursor()
    cur.execute(query)
    df = pd.DataFrame(cur.fetchall(), columns=['order_date', 'total_sales'])
    return df

st.title("Retail Sales Dashboard")

data = load_data()

st.line_chart(data.set_index('order_date')['total_sales'])

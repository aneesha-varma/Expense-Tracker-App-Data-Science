import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------
# LOAD DATA
# -------------------
df = pd.read_csv("data/expenses.csv")
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()

st.title("💰 Expense Tracker Dashboard")

# -------------------
# FILTERS
# -------------------
category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[df["Category"].isin(category)]

# -------------------
# RAW DATA
# -------------------
if st.checkbox("Show Data"):
    st.write(filtered_df)

# -------------------
# CATEGORY CHART
# -------------------
st.subheader("📊 Category-wise Spending")

cat_data = filtered_df.groupby("Category")["Amount"].sum()

fig1, ax1 = plt.subplots()
cat_data.plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# -------------------
# MONTHLY TREND
# -------------------
st.subheader("📈 Monthly Spending Trend")

month_data = filtered_df.groupby("Month")["Amount"].sum()

fig2, ax2 = plt.subplots()
month_data.plot(kind="line", marker="o", ax=ax2)
st.pyplot(fig2)

# -------------------
# PIE CHART
# -------------------
st.subheader("🥧 Expense Distribution")

fig3, ax3 = plt.subplots()
ax3.pie(cat_data, labels=cat_data.index, autopct="%1.1f%%")
st.pyplot(fig3)

st.success("Dashboard Loaded Successfully 🚀")
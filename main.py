import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# 1️⃣ LOAD DATA
# =========================
df = pd.read_csv("data/expenses.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Category"] = df["Category"].str.title()

df["Month"] = df["Date"].dt.month_name()

print("✅ Data Loaded Successfully")

# =========================
# 2️⃣ CREATE OUTPUT FOLDER
# =========================
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# =========================
# 3️⃣ ANALYSIS
# =========================
category_sum = df.groupby("Category")["Amount"].sum()
monthly_sum = df.groupby("Month")["Amount"].sum()

print("📊 Category Analysis Done")

# =========================
# 4️⃣ CATEGORY BAR CHART
# =========================
plt.figure(figsize=(8,5))
category_sum.sort_values().plot(kind="bar", color="skyblue")
plt.title("Category-wise Spending")
plt.ylabel("Amount")

plt.tight_layout()
plt.savefig(f"{output_dir}/category_chart.png", dpi=300)
plt.show()

# =========================
# 5️⃣ PIE CHART
# =========================
plt.figure(figsize=(6,6))
plt.pie(category_sum, labels=category_sum.index, autopct="%1.1f%%")
plt.title("Expense Distribution")

plt.savefig(f"{output_dir}/pie_chart.png", dpi=300)
plt.show()

# =========================
# 6️⃣ MONTHLY TREND
# =========================
plt.figure(figsize=(8,5))
monthly_sum.plot(marker="o")
plt.title("Monthly Spending Trend")
plt.ylabel("Amount")

plt.savefig(f"{output_dir}/monthly_trend.png", dpi=300)
plt.show()

# =========================
# 7️⃣ INSIGHTS
# =========================
print("\n🔥 INSIGHTS")
print("Highest Spending Category:", category_sum.idxmax())
print("Total Spending:", df["Amount"].sum())
print("Average Expense:", df["Amount"].mean())
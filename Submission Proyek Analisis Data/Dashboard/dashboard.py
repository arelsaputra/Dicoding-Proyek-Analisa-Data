import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

st.title("Dashboard Analisis Data")

np.random.seed(42)
data = pd.DataFrame({
    "payment": np.random.exponential(scale=150, size=1000),
    "review_score": np.random.choice([1, 2, 3, 4, 5], size=1000, p=[0.1, 0.05, 0.15, 0.3, 0.4])
})

st.sidebar.header("Filter & Opsi Visualisasi")

st.sidebar.subheader("Filter Rentang Pembayaran")
min_pay, max_pay = st.sidebar.slider("Pilih Rentang Pembayaran", 
                                     min_value=float(data["payment"].min()), 
                                     max_value=float(data["payment"].max()), 
                                     value=(float(data["payment"].min()), float(data["payment"].max())))

st.sidebar.subheader("Opsi Histogram")
bins = st.sidebar.slider("Jumlah Bin", min_value=5, max_value=50, value=30)

show_kde = st.sidebar.checkbox("Tampilkan KDE (Density Curve)", value=True)

filtered_data = data[(data["payment"] >= min_pay) & (data["payment"] <= max_pay)]

st.sidebar.subheader("Opsi Visualisasi Skor Ulasan")
chart_type = st.sidebar.radio("Pilih Jenis Visualisasi", ["Bar Chart", "Pie Chart"])

st.sidebar.subheader("Filter Skor Ulasan")
selected_scores = st.sidebar.multiselect("Pilih Skor Ulasan yang Ditampilkan", options=[1, 2, 3, 4, 5], default=[1, 2, 3, 4, 5])

st.sidebar.subheader("Pilihan Warna")
color_palette = st.sidebar.selectbox("Pilih Palet Warna", ["Blues", "viridis", "coolwarm", "magma"])

avg_payment = filtered_data["payment"].mean()
median_payment = filtered_data["payment"].median()
std_payment = filtered_data["payment"].std()

st.subheader("Rata-rata Jumlah Pembayaran per Transaksi")
st.metric(label="Rata-rata Pembayaran", value=f"Rp {avg_payment:.2f}")
st.write(f"**Median**: Rp {median_payment:.2f} | **Standar Deviasi**: Rp {std_payment:.2f}")

st.subheader("Distribusi Pembayaran")
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(filtered_data["payment"], bins=bins, kde=show_kde, color="blue", ax=ax)
ax.axvline(avg_payment, color='red', linestyle='dashed', linewidth=2)
ax.set_xlabel("Jumlah Pembayaran (Rp)")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

st.subheader("Distribusi Skor Ulasan Pelanggan")
filtered_reviews = data[data["review_score"].isin(selected_scores)]

fig, ax = plt.subplots(figsize=(7, 4))
if chart_type == "Bar Chart":
    sns.countplot(x=filtered_reviews["review_score"], palette=color_palette, ax=ax)
    ax.set_xlabel("Skor Ulasan")
    ax.set_ylabel("Jumlah Ulasan")
else:
    review_counts = filtered_reviews["review_score"].value_counts()
    ax.pie(review_counts, labels=review_counts.index, autopct='%1.1f%%', colors=sns.color_palette(color_palette))
    ax.set_ylabel("")

st.pyplot(fig)

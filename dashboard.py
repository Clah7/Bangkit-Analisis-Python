import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('cleaned_data.csv')

# Membuat kolom TANGGAL dari kolom year, month, dan day
data['TANGGAL'] = pd.to_datetime(data[['year', 'month', 'day']])
st.title('Dashboard Kualitas Udara')

# Menampilkan data dalam tabel
st.subheader('Data Kualitas Udara')
st.dataframe(data)

# Menampilkan statistik deskriptif
st.subheader('Statistik Deskriptif')
st.write(data.describe())

# Menggambarkan grafik PM2.5
st.subheader('Grafik PM2.5')
plt.figure(figsize=(10, 5))
plt.plot(data['TANGGAL'], data['PM2.5'], label='PM2.5', color='blue')
plt.xlabel('Tanggal')
plt.ylabel('Konsentrasi PM2.5')
plt.title('Perubahan Konsentrasi PM2.5 dari Waktu ke Waktu')
plt.xticks(rotation=45)
plt.legend()
st.pyplot(plt)

# Menampilkan histogram dari PM2.5
st.subheader('Histogram PM2.5')
plt.figure(figsize=(10, 5))
plt.hist(data['PM2.5'], bins=30, color='blue', alpha=0.7)
plt.xlabel('Konsentrasi PM2.5')
plt.ylabel('Frekuensi')
plt.title('Histogram Konsentrasi PM2.5')
st.pyplot(plt)

# Menambahkan interaksi untuk memilih polutan yang ditampilkan
st.subheader('Visualisasi Interaktif Rata-rata Polutan per Tahun')
pollutants = ['PM2.5', 'PM10', 'CO', 'SO2', 'NO2', 'O3']
selected_pollutant = st.selectbox('Pilih polutan untuk ditampilkan', pollutants)

# Menghitung rata-rata polutan per tahun
average_pollutant_per_year = data.groupby('year')[selected_pollutant].mean()

# Membuat grafik
plt.figure(figsize=(10, 6))
average_pollutant_per_year.plot(kind='line', label=selected_pollutant, color='blue')
plt.title(f'Rata-rata {selected_pollutant} per Tahun')
plt.ylabel('Konsentrasi Rata-rata')
plt.xlabel('Tahun')
plt.legend(title='Polutan')
plt.xticks(rotation=45)
st.pyplot(plt)

import pandas as pd
from sklearn.cluster import KMeans
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Membaca data CSV
data1 = pd.read_csv('Case Study - Customer.csv')
data2 = pd.read_csv('Case Study - Product.csv')
data3 = pd.read_csv('Case Study - Store.csv')
data4 = pd.read_csv('Case Study - Transaction.csv')

# Data Cleansing
# Lakukan data cleansing sesuai kebutuhan
# Merubah tipe data Date menjadi datetime
data4['Date'] = pd.to_datetime(data4['Date'], format='%d/%m/%Y')

# Menggabungkan semua data
all_data = pd.concat([data1, data2, data3, data4], ignore_index=True)

# Membuat data baru untuk regression
regression_data = all_data.groupby('Date')['Qty'].sum().reset_index()

# Membuat model machine learning regression (ARIMA)
model = ARIMA(regression_data['Qty'], order=(5, 1, 0))
model_fit = model.fit()
forecast_steps = 365

# Melakukan prediksi menggunakan model ARIMA
forecast = model_fit.forecast(steps=forecast_steps)

# Visualisasi prediksi
plt.figure(figsize=(10, 6))
plt.plot(regression_data['Date'], regression_data['Qty'], label='Actual')
plt.plot(pd.date_range(start=regression_data['Date'].max(), periods=forecast_steps, freq='D'), forecast, label='Forecast', color='red')
plt.xlabel('Date')
plt.ylabel('Total Quantity')
plt.title('ARIMA Time Series Forecast')
plt.legend()
plt.show()

# Data Cleansing untuk Clustering
all_data['CustomerID'] = all_data['CustomerID'].astype(str)  # Merubah tipe data CustomerID menjadi string

# Membuat data baru untuk clustering
clustering_data = all_data.groupby('CustomerID').agg({
    'TransactionID': 'count',
    'Qty': 'sum',
    'TotalAmount': 'sum'
}).reset_index()

# Membuat model machine learning clustering (KMeans)
clustering_features = clustering_data[['TransactionID', 'Qty', 'TotalAmount']]
kmeans_model = KMeans(n_clusters=3)
kmeans_model.fit(clustering_features)

# Menambahkan label klaster ke data
clustering_data['Cluster'] = kmeans_model.labels_

# Menampilkan hasil klastering
print(clustering_data)

# Visualisasi hasil klastering
plt.scatter(clustering_data['Qty'], clustering_data['TotalAmount'], c=clustering_data['Cluster'], cmap='rainbow')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.title('Clustering Results')
plt.show()
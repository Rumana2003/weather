import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load the dataset
weather = pd.read_csv('weatherHistory.csv.zip')
weather['Formatted Date'] = pd.to_datetime(weather['Formatted Date'], utc=True)
weather.set_index('Formatted Date', inplace=True)

# 2️⃣ Plot Average Monthly Temperatures
monthly_avg = weather.resample('M')['Temperature (C)'].mean()
plt.figure(figsize=(12, 6))
plt.plot(monthly_avg.index, monthly_avg, marker='o')
plt.title('Average Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# 3️⃣ Correlation Heatmap for Key Features
features = weather[['Temperature (C)', 'Apparent Temperature (C)',
                    'Humidity', 'Wind Speed (km/h)',
                    'Visibility (km)', 'Pressure (millibars)']]
plt.figure(figsize=(10, 8))
sns.heatmap(features.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Weather Parameters')
plt.show()

# 4️⃣ Identify Hottest and Coldest Months
hottest_month = monthly_avg.idxmax()
coldest_month = monthly_avg.idxmin()
print(f"\nHottest Month: {hottest_month.strftime('%Y-%m')} "
      f"with an average temperature of {monthly_avg.max():.2f}°C.")
print(f"Coldest Month: {coldest_month.strftime('%Y-%m')} "
      f"with an average temperature of {monthly_avg.min():.2f}°C.")

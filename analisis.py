import pandas as pd
data = pd.read_csv(r'C:\data\SYNGENTA\COBA PROJECT\.vscode\data_fix.csv')
print(data)
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#pembuatan grafik rata rata produksi jagung per tahun
yield_per_year = data.groupby("tahun")["Yield(Kg/Ha)"].mean().reset_index()
print(yield_per_year)
max_yield = yield_per_year["Yield(Kg/Ha)"].max()
min_yield = yield_per_year["Yield(Kg/Ha)"].min()
max_year = yield_per_year[yield_per_year["Yield(Kg/Ha)"]== max_yield]["tahun"].values[0]
min_year = yield_per_year[yield_per_year["Yield(Kg/Ha)"]== min_yield]["tahun"].values[0]
plt.figure(figsize=(5,8))
plt.bar(yield_per_year["tahun"],yield_per_year["Yield(Kg/Ha)"],color="skyblue")
plt.title('Yield Average by Years')
plt.xlabel("Tahun",)
plt.ylabel("Yield(Kg/Ha)")
plt.xticks(yield_per_year["tahun"], rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

#menambahkan label untuk yield tertinggi dan terendah
plt.text(max_year, max_yield, f"Yield Tertinggi\n{max_yield:.2f}", 
         ha="center", va="bottom", color="green", fontsize=10, fontweight="bold")
plt.text(min_year, min_yield, f"Yield Terendah\n{min_yield:.2f}", 
         ha="center", va="top", color="red", fontsize=10, fontweight="bold")
plt.show()

#pembuatan grafik stacked bar chart rata rata produksi jagung dengan bulan tanam
df_pivot = data.pivot_table(index='tahun', columns='tanam', values='Yield(Kg/Ha)', aggfunc='avg')
desired_order = ['APR','MAY','JUN','JUL']
df_pivot = df_pivot.reindex(columns=desired_order)
df_pivot.plot(kind='bar', stacked=True, figsize=(10, 6), color=['blue', 'red', 'green', 'yellow'])
plt.title('Perkembangan Produktivitas Jagung per Tahun Berdasarkan Bulan Tanam', fontsize=14)
plt.xlabel('tahun', fontsize=12)
plt.ylabel('Yield (Kg/Ha)', fontsize=12)
plt.show()

# rata rata yield berdasarakan bulan tanam
yield_per_plant = data.groupby("tanam")["Yield(Kg/Ha)"].mean().reset_index()
print(yield_per_plant)

# rata rata yield berdasarakan bulan panen
yield_per_plant = data.groupby("panen")["Yield(Kg/Ha)"].mean().reset_index()
print(yield_per_plant)

#rata rata yield berdasarkan kota
yield_by_state = data.groupby("kota")["Yield(Kg/Ha)"].mean().reset_index()
print(yield_by_state.sort_values(by='Yield(Kg/Ha)',ascending=False))

#mencari korelasi
selected_variabel = data.drop(columns=["kota","tahun","tanam","panen"])
plt.figure(figsize=(8, 6))
sns.heatmap(selected_variabel.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap Korelasi")
plt.show()

#analisis regresi
bulan_mapping = {'APR': 1, 'MAY': 2, 'JUN': 3, 'JUL': 4, 'AUG': 5, 'SEP': 6, 'OCT': 7, 'NOV': 8}
data['tanam_angka'] = data['tanam'].map(bulan_mapping)
data['panen_angka'] = data['panen'].map(bulan_mapping)
print(data)

y = data['Yield(Kg/Ha)']
X = data[['tanam_angka','tahun','temperature','kelembaban','curah_hujan']]
X = sm.add_constant(X)
# Buat model regresi
model = sm.OLS(y, X).fit()
# Output ringkasan model
print(model.summary())

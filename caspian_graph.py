
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('data/caspian.csv', encoding='utf-8')
df = df.iloc[:, :2]
df.rename(columns={'water level': 'water_level'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
grouped = df.groupby(df['date'].dt.year)['water_level'].mean()
print(grouped)

plt.figure(figsize=(8, 15))
plt.plot(grouped.index, grouped.values, marker='o')
plt.title('Уровень воды в Каспийском море относительно уровня моря')
plt.xlabel('Год')
plt.ylabel('Уровень воды')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Завантаження даних
file_path = 'GoogleApps.csv'
data = pd.read_csv(file_path)
sns.set(style="whitegrid")

# Гістограма розподілу рейтингів
plt.figure(figsize=(10, 6))
sns.histplot(data['Rating'].dropna(), bins=30, kde=True, color='skyblue')
plt.title('Розподіл Рейтингів Додатків')
plt.xlabel('Рейтинг')
plt.ylabel('Кількість додатків')
plt.show()


# Кругова діаграма категорій додатків
plt.figure(figsize=(12, 8))
data['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Розподіл Категорій Додатків')
plt.ylabel('')
plt.show()



# Скаттер-плот залежності між кількістю відгуків та рейтингом
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Reviews', y='Rating', data=data, color='red')
plt.title('Залежність між Кількістю Відгуків та Рейтингом')
plt.xlabel('Кількість відгуків')
plt.ylabel('Рейтинг')
plt.xscale('log')
plt.show()


# Створення стовпчикової діаграми середнього рейтингу по категоріям
plt.figure(figsize=(14, 8))
category_rating_avg = data.groupby('Category')['Rating'].mean().sort_values()
sns.barplot(x=category_rating_avg.values, y=category_rating_avg.index, palette='coolwarm')
plt.title('Середній Рейтинг по Категоріям')
plt.xlabel('Середній Рейтинг')
plt.ylabel('Категорія')
plt.show()



# Гістограма кількості інсталяцій по категоріях
plt.figure(figsize=(14, 8))
installs_per_category = data.groupby('Category')['Installs'].sum().sort_values()
sns.barplot(x=installs_per_category.values, y=installs_per_category.index, palette='viridis')
plt.title('Кількість Інсталяцій по Категоріях')
plt.xlabel('Загальна Кількість Інсталяцій')
plt.ylabel('Категорія')
plt.xscale('log')
plt.show()


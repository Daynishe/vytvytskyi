import pandas as pd

# Завантаження даних
file_path = 'GoogleApps.csv'
data = pd.read_csv(file_path)

# Визначення назви програми, яка розташована першою у наборі даних
first_app_name = data.iloc[0]['App']

# Визначення категорії додатку, який розташований останнім у наборі даних
last_app_category = data.iloc[-1]['Category']

# Визначення кількості стовпців у наборі даних
num_columns = data.shape[1]

# Обрахунок середнього арифметичного та медіани розміру додатків
average_size = data['Size'].mean()
median_size = data['Size'].median()

# Визначення категорії додатку з найбільшою кількістю відгуків
category_most_reviews = data.loc[data['Reviews'].idxmax()]['Category']

# Обрахунок середнього рейтингу додатків вартістю понад 20 доларів із кількістю установок більше 10000
average_rating_expensive_apps = data[(data['Price'] > 20) & (data['Installs'] > 10000)]['Rating'].mean()

# Виведення результатів
print(f"Назва програми, що розташована першою у наборі даних: {first_app_name}")
print(f"Категорія додатку, що розташований останнім у наборі даних: {last_app_category}")
print(f"Кількість стовпців у наборі даних: {num_columns}")
print(f"Середнє арифметичне розміру додатків: {average_size:.2f} MB")
print(f"Медіана розміру додатків: {median_size} MB")
print(f"Категорія додатку з найбільшою кількістю відгуків: {category_most_reviews}")
print(f"Середній рейтинг додатків вартістю понад $20 із кількістю установок більше 10000: {average_rating_expensive_apps:.2f}")

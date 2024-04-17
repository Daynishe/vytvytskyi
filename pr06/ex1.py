import json
import sqlite3
from bs4 import BeautifulSoup as bs
import requests as rq

# URL to scrape
url = 'https://rozetka.com.ua/ua/apple-iphone-15-pro-128gb-natural-titanium/p395460909/'

# Send HTTP request
response = rq.get(url)
soup = bs(response.content, 'html.parser')

# Parse the necessary fields
name = soup.find(class_="product__title-left product__title-collapsed ng-star-inserted").text.strip()
old_price = soup.find(class_="product-price__small ng-star-inserted").text.strip()
new_price = soup.find(class_="product-price__big product-price__big-color-red").text.strip()
product_about = soup.find(class_="product-about__brief ng-star-inserted").text.strip()

# Print the data (optional)
print(f"""
Name: {name}
Old price: {old_price} UAH
Price with discount: {new_price} UAH
About: {product_about}
""")

# Save to SQLite
# Connect to SQLite database
conn = sqlite3.connect('product_data.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS products
             (name TEXT, old_price TEXT, new_price TEXT, about TEXT)''')

# Insert a row of data
c.execute("INSERT INTO products (name, old_price, new_price, about) VALUES (?, ?, ?, ?)",
          (name, old_price, new_price, product_about))

# Save (commit) the changes and close the connection
conn.commit()
conn.close()

# Save to JSON
data = {
    "Name": name,
    "Old price": old_price,
    "Price with discount": new_price,
    "About": product_about
}

# Writing to json file
with open(f'{("").join(name.split(" ")[0:5])} .json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

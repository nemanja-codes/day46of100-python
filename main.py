from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")

top100 = [song.getText().strip() for song in soup.find_all(name="h3", class_="a-no-trucate")]
print(top100)


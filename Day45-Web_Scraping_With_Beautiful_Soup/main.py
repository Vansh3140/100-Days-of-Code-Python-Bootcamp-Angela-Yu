from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movies_list = soup.find_all(name="h3")

movie_titles = [x.get_text() for x in movies_list]

movie_titles.reverse()

print(movie_titles)

with open("movie_titles.txt", "w", encoding="utf-8") as file:
    for x in movie_titles:
        file.write(x + "\n")

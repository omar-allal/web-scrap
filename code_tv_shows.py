from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250').text
soup = BeautifulSoup(html_text, 'lxml')
tvshows = soup.find('tbody', class_ = "lister-list").find_all('tr')

file = open("top_rated_tvshows_imdb.csv", "w", newline='')
writer = csv.writer(file)

writer.writerow(["name", "rank", "release_year", "rating"])

for tvshow in tvshows:
    name = tvshow.find('td', class_ = "titleColumn").a.text
    rank = tvshow.find('td', class_ = "titleColumn").get_text(strip=True).split('.')[0]
    release_year = tvshow.find('td', class_ = "titleColumn").span.text.strip('()')
    rating = tvshow.find('td', class_ = "ratingColumn imdbRating").strong.text
    print(name, rank, release_year, rating)
    writer.writerow([name, rank, release_year, rating])

file.close()
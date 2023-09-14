from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find('tbody', class_ = "lister-list").find_all('tr')

file = open("top_rated_movies_imdb.csv", "w", newline='')
writer = csv.writer(file)

writer.writerow(["movie_name", "rank", "release_year", "rating"])

for movie in movies:
    movie_name = movie.find('td', class_ = "titleColumn").a.text
    movie_rank = movie.find('td', class_ = "titleColumn").get_text(strip=True).split('.')[0]
    release_year = movie.find('td', class_ = "titleColumn").span.text.strip('()')
    movie_rating = movie.find('td', class_ = "ratingColumn imdbRating").strong.text
    print(movie_name, movie_rank, release_year, movie_rating)
    writer.writerow([movie_name, movie_rank, release_year, movie_rating])

file.close()


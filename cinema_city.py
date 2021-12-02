from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CINEMA_CITY_BASE_URL = "https://www.cinema-city.pl"

CINEMAS_ID = {"WARSZAWA - ARKADIA": "1074", "WARSZAWA - BEMOWO": "1061",
              "WARSZAWA - BIAŁOŁĘKA GALERIA PÓŁNOCNA": "1096", "WARSZAWA - GALERIA MOKOTÓW": "1070",
              "WARSZAWA - JANKI": "1069", "WARSZAWA - PROMENADA": "1068", "WARSZAWA - SADYBA": "1060"}

DRIVER_PATH = 'assets/chromedriver'


#
# def get_cinema_city_repertoire(cinema_name, date):
#     cinema_id = CINEMAS_ID.get(cinema_name)
#
#     cinema_url = CINEMA_CITY_BASE_URL + "/#/buy-tickets-by-cinema?in-cinema=" + cinema_id + "&at=" + date + "&view-mode=list"
#     movies_list = []
#
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#
#     browser = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
#     browser.get(cinema_url)
#     time.sleep(1)
#     res = browser.page_source
#     browser.close()
#
#     soup = BeautifulSoup(res, "html.parser")
#
#     movie_divs = soup.findAll(
#         "div", {"class": "qb-movie-details col-sm-9 col-md-10 pull-right"})
#
#     for movie in movie_divs:
#         all_shows = movie.find_all('a')
#         movie = {}
#         movie_dates = []
#         movie_title = ""
#         for i in range(len(all_shows)):
#             if i == 0:
#                 movie_title = all_shows[i].text
#                 print("TITLE: " + movie_title)
#             else:
#                 movie_date = all_shows[i].text.replace(" ", "")
#                 movie_dates.append(movie_date)
#                 print(movie_date)
#
#         movie[movie_title] = movie_dates
#         movies_list.append(movie)
#
#     print(movies_list)
#

def get_cinema_city_movie(cinema_name, date, movie_title):
    cinema_id = CINEMAS_ID.get(cinema_name.upper())
    cinema_url = CINEMA_CITY_BASE_URL + "/#/buy-tickets-by-cinema?in-cinema=" + cinema_id + "&at=" + date + "&view-mode=list"

    movies = {"name": cinema_name.upper()}

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
    browser.get(cinema_url)
    res = browser.page_source
    browser.close()

    soup = BeautifulSoup(res, "html.parser")

    movie_divs = soup.findAll(
        "div", {"class": "qb-movie-details col-sm-9 col-md-10 pull-right"})

    for movie in movie_divs:
        all_shows = movie.find_all('a')
        movie = {}
        movie_dates = []
        scrapped_movie_title = ""
        for i in range(len(all_shows)):
            if i == 0:
                scrapped_movie_title = all_shows[i].text
            else:
                if movie_title.upper() == scrapped_movie_title.upper():
                    movie_date = all_shows[i].text.replace(" ", "")
                    movie_dates.append(movie_date)
        if movie_title.upper() == scrapped_movie_title.upper():
            movie[movie_title] = movie_dates
            movies["seanse"] = movie_dates

    return movies


# def scrap_all_cinemas(date):
#     for cinema_name in CINEMAS_ID.keys():
#         print(cinema_name.upper())
#         get_cinema_city_repertoire(cinema_name, date)
#

def get_movie_times(cinemas_names_list, date, title_movie):
    cinema_movies = []
    for cinema_name in cinemas_names_list:
        cinema_movies.append(get_cinema_city_movie(cinema_name, date, title_movie))
    return cinema_movies
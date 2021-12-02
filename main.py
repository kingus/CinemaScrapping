import cinema_city

date = "2021-12-02"
title_movie = "Dom Gucci"
cinemas_response = cinema_city.get_movie_times(["warszawa - Arkadia", "Warszawa - bemowo"], date, title_movie)
print(cinemas_response)

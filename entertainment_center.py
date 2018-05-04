import media
import fresh_tomatoes

# Create instances of class Movie
milky_way = media.Movie("Milky Way", "Breastfeeding documentary",
                        "https://ia.media-imdb.com/images/M/MV5BMjExNzg4NzA5MF5BMl5BanBnXkFtZTgwNjgyMzI2NTE@._V1_UY268_CR9,0,182,268_AL_.jpg", # noqa
                        "https://www.youtube.com/watch?v=8wWE-ZHu1i8")

born = media.Movie("The Business of Being Born", "Birth Documentary",
                   "https://ia.media-imdb.com/images/M/MV5BMTA5MzQ1MDcxODZeQTJeQWpwZ15BbWU4MDU3MjQzNjEy._V1_SY1000_CR0,0,675,1000_AL_.jpg", # noqa
                   "https://www.youtube.com/watch?v=l2zgzwP7mwM")

fellowship = media.Movie("The Fellowship of the Ring",
                         "First movie in the Lord of the Rings trilogy",
                         "https://images-na.ssl-images-amazon.com/images/I/51Qvs9i5a%2BL.jpg",
                         "https://www.youtube.com/watch?v=V75dMMIW2B4")

journey = media.Movie("The Hobbit: An Unexpected Journey",
                      "The first movie in The Hobbit series.",
                      "https://images-na.ssl-images-amazon.com/images/I/71mOQV8-GzL._SY550_.jpg",
                      "https://www.youtube.com/watch?v=SDnYMbYB-nU")

des_smaug = media.Movie("The Hobbit: The Desolation of Smaug",
                        "The second movie in The Hobbit series",
                        "https://images-na.ssl-images-amazon.com/images/I/7145Wo9GjlL._SY550_.jpg",
                        "https://www.youtube.com/watch?v=OPVWy1tFXuc")

armies = media.Movie("The Hobbit: The Battle of the Five Armies",
                     "The Last Movie in The Hobbit series",
                     "http://www.impawards.com/2014/posters/hobbit_the_battle_of_the_five_armies_ver21.jpg", # noqa
                     "https://www.youtube.com/watch?v=iVAgTiBrrDA")
                    
# Create a list of instance of class Movie
movies = [milky_way, born, fellowship, journey, des_smaug, armies]

# Use fresh_tomatoes to display movie images and names, and play the movie trailer when clicked
fresh_tomatoes.open_movies_page(movies)


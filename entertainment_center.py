import fresh_tomatoes
import media

# In this file will be place each movie displayed on main screen:
#
#
#    1.Attributes:

#    a) Title;
#    b) A little information about the movie (using IMDb as information);
#    c) URL where is host the movie poster;
#    d) URL of youtube trailer ;
#
#    2. Vector
#
#    In the final we create a vector named ''movie =[]'', here are insert each
#    movie who will be displayed on main screen.

# The main code of the Movies and the attributes

matrix = media.Movie(
                    "Matrix",
                    "A hacker learns from mysterious rebels"
                    " about the true nature of his reality and his role"
                    " in the war against its controllers.",
                    "https://upload.wikimedia.org/wikipedia/pt/c/c1/"
                    "The_Matrix_Poster.jpg",
                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

back_to_the_future = media.Movie(
                                "Back to the Future",
                                "Marty McFly, a 17-year-old high school"
                                " student, is accidentally sent thirty years"
                                " into the past in a time-traveling DeLorean"
                                " invented by his close friend, the maverick"
                                " scientist Doc Brown.",
                                "https://upload.wikimedia.org/wikipedia/pt/9/"
                                "97/BackFuturePoster.jpg",
                                "https://www.youtube.com/watch?v=qvsgGtivCgs")

rocky4 = media.Movie(
                    "Rocky IV",
                    "Rocky Balboa proudly holds the world heavyweight boxing"
                    " championship, but a new challenger has stepped forward:"
                    " Drago, a six-foot-four, 261-pound fighter who has the"
                    " backing of the Soviet Union. "
                    "killed by Ivan Drago he return to fight his new enemy",
                    "https://upload.wikimedia.org/wikipedia/pt/9/95/"
                    "Rocky_IV.jpg",
                    "https://www.youtube.com/watch?v=S5GGQK4n-YA")

tropa_de_elite = media.Movie("Tropa de Elite",
                             "1997, Captain Nascimento has to find a"
                             " substitute for his occupation while trying"
                             " to take down drug dealers and criminals"
                             " before the Pope comes to Rio de Janeiro,"
                             " Brazil.",
                             "https://mir-s3-cdn-cf.behance.net/project_"
                             "modules/disp/3b327617071869.562b543ac6203.jpg",
                             "https://www.youtube.com/watch?v=P_9GgCnDi7g")

indiana_jones = media.Movie("Indiana Jones",
                            "In 1936, archaeologist and adventurer Indiana"
                            " Jones is hired by the U.S. government to find"
                            " the Ark of the Covenant before Adolf Hitler's"
                            " Nazis can obtain its awesome powers.",
                            "https://upload.wikimedia.org/wikipedia/pt/4/4b/"
                            "Raiders.jpg",
                            "https://www.youtube.com/watch?v=XkkzKHCx154")

rambo = media.Movie("Rambo",
                    "Former Green Beret John Rambo is pursued into the"
                    " mountains surrounding a small town by a tyrannical"
                    " sheriff and his deputies, forcing him to survive"
                    " using his combat skills. ",
                    "https://upload.wikimedia.org/wikipedia/en/d/d6/"
                    "First_blood_poster.jpg",
                    "https://www.youtube.com/watch?v=IAqLKlxY3Eo")

quiet_place = media.Movie("Quiet Place",
                          "In a post-apocalyptic world, a family is forced"
                          " to live in silence while hiding from monsters"
                          " with ultra-sensitive hearing. ",
                          "https://upload.wikimedia.org/wikipedia/pt/7/7e/"
                          "A_Quiet_Place.png",
                          "https://www.youtube.com/watch?v=p9wE8dyzEJE")

cassino_royale = media.Movie("007 - Cassino Royale",
                             "Armed with a license to kill, Secret Agent"
                             " James Bond sets out on his first mission as"
                             " 007, and must defeat a private banker to"
                             "terrorists in a high stakes game of poker at"
                             "Casino Royale, Montenegro, but things are not"
                             "what they seem. ",
                             "https://upload.wikimedia.org/wikipedia/pt/3/3d/"
                             "Casino_Royale.jpg",
                             "https://www.youtube.com/watch?v=36mnx8dBbGE")

the_hunt_for_red_october = media.Movie("The Hunt for Red October",
                                       " In November 1984, the URSS best"
                                       " submarine captain in their newest"
                                       " sub violates orders and heads for"
                                       "the U.S. Is he trying to defect or"
                                       "to start a war?",
                                       "https://upload.wikimedia.org/"
                                       "wikipedia/en/3/36/The_Hunt_for_Red"
                                       "_October_movie_poster.png",
                                       "https://www.youtube.com/watch?v="
                                       "3C2tE7vjdHk")

# Vector to place the movies
movie = [
        matrix, back_to_the_future, rocky4, tropa_de_elite, indiana_jones,
        rambo, quiet_place, cassino_royale, the_hunt_for_red_october]

fresh_tomatoes.open_movies_page(movie)

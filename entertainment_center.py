import fresh_tomatoes
import media

#In this file will be place each movie displayed on main screen:
#
#
#    1.Attributes:

#    a) Title;
#    b) A little information about the movie;
#    c) URL where is host the movie poster;
#    d) URL of youtube trailer ;
#
#    2. Vector
#
#    In the final we create a vector named ''movie =[]'', here are insert each movie who will be displayed on main screen.
#        
# 

#The main code of the Movies and the attributes

matrix = media.Movie("Matrix",
                     "The greatest movie ever",
                     "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

back_to_the_future = media.Movie("Back to the Future",
                                 "Marty McFly traveling around the years",
                                 "https://upload.wikimedia.org/wikipedia/pt/9/97/BackFuturePoster.jpg",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

rocky4 = media.Movie("Rocky IV",
                     "Rocky was retire, but after watching his friend get killed by Ivan Drago he return to fight his new enemy",
                     "https://upload.wikimedia.org/wikipedia/pt/9/95/Rocky_IV.jpg",
                     "https://www.youtube.com/watch?v=S5GGQK4n-YA")


tropa_de_elite = media.Movie("Tropa de Elite",
                             "Captain Nascimento against the Crime",
                             "https://mir-s3-cdn-cf.behance.net/project_modules/disp/3b327617071869.562b543ac6203.jpg",
                             "https://www.youtube.com/watch?v=P_9GgCnDi7g")

indiana_jones = media.Movie("Indiana Jones",
                            "Indiana Jones: The new hero",
                            "https://upload.wikimedia.org/wikipedia/pt/4/4b/Raiders.jpg",
                            "https://www.youtube.com/watch?v=XkkzKHCx154")

rambo = media.Movie("Rambo",
                    "Stalone become Rambo",
                    "https://upload.wikimedia.org/wikipedia/en/d/d6/First_blood_poster.jpg",
                    "https://www.youtube.com/watch?v=IAqLKlxY3Eo")

quiet_place = media.Movie("Quiet Place",
                          "If you talk you die!!!",
                          "https://upload.wikimedia.org/wikipedia/pt/7/7e/A_Quiet_Place.png",
                          "https://www.youtube.com/watch?v=p9wE8dyzEJE")

cassino_royale = media.Movie("007 - Cassino Royale",
                             "James Bond is back",
                             "https://upload.wikimedia.org/wikipedia/pt/3/3d/Casino_Royale.jpg",
                             "https://www.youtube.com/watch?v=36mnx8dBbGE")

the_hunt_of_the_red_october = media.Movie("The Hunt of the Red October",
                                          "Jack Ryan need to solve the problem befere a nuclear attack become real",
                                          "https://upload.wikimedia.org/wikipedia/en/3/36/The_Hunt_for_Red_October_movie_poster.png",
                                          "https://www.youtube.com/watch?v=3C2tE7vjdHk")


#Vector to place the movies 
movie = [matrix, back_to_the_future, rocky4, tropa_de_elite, indiana_jones, rambo, quiet_place, cassino_royale, the_hunt_of_the_red_october]
fresh_tomatoes.open_movies_page(movie)



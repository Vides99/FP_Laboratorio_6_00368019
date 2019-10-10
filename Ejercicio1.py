movie1 = int(input("introduce el precio de la primera pelicula"))
movie2 = int(input("introduce el precio de la segunda pelicula"))
movie3 = int(input("introduce el precio de la tercera pelicula"))
sumaMovie = 0

if movie1 > movie2:
    if movie1 > movie3:
        sumaMovie = movie2 + movie3
        print("hay una promocion, que al llevar 3 peliculas pagas las 2 mas baratas! tu cuenta es de ", sumaMovie)
    else:
        sumaMovie = movie2 + movie1
        print("hay una promocion, que al llevar 3 peliculas pagas las 2 mas baratas! tu cuenta es de ", sumaMovie)
else:
    if movie2 > movie3:
        sumaMovie = movie1 + movie3
        print("hay una promocion, que al llevar 3 peliculas pagas las 2 mas baratas! tu cuenta es de ", sumaMovie)
    else:
        sumaMovie = movie1 + movie2
        print("hay una promocion, que al llevar 3 peliculas pagas las 2 mas baratas! tu cuenta es de ", sumaMovie)
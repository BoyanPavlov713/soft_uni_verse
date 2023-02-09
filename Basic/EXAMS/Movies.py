min_number = 1000000000
max_number = -1000000000
average_rating = 0
total = 0
best_movie = ''
worst_movie = ''
number_movies = int(input())
rating = 0
movie_name = ''
for name in range(1, number_movies + 1):
    movie_name = input()
    rating = float(input())

    if rating > max_number:
        max_number = rating
        best_movie = movie_name
    if rating < min_number:
        min_number = rating
        worst_movie = movie_name

    total += rating
    average_rating = total / number_movies


print(f"{best_movie} is with highest rating: {max_number:.1f}")
print(f"{worst_movie} is with lowest rating: {min_number:.1f}")
print(f"Average rating: {average_rating:.1f}")

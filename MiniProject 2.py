movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# take extra movies from user
more = int(input("How many movies do you want to add? "))
for _ in range(more):  # loop for extra movies
    name = input("Enter movie name: ")
    budget = int(input("Enter budget: "))
    movies.append((name, budget))

# find average budget
total_budget = sum(b for _, b in movies)
average = total_budget / len(movies)
print(f"\nAverage budget: {average:.2f}\n")

count = 0
for n, b in movies:  # loop to check above average
    if b > average:
        print(f"{n} exceeded the average by {b - average}")
        count += 1

# total count
print(f"\nTotal movies above average: {count}")

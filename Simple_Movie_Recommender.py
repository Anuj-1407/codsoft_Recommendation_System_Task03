# Simple Movie Recommendation System
movies = {

    "Action": [
        {"name": "Avengers", "rating": 8.5},
        {"name": "John Wick", "rating": 8.0},
        {"name": "Batman", "rating": 8.3},
        {"name": "War", "rating": 7.5},
        {"name": "Pathaan", "rating": 7.2}
    ],

    "Comedy": [
        {"name": "Mr. Bean", "rating": 7.8},
        {"name": "The Mask", "rating": 8.1},
        {"name": "Jumanji", "rating": 7.5},
        {"name": "Hera Pheri", "rating": 8.5},
        {"name": "Bhool Bhulaiyaa", "rating": 7.4}
    ],

    "Sci-Fi": [
        {"name": "Interstellar", "rating": 8.9},
        {"name": "Inception", "rating": 8.8},
        {"name": "The Matrix", "rating": 8.7},
        {"name": "Koi Mil Gaya", "rating": 7.1}
    ],

    "Horror": [
        {"name": "Conjuring", "rating": 7.9},
        {"name": "Annabelle", "rating": 7.0},
        {"name": "Insidious", "rating": 7.6},
        {"name": "Stree", "rating": 7.5},
        {"name": "Tumbbad", "rating": 8.2}
    ],

    "Drama": [
        {"name": "3 Idiots", "rating": 8.4},
        {"name": "Dangal", "rating": 8.3},
        {"name": "Taare Zameen Par", "rating": 8.4},
        {"name": "The Pursuit of Happyness", "rating": 8.0}
    ]
}

watchlist = []

print("=" * 60)
print("        🎬 MOVIE RECOMMENDATION SYSTEM 🎬")
print("=" * 60)

user_name = input("Enter your name: ")

print(f"\nWelcome {user_name}!")

while True:

    print("\nAvailable Genres:\n")

    for genre in movies:
        print("➡", genre)

    choice = input("\nEnter your favorite genre: ").title()

    if choice in movies:

        print(f"\n🔥 Top {choice} Movies For You:\n")

        for index, movie in enumerate(movies[choice], start=1):
            print(f"{index}. {movie['name']} ⭐ {movie['rating']}")

        print("\n1. Add movie to watchlist")
        print("2. View watchlist")
        print("3. Continue")

        option = input("\nChoose an option (1/2/3): ")

        if option == "1":

            movie_no = int(input("Enter movie number: "))

            if 1 <= movie_no <= len(movies[choice]):

                selected_movie = movies[choice][movie_no - 1]["name"]

                if selected_movie not in watchlist:
                    watchlist.append(selected_movie)
                    print(f"\n✅ '{selected_movie}' added to watchlist!")
                else:
                    print("\n⚠ Movie already in watchlist!")

            else:
                print("\n❌ Invalid movie number!")

        elif option == "2":

            print("\n🎥 Your Watchlist:")

            if len(watchlist) == 0:
                print("Watchlist is empty!")

            else:
                for movie in watchlist:
                    print("•", movie)

    else:
        print("\n❌ Genre not found!")

    again = input("\nDo you want more recommendations? (yes/no): ").lower()

    if again != "yes":
        break

print("\n🎉 Thank you for using Movie Recommendation System!")
print("Enjoy your movies 🍿")
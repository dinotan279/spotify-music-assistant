#Dino
import json
import os

SONGS_FILE = "data/songs.json"
RECOMMENDATIONS_FILE = "data/recommendations.json"


# =========================
# SONG / PLAYLIST FUNCTIONS
# =========================

def load_songs():
    if not os.path.exists(SONGS_FILE):
        return []

    with open(SONGS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_songs(songs):
    with open(SONGS_FILE, "w", encoding="utf-8") as file:
        json.dump(songs, file, indent=4)

# Dino - Add Song

def add_song(songs):
    print("\n--- Add Song ---")

    title = input("Enter song title: ")
    artist = input("Enter artist: ")
    genre = input("Enter genre: ")
    year = input("Enter release year: ")

    song = {
        "title": title,
        "artist": artist,
        "genre": genre,
        "year": year
    }

    songs.append(song)
    save_songs(songs)

    print("\nSong added successfully!")


# Aloysius - VIEW PLAYLIST

def view_playlist(songs):
    print("\n--- My Playlist ---")

    if not songs:
        print("Your playlist is empty.")
        return

    for number, song in enumerate(songs, 1):
        print(f"\n{number}. {song['title']}")
        print(f"   Artist: {song['artist']}")
        print(f"   Genre: {song['genre']}")
        print(f"   Year: {song['year']}")

# Aloysius - SEARCH SONG

def search_song(songs):
    print("\n--- Search Song ---")

    keyword = input("Enter song title or artist: ").lower()

    found = False

    for song in songs:
        if (keyword in song["title"].lower()
                or keyword in song["artist"].lower()):

            print("\nSong Found!")
            print(f"Title: {song['title']}")
            print(f"Artist: {song['artist']}")
            print(f"Genre: {song['genre']}")
            print(f"Year: {song['year']}")

            found = True

    if not found:
        print("\nSong not found.")


# WEI HONG - RECOMMENDATION

def music_recommendation():

    print("\n================================")
    print("     MUSIC RECOMMENDATION")
    print("================================")

    # Load recommendation JSON
    if not os.path.exists(RECOMMENDATIONS_FILE):
        print("\nRecommendation file not found.")
        return

    with open(RECOMMENDATIONS_FILE, "r", encoding="utf-8") as file:
        recommendations = json.load(file)

    # Mood selection
    print("\nChoose your mood:")
    print("1. Happy")
    print("2. Relaxed")
    print("3. Sad")
    print("4. Energetic")

    mood_choice = int(input("\nEnter your choice: "))

    moods = {
        1: "Happy",
        2: "Relaxed",
        3: "Sad",
        4: "Energetic"
    }

    mood = moods.get(mood_choice)

    if mood is None:
        print("\nInvalid mood choice.")
        return

    # Genre selection
    print("\nChoose your genre:")
    print("1. Pop")
    print("2. K-Pop")
    print("3. R&B")
    print("4. Rock")

    genre_choice = int(input("\nEnter your choice: "))

    genres = {
        1: "Pop",
        2: "K-Pop",
        3: "R&B",
        4: "Rock"
    }

    genre = genres.get(genre_choice)

    if genre is None:
        print("\nInvalid genre choice.")
        return

    # Get recommended songs from JSON
    recommended_songs = recommendations.get(mood, {}).get(genre, [])

    # Display recommendation
    print("\n--------------------------------")
    print("Recommended for you:")
    print("Genre:", genre)
    print("Mood:", mood)

    print("\nRecommended Songs:")

    if not recommended_songs:
        print("No recommendations found.")
    else:
        for i, song in enumerate(recommended_songs[:5], 1):
            print(f"{i}. {song}")

    print("--------------------------------")


# =========================
# MAIN MENU
# =========================

def main_menu():
    print("\n================================")
    print("       SPOTIFY MUSIC ASSISTANT")
    print("================================")
    print("1. Add Song")
    print("2. View My Playlist")
    print("3. Search Song")
    print("4. Remove Song")
    print("5. Get Music Recommendation")
    print("6. Exit")
    print("================================")


# =========================
# MAIN PROGRAM
# =========================

songs = load_songs()

while True:

    main_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_song(songs)

    elif choice == "2":
        view_playlist(songs)

    elif choice == "3":
        search_song(songs)

    elif choice == "4":
        print("\nRemove Song - Coming Soon")

    elif choice == "5":
        music_recommendation()

    elif choice == "6":
        print("\nThank you for using Spotify Music Assistant!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")

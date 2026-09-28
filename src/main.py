import json
import os

DATA_FILE = "data/songs.json"

def load_songs():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_songs(songs):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(songs, file, indent=4)


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
# =========================
# Aloysius - VIEW PLAYLIST
# =========================

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


# =========================
# Aloysius - SEARCH SONG
# =========================

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



songs = load_songs()


while True:
    main_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_song(songs)

    elif choice == "2":
        print("\nView My Playlist - Coming Soon")

    elif choice == "3":
        print("\nSearch Song - Coming Soon")

    elif choice == "4":
        print("\nRemove Song - Coming Soon")

    elif choice == "5":
        print("\nMusic Recommendation - Coming Soon")

    elif choice == "6":
        print("\nThank you for using Spotify Music Assistant!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")

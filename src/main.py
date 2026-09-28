# ----------------------------
# Dino 
# ----------------------------

import json
import os

DATA_FILE = "data/songs.json"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_songs():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_songs(songs):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(songs, file, indent=4)

# --------------------------------
# Dino - Add Song
# --------------------------------

def add_song(songs):
    clear_screen()

    print("========================================")
    print("               ADD SONG")
    print("========================================")
    print("\nPress Enter without typing to cancel.\n")

    title = input("Enter song title: ").strip()


    if title == "":
        print("\nAdd Song cancelled.")
        input("Press Enter to return to the main menu...")
        return

    artist = input("Enter artist: ").strip()

    if artist == "":
        print("\nAdd Song cancelled.")
        input("Press Enter to return to the main menu...")
        return

    genre = input("Enter genre: ").strip()

    if genre == "":
        print("\nAdd Song cancelled.")
        input("Press Enter to return to the main menu...")
        return

    year = input("Enter release year: ").strip()

    if year == "":
        print("\nAdd Song cancelled.")
        input("Press Enter to return to the main menu...")
        return

    song = {
        "title": title,
        "artist": artist,
        "genre": genre,
        "year": year
    }

    songs.append(song)
    save_songs(songs)

    print("\n✓ Song added successfully!")

    input("\nPress Enter to return to the main menu...")

# =========================
# Aloysius - VIEW PLAYLIST
# =========================

def view_playlist(songs): 
    clear_screen()

    print("========================================")
    print("             MY PLAYLIST")
    print("========================================")

    if not songs:
        print("Your playlist is empty.")
        input("\nPress Enter to return to the main menu...")
        return

    for number, song in enumerate(songs, 1):
        print(f"\n{number}. {song['title']}")
        print(f"   Artist: {song['artist']}")
        print(f"   Genre: {song['genre']}")
        print(f"   Year: {song['year']}")

    input("\nPress Enter to return to the main menu...")
    

# =========================
# Aloysius - SEARCH SONG
# =========================

def search_song(songs):
    clear_screen()

    print("========================================")
    print("              SEARCH SONG")
    print("========================================")

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

    input("\nPress Enter to return to the main menu...")

def main_menu(songs):
    clear_screen()


    print("\n========================================")
    print("          SPOTIFY MUSIC ASSISTANT")
    print("========================================")
    print(f"\n  Songs in your playlist: {len(songs)}\n")

    print("  YOUR LIBRARY")
    print("  ----------------------------")
    print("  1. Add Song")
    print("  2. View My Playlist")
    print("  3. Search Song")
    print("  4. Remove Song")

    print("\n  DISCOVER")
    print("  ----------------------------")
    print("  5. Get Music Recommendation")

    print("\n  0. Exit")
    print("\n========================================")



songs = load_songs()


while True:
    main_menu(songs)

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_song(songs)

    elif choice == "2":
        view_playlist(songs)

    elif choice == "3":
        search_song(songs)

    elif choice == "4":
        print("\nRemove Song - Coming Soon")

    elif choice == "5":
        print("\nMusic Recommendation - Coming Soon")

    elif choice == "0":
        print("\nThank you for using Spotify Music Assistant!")
        break

    else:
        print("\nInvalid choice.")
        print("Please enter a number from 0 to 5.")
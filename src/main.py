# ----------------------------
# Dino
# ----------------------------

import json
import os

from recommendation import get_music_recommendation

SONGS_FILE = "data/songs.json"
RECOMMENDATIONS_FILE = "data/recommendations.json"


# =========================
# SONG / PLAYLIST FUNCTIONS
# =========================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_songs():
    if not os.path.exists(SONGS_FILE):
        return []

    with open(SONGS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_songs(songs):
    with open(SONGS_FILE, "w", encoding="utf-8") as file:
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

# =========================
# Ethan Lim - REMOVE SONG
# =========================

def remove_song(songs):
    clear_screen()

    print("========================================")
    print("              REMOVE SONG")
    print("========================================")

    if not songs:
        print("\nYour playlist is empty.")
        input("\nPress Enter to return to the main menu...")
        return

    print("\nSongs in your playlist:")

    for number, song in enumerate(songs, 1):
        print(f"{number}. {song['title']} - {song['artist']}")

    print("\nPress Enter without typing to cancel.")

    title = input("\nEnter song title to remove: ").strip()

    # Input validation
    if title == "":
        print("\nRemove Song cancelled.")
        input("Press Enter to return to the main menu...")
        return

    for song in songs:
        if song["title"].lower() == title.lower():
            songs.remove(song)
            save_songs(songs)

            print(f"\n✓ '{song['title']}' removed successfully!")
            input("\nPress Enter to return to the main menu...")
            return

    print("\nSong not found in your playlist.")
    input("Press Enter to return to the main menu...")



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
        remove_song(songs)

    elif choice == "5":
        get_music_recommendation(songs, save_songs)

    elif choice == "0":
        print("\nThank you for using Spotify Music Assistant!")
        break

    else:
        print("\nInvalid choice.")
        print("Please enter a number from 0 to 5.")
        input("\nPress Enter to continue...")

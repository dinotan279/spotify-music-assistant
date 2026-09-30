# ----------------------------
# Dino
# ----------------------------

import json
import os

from addsong import add_song
from playlist import view_playlist
from recommendation import get_music_recommendation
from remove import remove_song
from search import search_song

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
        remove_song(songs,save_songs)

    elif choice == "5":
        get_music_recommendation(songs, save_songs)

    elif choice == "0":
        print("\nThank you for using Spotify Music Assistant!")
        break

    else:
        print("\nInvalid choice.")
        print("Please enter a number from 0 to 5.")
        input("\nPress Enter to continue...")

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

# Wei Hong recommendation system
print("================================")
print("     MUSIC RECOMMENDATION")
print("================================")

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

# Song recommendations
songs = {

    # Happy
    (1, 1): [
        "Espresso - Sabrina Carpenter",
        "Levitating - Dua Lipa",
        "Shake It Off - Taylor Swift",
        "Good Time - Owl City & Carly Rae Jepsen",
        "Flowers - Miley Cyrus"
    ],

    (1, 2): [
        "Super Shy - NewJeans",
        "Dynamite - BTS",
        "Cupid - FIFTY FIFTY",
        "After LIKE - IVE",
        "Queencard - (G)I-DLE"
    ],

    (1, 3): [
        "Leave The Door Open - Silk Sonic",
        "Treasure - Bruno Mars",
        "Kiss Me More - Doja Cat ft. SZA",
        "Sunday Morning - Maroon 5",
        "Best Part - Daniel Caesar ft. H.E.R."
    ],

    (1, 4): [
        "Shut Up and Dance - WALK THE MOON",
        "Don't Stop Me Now - Queen",
        "Mr. Brightside - The Killers",
        "Sugar, We're Goin Down - Fall Out Boy",
        "Adventure of a Lifetime - Coldplay"
    ],

    # Relaxed
    (2, 1): [
        "golden hour - JVKE",
        "Until I Found You - Stephen Sanchez",
        "Perfect - Ed Sheeran",
        "Ocean Eyes - Billie Eilish",
        "Photograph - Ed Sheeran"
    ],

    (2, 2): [
        "Ditto - NewJeans",
        "Love Scenario - iKON",
        "Through the Night - IU",
        "Instagram - DEAN",
        "Fairy of Shampoo - TOMORROW X TOGETHER"
    ],

    (2, 3): [
        "Best Part - Daniel Caesar ft. H.E.R.",
        "Get You - Daniel Caesar ft. Kali Uchis",
        "Snooze - SZA",
        "Location - Khalid",
        "Adore You - Harry Styles"
    ],

    (2, 4): [
        "Yellow - Coldplay",
        "Sparks - Coldplay",
        "The Scientist - Coldplay",
        "Drive - Incubus",
        "505 - Arctic Monkeys"
    ],

    # Sad
    (3, 1): [
        "drivers license - Olivia Rodrigo",
        "Someone Like You - Adele",
        "traitor - Olivia Rodrigo",
        "When I Was Your Man - Bruno Mars",
        "Happier - Ed Sheeran"
    ],

    (3, 2): [
        "Holo - LeeHi",
        "Lonely - 2NE1",
        "Eight - IU ft. SUGA",
        "Gone - ROSÉ",
        "Ex - Stray Kids"
    ],

    (3, 3): [
        "Lovely - Billie Eilish & Khalid",
        "Call Out My Name - The Weeknd",
        "Un-Break My Heart - Toni Braxton",
        "Die For You - The Weeknd",
        "we can't be friends - Ariana Grande"
    ],

    (3, 4): [
        "The Night We Met - Lord Huron",
        "Another Love - Tom Odell",
        "Creep - Radiohead",
        "Snuff - Slipknot",
        "November Rain - Guns N' Roses"
    ],

    # Energetic
    (4, 1): [
        "Blinding Lights - The Weeknd",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Don't Start Now - Dua Lipa",
        "Starships - Nicki Minaj",
        "One Kiss - Calvin Harris & Dua Lipa"
    ],

    (4, 2): [
        "God's Menu - Stray Kids",
        "Super - SEVENTEEN",
        "MIC Drop - BTS",
        "BANG BANG BANG - BIGBANG",
        "I AM - IVE"
    ],

    (4, 3): [
        "24K Magic - Bruno Mars",
        "Yeah! - Usher ft. Lil Jon & Ludacris",
        "Motive - Ariana Grande ft. Doja Cat",
        "Can't Feel My Face - The Weeknd",
        "OMG - Usher ft. will.i.am"
    ],

    (4, 4): [
        "Believer - Imagine Dragons",
        "Thunder - Imagine Dragons",
        "Centuries - Fall Out Boy",
        "The Pretender - Foo Fighters",
        "Immigrant Song - Led Zeppelin"
    ]
}

recommended_songs = songs.get((mood_choice, genre_choice))

# Display recommendation
print("\n--------------------------------")
print("Recommended for you:")
print("Genre:", genre)
print("Mood:", mood)
print("\nRecommended Songs:")

for i, song in enumerate(recommended_songs, 1):
    print(f"{i}. {song}")

print("--------------------------------")

# Wei Hong end of recommendation system

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
        print("\nMusic Recommendation - Coming Soon")

    elif choice == "0":
        print("\nThank you for using Spotify Music Assistant!")
        break

    else:
        print("\nInvalid choice.")
        print("Please enter a number from 0 to 5.")
        input("\nPress Enter to continue...")

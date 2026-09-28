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

#Wei HONG recommendation system
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

#Wei Hong end of recommendation system

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

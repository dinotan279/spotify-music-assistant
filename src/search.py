# =========================
# Aloysius - SEARCH SONG
# =========================

def search_song(songs):
    clear_screen()

    print("========================================")
    print("              SEARCH SONG")
    print("========================================")

    keyword = input("Enter song title or artist: ").lower()
    input("\nPress Enter to return to the main menu...")
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
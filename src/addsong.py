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
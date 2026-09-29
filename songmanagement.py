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
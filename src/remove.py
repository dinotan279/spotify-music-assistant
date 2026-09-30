# =========================
# Ethan Lim - REMOVE SONG
# =========================
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def remove_song(songs,save_songs):
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

    choice = input("\nEnter song number to remove: ").strip()

    # Input validation
    if choice == "":
        print("\nRemove Song cancelled.")
        input("Press Enter to return to the main menu...")
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(songs):
        print("\nInvalid choice.")
        input("Press Enter to return to the main menu...")
        return

    song = songs.pop(int(choice) - 1)
    save_songs(songs)

    print(f"\n✓ '{song['title']}' removed successfully!")
    input("\nPress Enter to return to the main menu...")

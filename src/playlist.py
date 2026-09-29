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
import os

from recommendation_data import RECOMMENDATIONS


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_music_recommendation(songs, save_songs):

    # =========================
    # MOOD SELECTION
    # =========================

    clear_screen()

    print("========================================")
    print("         MUSIC RECOMMENDATION")
    print("========================================")

    print("\nSelect your mood:")
    print("1. Happy")
    print("2. Sad")
    print("3. Energetic")
    print("4. Relaxed")

    print("\nPress Enter without typing to cancel.")

    mood_choice = input("\nEnter your choice: ").strip()

    if mood_choice == "":
        print("\nRecommendation cancelled.")
        input("Press Enter to return to the main menu...")
        return

    mood_map = {
        "1": "happy",
        "2": "sad",
        "3": "energetic",
        "4": "relaxed"
    }

    if mood_choice not in mood_map:
        print("\nInvalid choice.")
        input("Press Enter to return to the main menu...")
        return

    mood = mood_map[mood_choice]

    # =========================
    # GENRE SELECTION
    # =========================

    clear_screen()

    print("========================================")
    print("         MUSIC RECOMMENDATION")
    print("========================================")

    print(f"\nMood selected: {mood.capitalize()}")

    print("\nSelect your genre:")
    print("1. Pop")
    print("2. Rock")
    print("3. R&B")

    print("\nPress Enter without typing to cancel.")

    genre_choice = input("\nEnter your choice: ").strip()

    if genre_choice == "":
        print("\nRecommendation cancelled.")
        input("Press Enter to return to the main menu...")
        return

    genre_map = {
        "1": "pop",
        "2": "rock",
        "3": "rnb"
    }

    if genre_choice not in genre_map:
        print("\nInvalid choice.")
        input("Press Enter to return to the main menu...")
        return

    genre = genre_map[genre_choice]


    # =========================
    # GET RECOMMENDATIONS
    # =========================

    recommendations = RECOMMENDATIONS[mood][genre]


    # =========================
    # SHOW RECOMMENDED SONGS
    # =========================

    clear_screen()

    print("========================================")
    print("         MUSIC RECOMMENDATION")
    print("========================================")

    print(f"\nMood: {mood.capitalize()}")
    print(f"Genre: {genre.upper()}")

    print("\nRecommended Songs")
    print("----------------------------------------")

    for number, song in enumerate(recommendations, 1):
        print(f"\n{number}. {song['title']}")
        print(f"   Artist: {song['artist']}")
        print(f"   Genre: {song['genre']}")
        print(f"   Year: {song['year']}")

    print("\n----------------------------------------")
    print("0. Cancel")

    song_choice = input(
        "\nSelect a song to add to your playlist: "
    ).strip()


    # =========================
    # CANCEL SONG SELECTION
    # =========================

    if song_choice == "" or song_choice == "0":
        print("\nAdd to Playlist cancelled.")
        input("Press Enter to return to the main menu...")
        return


    # =========================
    # CHECK SONG NUMBER
    # =========================

    if not song_choice.isdigit():
        print("\nInvalid choice.")
        input("Press Enter to return to the main menu...")
        return

    song_number = int(song_choice)

    if song_number < 1 or song_number > len(recommendations):
        print("\nInvalid song number.")
        input("Press Enter to return to the main menu...")
        return


    # =========================
    # SELECTED SONG
    # =========================

    selected_song = recommendations[song_number - 1]

    clear_screen()

    print("========================================")
    print("           SELECTED SONG")
    print("========================================")

    print(f"\nTitle: {selected_song['title']}")
    print(f"Artist: {selected_song['artist']}")
    print(f"Genre: {selected_song['genre']}")
    print(f"Year: {selected_song['year']}")

    print("\n----------------------------------------")
    print("1. Add to Playlist")
    print("0. Cancel")

    confirm = input("\nEnter your choice: ").strip()


    # =========================
    # CANCEL ADDING
    # =========================

    if confirm == "" or confirm == "0":
        print("\nAdd to Playlist cancelled.")
        input("Press Enter to return to the main menu...")
        return


    # =========================
    # CONFIRM ADD
    # =========================

    if confirm != "1":
        print("\nInvalid choice.")
        input("Press Enter to return to the main menu...")
        return


    # =========================
    # CHECK DUPLICATE
    # =========================

    for song in songs:

        if (
            song["title"].lower() == selected_song["title"].lower()
            and
            song["artist"].lower() == selected_song["artist"].lower()
        ):

            print(
                f"\n'{selected_song['title']}' "
                "is already in your playlist."
            )

            input("\nPress Enter to return to the main menu...")
            return


    # =========================
    # ADD TO PLAYLIST
    # =========================

    song_to_add = {
        "title": selected_song["title"],
        "artist": selected_song["artist"],
        "genre": selected_song["genre"],
        "year": selected_song["year"]
    }

    songs.append(song_to_add)

    save_songs(songs)


    # =========================
    # SUCCESS
    # =========================

    print(
        f"\n✓ '{selected_song['title']}' "
        "added to your playlist!"
    )

    input("\nPress Enter to return to the main menu...")
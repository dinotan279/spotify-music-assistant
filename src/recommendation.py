import os
from recommendation_data import RECOMMENDATIONS


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_music_recommendation(songs):
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

    choice = input("\nEnter your choice: ").strip()

    if choice == "":
        print("\nRecommendation cancelled.")
        input("Press Enter to return to the main menu...")
        return

    mood_map = {
        "1": "happy",
        "2": "sad",
        "3": "energetic",
        "4": "relaxed"
    }

    if choice not in mood_map:
        print("\nInvalid choice.")
        input("Press Enter to return to the main menu...")
        return

    mood = mood_map[choice]

    recommendations = RECOMMENDATIONS[mood]

    print(f"\nRecommended songs for your {mood} mood:")
    print("----------------------------------------")

    for number, song in enumerate(recommendations, 1):
        print(f"\n{number}. {song['title']}")
        print(f"   Artist: {song['artist']}")
        print(f"   Genre: {song['genre']}")
        print(f"   Year: {song['year']}")

    input("\nPress Enter to return to the main menu...")
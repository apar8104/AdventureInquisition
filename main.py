from story_data import story
import json
import os

SAVE_FILE = "save.json"

ALL_ENDINGS = [
    "Treasure Ending",
    "Lost Ending",
    "Drowned Ending",
    "Survival Ending"
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

print(" Welcome to Adventure Aquisition, a choose your own adventure story game.\n Please type the corresponsing number to make your choices.\n Press 0 to EXIT at any time \n Press 9 to RESTART at anytime\n Enjoy!")

# Data Load Function
def load_data():
    if not os.path.exists(SAVE_FILE):
        return {}

    with open(SAVE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

# Data Save Function
def save_data(data):
    print("SAVING DATA:", data)  # DEBUG LINE
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_endings(unlocked):
    print("\n=== ENDINGS ACHIEVEMENTS ===\n")

    for ending in ALL_ENDINGS:
        if ending in unlocked:
            print(f"{GREEN}✔ {ending}{RESET}")
        else:
            print(f"{RED}✖ {ending}{RESET}")

    print("\n===========================\n")

# Core Gameplay
def play_game(username, data):
    current = "start"

    if username not in data:
        data[username] = []

    while True:
        node = story[current]

        print("\n" + node["text"])

        # Ending Gameplay Mode
        if "ending" in node:
            ending = node["ending"]

            if ending not in data[username]:
                data[username].append(ending)
                save_data(data)
                print("\n🏆 New ending unlocked!")

            print(f"\nYou reached: {ending}")
            print("\n0 - Exit")
            print("9 - Restart")
            print("8 - View Achievements")

            pick = input("\n> ")

            if pick == "0":
                return
            elif pick == "9":
                break
            elif pick == "8":
                show_endings(data[username])
                continue
            else:
                continue

        # Choice Gameplay Mode
        for i, choice in enumerate(node["choices"], 1):
            print(f"{i} - {choice[0]}")

        print("\n0 - Exit | 9 - Restart | 8 - View Achievements")

        pick = input("\n> ")

        if pick == "0":
            return
        if pick == "9":
            break
        if pick == "8":
            show_endings(data[username])
            continue

        try:
            pick = int(pick)
            current = node["choices"][pick - 1][1]
        except:
            print("Invalid input.")

def main():
    data = load_data()

    username = input("Enter username: ")

    print(f"\nWelcome, {username}!\n")

    while True:
        play_game(username, data)

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            break


main()
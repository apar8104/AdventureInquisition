from story_data import story
1
print(" Welcome to Adventure Aquisition, a choose your own adventure story game.\n Please type the corresponsing number to make your choices.\n Press 0 to EXIT at any time \n Press 9 to RESTART at anytime\n Enjoy!")

from story_data import story

def play_game():
    while True:
        current = "start"

        while True:
            node = story[current]

            print("\n" + node["text"])

            # ---------------- ENDING STATE ---------------- #
            if "ending" in node:
                print("\n🎉 Ending earned!")
                print("What would you like to do?")
                print("9 - Restart")
                print("0 - Exit")

                pick = input("\n> ")

                if pick == "0":
                    print("Goodbye!")
                    return

                elif pick == "9":
                    print("\n... Restarting...\n")
                    break  # restart game loop

                else:
                    print("Invalid input.")
                    continue

            # ---------------- NORMAL GAMEPLAY ---------------- #
            print("\nWhat will you do?\n")

            for i, choice in enumerate(node["choices"], 1):
                print(f"{i} - {choice[0]}")

            pick = input("\n> ")

            # EXIT
            if pick == "0":
                print("Goodbye!")
                return

            # RESTART
            if pick == "9":
                print("\n🔄 Restarting game...\n")
                break

            # CHOICE HANDLING
            try:
                pick = int(pick)
                if 1 <= pick <= len(node["choices"]):
                    current = node["choices"][pick - 1][1]
                else:
                    print("Invalid choice.")
            except:
                print("Enter a valid number.")

play_game()        
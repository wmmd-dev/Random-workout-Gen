import random





menu = str("""
    
 ⢀⡀⠀⠀⠀⠀⠀⠀⠀     ⢀⣤⣶⣤⠀⠀⠀⢠⣤⣄⠀      _       __           __               __                       
⠘⠻⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⣻⣿⣿⣿⡆⠀⠀⠈⠉⢻⣆      | |     / /___  _____/ /______  __  __/ /_   ____ ____  ____ 
⠀⠀⠀⠙⠛⠻⢿⣿⣷⣾⣷⣦⣿⣿⣿⣿⣯⣤⣄⣀⣀⣸⣿⡆    | | /| / / __ \/ ___/ //_/ __ \/ / / / __/  / __ `/ _ \/ __ \
        ⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃     | |/ |/ / /_/ / /  / ,< / /_/ / /_/ / /_   / /_/ /  __/ / / /
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠁⠀⠀     |__/|__/\____/_/  /_/|_|\____/\__,_/\__/   \__, /\___/_/ /_/ 
             ⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀                                                /____/             
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠋⠀

""")
def load_exercises(filename):
    exercises = {}
    category = None

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("[") and line.endswith("]"):
                category = line[1:-1].lower()
                exercises[category] = []

            elif category:
                exercises[category].append(line)

    return exercises


def print_workout(exercises, per_category=3):
    icons = {"core": """\͝(‡)͝/"""
    
             , "arms": "( ◡̀_◡́)ᕤ",
              
               "legs": "𓂾𓂾"}

    print()
    print("=" * 30)
    print("   TODAY'S WORKOUT ❚█══█❚")
    print("=" * 30)

    number = 1
    for group, moves in exercises.items():
        icon = icons.get(group, "•")
        print(f"\n{icon}  {group.upper()}")
        print("-" * 30)
        for move in random.sample(moves, min(per_category, len(moves))):
            print(f"  {number}. {move}")
            number += 1

    print("\n" + "=" * 30)
    print(" ❚█══█❚ STRENGTH ❚█══█❚")
    print("=" * 30)


exercises = load_exercises("excercizes.txt")
per_category = 3

while True:
    print(menu)
    print("[1] = generate")
    print("[2] = change exercises per section")
    print("[3] = exit")

    choice = input("\nPick an option: ")

    if choice == "1":
        print_workout(exercises, per_category)
        input("\nPress Enter key to go back to  menu")

    elif choice == "2":
        number = input("How many excercizes per section? ")
        if number.isdigit() and int(number) > 0:
            per_category = int(number)
            print(f" Now picking {per_category} excercizes per section.")
        else:
            print("Invalid input. Please enter a positive integer.")

    elif choice == "3":
        print("Skipping the workout for today i see....")
        break

    else:
        print("Invalid input")




      
               
             








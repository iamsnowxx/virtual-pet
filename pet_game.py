import time

# Pet data
pet = {
    "name": "",
    "hunger": 100,
    "happiness": 100,
    "cleanliness": 100,
    "groomed": True,
    "outfits": []
}

# Player data
player = {
    "money": 200
}

# Decay per turn
DECAY = {
    "hunger": 5,
    "happiness": 4,
    "cleanliness": 3
}

# Cost per action
COST = {
    "feed": 10,
    "play": 8,
    "clean": 6,
    "groom": 12,
    "dress": 20
}

def clamp(value, min_val=0, max_val=100):
    return max(min_val, min(value, max_val))

def charge_player(action):
    cost = COST[action]
    if player["money"] < cost:
        print(f"❌ Not enough money! ${cost} required but you have only ${player['money']}.")
        return False
    player["money"] -= cost
    print(f"💸 You spent ${cost}. Your remaining balance is ${player['money']}.")
    return True

def show_status():
    print("\n📋 Pet Status:")
    print(f"🐾 Name: {pet['name']}")
    print(f"🍖 Hunger:     {pet['hunger']}")
    print(f"😊 Happiness:  {pet['happiness']}")
    print(f"🧼 Cleanliness:{pet['cleanliness']}")
    print(f"💇 Groomed:    {'Yes' if pet['groomed'] else 'No'}")
    print(f"👗 Outfits:    {', '.join(pet['outfits']) if pet['outfits'] else 'None'}")
    print(f"💰 Money:      ${player['money']}\n")

def check_warnings():
    if pet['hunger'] <= 20:
        print(f"⚠️ {pet['name']} looks really hungry! Try feeding them.")
    if pet['happiness'] <= 20:
        print(f"⚠️ {pet['name']} seems bored. Maybe you should play with them.")
    if pet['cleanliness'] <= 20:
        print(f"⚠️ {pet['name']} is getting very dirty. Time for a bath!")

def feed():
    if not charge_player("feed"):
        return
    pet['hunger'] = clamp(pet['hunger'] + 20)
    print(f"🍖 You fed {pet['name']}.")

def play():
    if not charge_player("play"):
        return
    pet['happiness'] = clamp(pet['happiness'] + 20)
    pet['cleanliness'] = clamp(pet['cleanliness'] - 10)
    print(f"🎾 You played with {pet['name']}.")

def clean():
    if not charge_player("clean"):
        return
    pet['cleanliness'] = clamp(pet['cleanliness'] + 25)
    print(f"🧼 You cleaned {pet['name']}.")

def groom():
    if not charge_player("groom"):
        return
    pet['cleanliness'] = 100
    pet['groomed'] = True
    print(f"💇 {pet['name']} is now well-groomed and super clean!")

def dress():
    if not charge_player("dress"):
        return
    print("👗 Choose an outfit to buy:")
    options = ["Cool Hat", "Fancy Glasses", "Rainbow Scarf"]
    for i, item in enumerate(options, 1):
        print(f"{i}. {item}")
    choice = input("Enter number: ").strip()
    if choice in ["1", "2", "3"]:
        selected = options[int(choice) - 1]
        if selected in pet['outfits']:
            print("⚠️ Already owned.")
        else:
            pet['outfits'].append(selected)
            print(f"🎉 You dressed {pet['name']} with a {selected}!")
    else:
        print("❌ Invalid choice.")

def update_status():
    for key in DECAY:
        pet[key] = clamp(pet[key] - DECAY[key])
    pet['groomed'] = False  # Reset grooming over time

def check_health():
    if pet['hunger'] <= 0:
        print(f"\n💀 {pet['name']} left because of starvation.")
        return False
    if pet['happiness'] <= 0:
        print(f"\n😢 {pet['name']} ran away to find joy.")
        return False
    if pet['cleanliness'] <= 0:
        print(f"\n🤢 {pet['name']} got sick and left...")
        return False
    return True

def main():
    print("🐶 Welcome to Virtual Pet!")
    pet['name'] = input("Please name your pet: ").strip() or "Buddy"
    print(f"You're now caring for {pet['name']}! Keep them happy and clean!")

    while True:
        print("\n--- What would you like to do? ---")
        print("Type one of the following commands:")
        print("feed / play / clean / groom / dress / status / quit")

        command = input("Your choice: ").strip().lower()

        if command == "feed":
            feed()
        elif command == "play":
            play()
        elif command == "clean":
            clean()
        elif command == "groom":
            groom()
        elif command == "dress":
            dress()
        elif command == "status":
            show_status()
            continue
        elif command == "quit":
            print(f"\n👋 Thanks for playing! {pet['name']} will miss you!")
            break
        else:
            print("❌ Invalid command.")
            continue

        update_status()
        check_warnings()
        if not check_health():
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
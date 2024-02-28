import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = []

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, amount):
        self.hp += amount

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.monster = None
        self.item = None

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_monster(self, monster):
        self.monster = monster

    def add_item(self, item):
        self.item = item

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def take_damage(self, damage):
        self.hp -= damage

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def fight(player, monster):
    while player.hp > 0 and monster.hp > 0:
        player_damage = random.randint(5, 20)
        monster_damage = random.randint(5, 15)

        player.take_damage(monster_damage)
        monster.take_damage(player_damage)

        print(f"{player.name} hits {monster.name} for {player_damage} damage.")
        print(f"{monster.name} hits {player.name} for {monster_damage} damage.")
        print(f"{player.name}'s HP: {player.hp}, {monster.name}'s HP: {monster.hp}")

    if player.hp <= 0:
        print("You were defeated. Game Over.")
        exit()
    else:
        print(f"You defeated the {monster.name}!")

def main():
    # Create player
    player_name = input("Enter your name: ")
    player = Player(player_name)

    # Create rooms
    entrance = Room("Entrance", "You are at the entrance of the dungeon.")
    hall = Room("Hall", "You are in a dark hallway.")
    treasure_room = Room("Treasure Room", "You found the treasure room!")
    
    # Define exits
    entrance.add_exit("north", hall)
    hall.add_exit("south", entrance)
    hall.add_exit("east", treasure_room)
    
    # Create monsters
    goblin = Monster("Goblin", 50, 10)
    dragon = Monster("Dragon", 100, 20)
    
    # Place monsters in rooms
    hall.add_monster(goblin)
    treasure_room.add_monster(dragon)
    
    # Start the game
    current_room = entrance
    print(f"Welcome, {player.name}! You find yourself at the entrance of a mysterious dungeon.")

    while True:
        print("\n" + "=" * 50)
        print(current_room.name)
        print(current_room.description)

        if current_room.monster:
            print(f"A {current_room.monster.name} appears!")
            fight(player, current_room.monster)
        
        command = input("Enter your command (north/south/east/west/exit): ").lower()
        
        if command == "exit":
            print("Goodbye! Thanks for playing.")
            break
        elif command in current_room.exits:
            current_room = current_room.exits[command]
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()

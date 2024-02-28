# Text-based-adventure-game-2
## Description-
This Python program implements a simple text-based adventure game. It defines classes for the player, rooms, monsters, and items. The player can explore different rooms, encounter monsters, fight them, and collect items. The game continues until the player finds the treasure room or decides to exit.
## Explanation-
  -1. The `Player` class represents the player character with attributes for name, health points (hp), and inventory, along with methods for managing health and inventory.

  -2. The `Room` class represents a location in the game with attributes for name, description, exits (connections to other rooms), and optionally a monster and an item, along with methods for managing exits, monsters, and items.

  -3. The `Monster` class represents an enemy in the game with attributes for name, health points (hp), and damage, along with a method for taking damage.

  -4. The `Item` class represents an item that can be collected in the game with attributes for name and description.

  -5. The `fight` function simulates a battle between the player and a monster, handling damage calculation until one of them is defeated.

  -6. The `main` function initializes the game environment, including creating the player, defining rooms, placing monsters, and starting the game loop.

  -7. Game environment initialization sets up the initial state of the game, including creating instances of rooms, defining connections between rooms, and placing monsters in specific rooms.

  -8. The game loop controls the flow of the game, including displaying information about the current room and any encounters with monsters, and allowing the player to navigate through rooms or exit the game.

## Note:
Remember this is another program which was created purely for fun.

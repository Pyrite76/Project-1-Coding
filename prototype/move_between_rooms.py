"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {
        "description": "This large room has many ruined tables and chairs, and a single large door still stands to the south.",   
        "exits": {"south": "Bedroom"}
    },
    "Bedroom": {
        "description": "This room has a soft bed in its center and two doors, one to the north and one to the east.",
        "exits": {"north": "Great Hall", "east": "Cellar"}
    }, #I have changed how the room group looks in order to make this easier system to be used for both descriptions and exits.#
    "Cellar": {
        "description": "This room, down a flight of stairs, is cold and damp, and has a feeling of being watched.",
        "exits": {"west": "Bedroom"}
    }
}
current_room = "Great Hall"

while True:
    room_data = rooms[current_room]
    print(f"\n {current_room}")
    print(room_data["description") #For my own project, I intend for each room to have a description to see what is in each room.

    exits = room_data["exits"]
    print("Exits:", ", ".join(exits.keys()))

    command = input("Which way do you want to go? (or input 'leave' to exit): ").lower().strip()

    if command == "leave":
        print("I hope you injoyed")
        break
    elif command in exits:
        current_room = exits[command]
    else:
        print("Theres a wall in the way")

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

# TODO: Run and debug all milestone cases in prototype/README.md.

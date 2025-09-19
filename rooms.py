def check_availability(connection):
    """
    Fetch and display the availability of rooms from the rooms table.
    
    Args:
        connection: The MySQL connection object.
    """
    cursor = connection.cursor()
    
    # Fetch all rooms and their occupancy status
    cursor.execute("SELECT RoomID, RoomNumber, Occupied FROM rooms")
    rooms = cursor.fetchall()
    
    total_rooms = len(rooms)
    occupied_rooms = [room for room in rooms if room[2] == 1]  # Check if the room is occupied (room[2] is Occupied)
    available_rooms = [room for room in rooms if room[2] == 0]  # Check if the room is available
    
    # Print room availability status
    print("\n--- Room Status ---")
    print(f"Total Rooms: {total_rooms}")
    print(f"Occupied Rooms: {len(occupied_rooms)}")
    print(f"Available Rooms: {len(available_rooms)}")
    
    print("\nList of Available Rooms:")
    for room in available_rooms:
        print(f"RoomID: {room[0]}, RoomNumber: {room[1]}")
    
    return True

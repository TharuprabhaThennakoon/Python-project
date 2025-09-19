from connection import connect_to_mysql
from rooms import check_availability

def allocate_room():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    # Fetch all students from the database
    cursor.execute("SELECT StudentID, FirstName, LastName FROM students")
    students = cursor.fetchall()
    
    # Display students
    print("\nAvailable Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]} {student[2]}")
    
    # Input student ID
    student_id = input("Enter Student ID: ")
    
    # Call check_availability() to see available rooms
    available = check_availability(connection) 
    if not available:
        print("No rooms are available.")
        cursor.close()
        connection.close()
        return

    room_id = input("Enter Room ID to allocate: ")
    
    # Input allocation and leaving dates
    allocating_date = input("Enter allocation date (YYYY-MM-DD): ")
    leaving_date = input("Enter leaving date (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO room_allocations (StudentID, RoomID, AllocationDate, LeavingDate) VALUES (%s, %s, %s, %s)",
        (student_id, room_id, allocating_date, leaving_date)
    )
    
    cursor.execute(
        "UPDATE rooms SET Occupied = 1 WHERE RoomID = %s", (room_id,)
    )
    

    connection.commit()
    
    print("Allocation saved successfully!")
    
    cursor.close()
    connection.close()


def make_room_available():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    # Fetch all occupied rooms
    cursor.execute("SELECT RoomID, RoomNumber FROM rooms WHERE Occupied = 1")
    occupied_rooms = cursor.fetchall()
    
    # Show occupied rooms
    if occupied_rooms:
        print("\n--- Occupied Rooms ---")
        for room in occupied_rooms:
            print(f"RoomID: {room[0]}, RoomNumber: {room[1]}")
    else:
        print("No rooms are currently occupied.")
        cursor.close()
        connection.close()
        return
    
    # Get the Room ID to set as available
    room_id = input("\nEnter RoomID to make available: ")
    
    # Update the room's Occupied status to 0 (available)
    cursor.execute(
        "UPDATE rooms SET Occupied = 0 WHERE RoomID = %s", (room_id,)
    )
    
    # Commit the transaction
    connection.commit()
    
    # Check if the update was successful
    if cursor.rowcount > 0:
        print(f"Room with RoomID {room_id} is now available.")
    else:
        print(f"No room found with RoomID {room_id}.")
    
    cursor.close()
    connection.close()





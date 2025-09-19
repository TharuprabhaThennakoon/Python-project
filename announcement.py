def add_announcement(connection, message, student_id):
    """
    Add a new announcement to the announcements table.
    
    Args:
        connection: The MySQL connection object.
        message: The announcement message.
        student_id: The ID of the student creating the announcement.
    """
    query = """
    INSERT INTO announcements (Message, StudentID)
    VALUES (%s, %s);
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (message, student_id))
        connection.commit()
        print(f"Announcement added successfully: {message}")
    except Exception as e:
        print(f"Error while adding announcement: {e}")

def read_all_announcements(connection):
    """
    Fetch all announcements from the announcements table.
    
    Args:
        connection: The MySQL connection object.
    """
    query = "SELECT AnnouncementID, Message, CreatedAt, StudentID FROM announcements;"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        announcements = cursor.fetchall()
        if not announcements:
            print("No announcements found.")
        else:
            print("Announcements:")
            for announcement in announcements:
                print(f"ID: {announcement[0]}, Message: {announcement[1]}, Created At: {announcement[2]}, Student ID: {announcement[3]}")
    except Exception as e:
        print(f"Error while fetching announcements: {e}")

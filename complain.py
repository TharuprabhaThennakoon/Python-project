def add_complaint(connection, comment, student_id):
    """
    Add a new complaint to the complaint table without using bind parameters.
    
    Args:
        connection: The MySQL connection object.
        comment: The complaint comment.
        student_id: The ID of the student lodging the complaint.
    """
    query = f"""
    INSERT INTO complaint (Comment, StudentID)
    VALUES ('{comment}', {student_id});
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Complaint added successfully: {comment}")
    except Exception as e:
        print(f"Error while adding complaint: {e}")

def read_all_complaints(connection):
    """
    Fetch all complaints from the complaint table without using bind parameters.
    
    Args:
        connection: The MySQL connection object.
    """
    query = "SELECT ComplainID, Comment, StudentID FROM complaint;"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        complaints = cursor.fetchall()
        if not complaints:
            print("No complaints found.")
        else:
            print("Complaints:")
            for complaint in complaints:
                print(f"ID: {complaint[0]}, Comment: {complaint[1]}, Student ID: {complaint[2]}")
    except Exception as e:
        print(f"Error while fetching complaints: {e}")

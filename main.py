from rooms import check_availability
from connection import connect_to_mysql, create_tables
from complain import add_complaint, read_all_complaints
from announcement import add_announcement, read_all_announcements
from roomallocation import allocate_room, make_room_available
from student_registration import register_student

def admin_login():
    """
    Admin login with hardcoded credentials.
    Returns True if login is successful, else False.
    """
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    # Hardcoded admin credentials
    if username == "admin" and password == "admin123":
        print("Admin login successful!")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

def user_menu(connection):
    """
    Menu for user actions.
    """
    while True:
        print("\n----------")
        print("User Menu:")
        print("----------2")
        print("1. View Announcements")
        print("2. Add a Complaint")
        print("3. Check Room Availability")
        print("4. Logout")
        
        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '1':
            read_all_announcements(connection)
        elif user_choice == '2':
            comment = input("Enter your complaint: ")
            student_id = int(input("Enter your student ID: "))
            add_complaint(connection, comment, student_id)
        elif user_choice == '3':
            check_availability(connection)
        elif user_choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option, please try again.")

def admin_menu(connection):
    """
    Menu for admin actions.
    """
    while True:
        print("\n------------")
        print("Admin Menu:")
        print("------------")
        print("1. Add Announcement")
        print("2. Register Student")
        print("3. Allocate Room")
        print("4. Make Room Available")
        print("5. Read Complaints")
        print("6. Logout")

        admin_choice = input("Enter your choice (1-6): ")

        if admin_choice == '1':
            message = input("Enter announcement message: ")
            student_id = int(input("Enter student ID: "))
            add_announcement(connection, message, student_id)
        elif admin_choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            gender = input("Enter gender (Male/Female/Other): ")
            nationality = input("Enter nationality: ")
            contact_number = input("Enter contact number: ")
            email = input("Enter email: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            role_id = 2  # Default role as User
            register_student(first_name, last_name, gender, nationality, contact_number, email, date_of_birth, role_id)
        elif admin_choice == '3':
            allocate_room()
        elif admin_choice == '4':
            make_room_available()
        elif admin_choice == '5':
            read_all_complaints(connection)
        elif admin_choice == '6':
            print("Logging out...")
            break
        else:
            print("Invalid option, please try again.")

def main():
    # Connect to MySQL
    connection = connect_to_mysql()

    if connection:
        create_tables(connection)  # Ensure tables are created

        while True:
            print("\t\t\t***************************************")
            print("\t\t\tWelcome to the Hostel Management System")
            print("\t\t\t***************************************")
            print("\n1. Admin Login")
            print("\n2. User Menu")
            print("\n3. Exit")

            choice = input("\nEnter your choice (1-3): ")

            if choice == '1':
                # Admin login
                if admin_login():
                    admin_menu(connection)
                else:
                    print("Failed to log in as admin.")
            elif choice == '2':
                # User actions (no login required for user)
                user_menu(connection)
            elif choice == '3':
                print("Exiting system...")
                break
            else:
                print("Invalid option, please try again.")
    else:
        print("Failed to connect to the database. Exiting program.")


main()
import mysql.connector
from mysql.connector import Error
from connection import connect_to_mysql

connection = connect_to_mysql()

def register_student(first_name, last_name, gender, nationality, contact_number, email, date_of_birth, role_id):
    try:
       
        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = """INSERT INTO students (FirstName, LastName, Gender, Nationality, ContactNumber, 
                               Email, DateOfBirth, RoleID)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            
           
            student_data = (first_name, last_name, gender, nationality, contact_number, email, date_of_birth, role_id)
            
          
            cursor.execute(insert_query, student_data)
            
            connection.commit()
            
            print("Student registered successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# gender = input("Enter gender (Male/Female/Other): ")
# nationality = input("Enter nationality: ")
# contact_number = input("Enter contact number: ")
# email = input("Enter email: ")
# date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
# role_id = int(input("Enter role ID: "))

# register_student(first_name, last_name, gender, nationality, contact_number, email, date_of_birth, role_id)
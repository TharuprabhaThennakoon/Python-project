import mysql.connector

def connect_to_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='hostelmanagementsystem',
        port=3306
    )
    if connection.is_connected():
        print("Connected to the database.")
        return connection
    else:
        print("Failed to connect to the database.")
        return None

def create_tables(connection):
    cursor = connection.cursor()
    
    # Create table queries
    create_table_queries = [
        """
        CREATE TABLE IF NOT EXISTS announcements (
            AnnouncementID int(11) NOT NULL AUTO_INCREMENT,
            Message text NOT NULL,
            CreatedAt timestamp NOT NULL DEFAULT current_timestamp(),
            StudentID int(11) NOT NULL,
            PRIMARY KEY (AnnouncementID),
            KEY StudentID (StudentID),
            FOREIGN KEY (StudentID) REFERENCES students (StudentID)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """,
        """
        CREATE TABLE IF NOT EXISTS complaint (
            ComplainID int(11) NOT NULL AUTO_INCREMENT,
            Comment varchar(500) DEFAULT NULL,
            StudentID int(11) NOT NULL,
            PRIMARY KEY (ComplainID),
            KEY StudentID (StudentID),
            FOREIGN KEY (StudentID) REFERENCES students (StudentID)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """,
        """
        CREATE TABLE IF NOT EXISTS payments (
            PaymentID int(11) NOT NULL AUTO_INCREMENT,
            StudentID int(11) NOT NULL,
            Amount decimal(10,2) NOT NULL,
            PaymentDate date NOT NULL,
            PaymentMethod enum('Cash','Card','Online') NOT NULL,
            PRIMARY KEY (PaymentID),
            KEY StudentID (StudentID),
            FOREIGN KEY (StudentID) REFERENCES students (StudentID)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """,
        """
        CREATE TABLE IF NOT EXISTS rooms (
            RoomID int(11) NOT NULL AUTO_INCREMENT,
            RoomNumber varchar(10) NOT NULL,
            Capacity int(11) NOT NULL,
            Occupied int(11) DEFAULT 0,
            PRIMARY KEY (RoomID),
            UNIQUE KEY RoomNumber (RoomNumber)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """,
        """
        CREATE TABLE IF NOT EXISTS room_allocations (
            AllocationID int(11) NOT NULL AUTO_INCREMENT,
            StudentID int(11) NOT NULL,
            RoomID int(11) NOT NULL,
            AllocationDate date NOT NULL,
            LeavingDate date DEFAULT NULL,
            PRIMARY KEY (AllocationID),
            KEY StudentID (StudentID),
            KEY RoomID (RoomID),
            FOREIGN KEY (StudentID) REFERENCES students (StudentID),
            FOREIGN KEY (RoomID) REFERENCES rooms (RoomID)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """,
        """
        CREATE TABLE IF NOT EXISTS students (
            StudentID int(11) NOT NULL AUTO_INCREMENT,
            FirstName varchar(100) NOT NULL,
            LastName varchar(100) NOT NULL,
            Gender enum('Male','Female','Other') DEFAULT NULL,
            Nationality varchar(100) DEFAULT NULL,
            ContactNumber varchar(15) DEFAULT NULL,
            Email varchar(100) DEFAULT NULL,
            DateOfBirth date DEFAULT NULL,
            RoleID int(11) NOT NULL,
            PRIMARY KEY (StudentID),
            UNIQUE KEY Email (Email),
            KEY RoleID (RoleID),
            FOREIGN KEY (RoleID) REFERENCES user_roles (RoleID)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """,
        """
        CREATE TABLE IF NOT EXISTS user_roles (
            RoleID int(11) NOT NULL AUTO_INCREMENT,
            RoleName varchar(50) NOT NULL,
            PRIMARY KEY (RoleID)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """
    ]

    try:
        for query in create_table_queries:
            cursor.execute(query)
        print("All tables created successfully (if they did not exist).")
    except Exception as e:
        print(f"Error creating tables: {e}")
    finally:
        cursor.close()



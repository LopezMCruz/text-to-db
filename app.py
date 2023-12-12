from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")



# establish connection
mydb = {
    
    'user':DB_USER,
    'password':DB_PASS,
    'host':DB_HOST,
    'database':DB_NAME
}
# Establish a database connection
conn = mysql.connector.connect(**mydb)
cursor = conn.cursor()

# Directory containing your .txt files
directory = "C:/Users/CruzC/text-to-db/text-docs/Dracula/"

# Function to extract chapter and section from filename
def extract_info_from_filename(filename):
    parts = filename.replace('dracula_', '').replace('.txt', '').split('_')
    chapter = parts[0]
    section = parts[1]
    return chapter, section

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # Extract chapter and section
        chapter, section = extract_info_from_filename(filename)

        # Read content from file
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # SQL query to insert data
        query = "INSERT INTO `dracula` (`chapter`, `section`, `content`) VALUES (%s, %s, %s)"
        values = (chapter, section, content)

        # Execute query
        cursor.execute(query, values)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Data insertion complete.")
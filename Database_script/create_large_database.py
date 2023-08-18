import random
from datetime import timedelta
from faker import Faker
import sqlite3


# Start faker session
fake = Faker()

# Connect to SQLite database, It will be created if it does not exist 
conn = sqlite3.connect(r"#path to file here")
c = conn.cursor()


# Create the Users table, if it does not exist yet. if it does, skips.
# Same for Books Borrowers & Loans
c.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password_hash TEXT,
        role TEXT
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        published_year INTEGER,
        isbn TEXT
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Borrowers(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Loans(
        id INTEGER PRIMARY KEY,
        book_id INTEGER,
        borrower_id INTEGER,
        loan_date TEXT,
        return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES Books(id),
        FOREIGN KEY (borrower_id) REFERENCES Borrowers(id)
    )
""")

#  data for the Users table
roles = ['librarian', 'borrower', 'administrator']
for _ in range(20000):
    username = fake.user_name()
    password_hash = fake.sha256()  # placeholder
    role = random.choice(roles)
    c.execute("""
        INSERT INTO Users(username, password_hash, role)
        VALUES(?, ?, ?)
    """, (username, password_hash, role))

# data for the Books and Borrowers tables
book_ids = []
for _ in range(20000):
    c.execute("""
        INSERT INTO Books(title, author, published_year, isbn)
        VALUES(?, ?, ?, ?)
    """, (fake.catch_phrase(), fake.name(), fake.year(), fake.isbn13()))
    book_ids.append(c.lastrowid)

borrower_ids = []
for _ in range(20000):
    c.execute("""
        INSERT INTO Borrowers(name, email)
        VALUES(?, ?)
    """, (fake.name(), fake.email()))
    borrower_ids.append(c.lastrowid)


#includes borrowers that have loaned multiple books. 
# Generate a random number of loans for each borrower, with a random book for each loan
# we're gonna randomize the chance the book isnt returned yet between a random percentage between 10-50%. this makes our data more interesting but we nede to create a variable first
for borrower_id in borrower_ids:
    for _ in range(random.randint(1, 5)):  # Each borrower borrows 1 to 5 books
        book_id = random.choice(book_ids)
        loan_date = fake.date_object()
        chance_not_returned = random.uniform(0.10,0.50)
        if random.random() < chance_not_returned:
            #Book not returned
            return_date = None
        else:
            #book is returned 1-30 days after loan date
            return_date = loan_date + timedelta(days=random.randint(1,30))
            
# if the book is not returned, we only insert loan_date and exclude return_date
        if return_date:
            c.execute("""
                INSERT INTO Loans(book_id, borrower_id, loan_date, return_date)
                VALUES(?, ?, ?, ?)
            """, (book_id, borrower_id, loan_date.strftime("%Y-%m-%d"), return_date.strftime("%Y-%m-%d")))
        else:
            c.execute("""
                INSERT INTO Loans(book_id, borrower_id, loan_date)
                VALUES(?,?,?)""", (book_id, borrower_id, loan_date.strftime("%Y-%m-%d")))
            

# Commit the changes and close connection
conn.commit()
conn.close()

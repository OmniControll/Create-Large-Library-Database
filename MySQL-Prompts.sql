-- show all tables
.tables
-- show all borrowers in database
SELECT * FROM Borrowers;
-- show all books in database
SELECT * FROM Books;
--show all loans
SELECT * FROM Loans;
-- show all users from database
SELECT * FROM Users;

-- set a timer to track query performance
.timer ON
SELECT * FROM Books WHERE published_year = 1998

-- count all books in database and see total
SELECT COUNT(*) FROM Books;

-- count number of loans, and find earliest and latest loan dates
SELECT COUNT(*), MIN(loan_date), MAX(loan_date) FROM Loans;

-- list the top 10 most common book titles in database
SELECT title, COUNT(*)
FROM Books
GROUP BY title
ORDER BY COUNT(*) DESC
LIMIT 10;

-- lets find out howmany books are on loan currently.author
-- we have to check if they have a loan date, but no return date
SELECT COUNT(*) FROM Loans WHERE return_date IS NULL;

-- lets now list all loans w/ corresponding book titles + borrower names
-- i will use JOIN  (default, inner join) to create a relation between the tables

SELECT Loans.id, Books.title, Borrowers.name
FROM Loans
JOIN Books ON Loans.book_id = Books.id
JOIN Borrowers ON Loans.borrower_id = Borrowers.id;

-- now a left join to match the values from Books to borrowers. I want to list all books on loan, 
--and if they're not on loan, it will be "not on loan" For this, 
-- I will use a CASE Statement to check values.

SELECT Books.title,
    CASE
        WHEN Borrowers.name IS NULL THEN 'Not on loan'
        ELSE Borrowers.name
    END AS borrower_name
FROM Books
LEFT JOIN Loans ON Books.id = Loans.book_id
LEFT JOIN Borrowers ON Loans.borrower_id = Borrowers.id;


-- now i will combine Books with Users and borrowers with aliases, 
-- to get a view of all info on each loan
SELECT Users.username, Users.role, Books.title, Borrowers.name AS borrower_name
FROM Loans
JOIN Users ON Users.id = Loans.borrower_id
JOIN Books ON Books.id = Loans.book_id
JOIN Borrowers ON Borrowers.id = Loans.borrower_id;


-- we want to know the role of the user who processed the loan for each book
--for this im going to join loans, users, books and borrowers

SELECT Users.username, Users.role, Books.title, Borrowers.name AS borrower_name
FROM Loans
JOIN Users ON Users.id = Loans.borrower_id
JOIN Books ON Books.id = Loans.book_id
JOIN Borrowers ON Borrowers.id = Loans.borrower_id;

-- now lets find all books that have been borrowed by a specific borrower

SELECT title
FROM Books
WHERE id IN
    (SELECT book_id
    FROM Loans
    WHERE borrower_id =
        (SELECT id FROM Borrowers WHERE name = 'Emily Bailey'));

        


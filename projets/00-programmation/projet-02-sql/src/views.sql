-- Vue qui resume les emprunts en cours avec les infos utiles
CREATE VIEW current_loans AS
SELECT
    books.title AS livre,
    authors.name AS auteur,
    borrowers.name AS emprunteur,
    loans.loan_date AS date_emprunt
FROM loans
JOIN books ON loans.book_id = books.id
JOIN authors ON books.author_id = authors.id
JOIN borrowers ON loans.borrower_id = borrowers.id
WHERE loans.return_date IS NULL;

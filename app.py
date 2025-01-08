from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***************",
    database="pavandb"
)

@app.route('/')
def index():
    return render_template('index.html')

# View all books
@app.route('/view_books')
def view_books():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    return render_template('view_books.html', books=books)

# Add a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']

        cursor = db.cursor()
        cursor.execute("INSERT INTO books (title, author, genre, year) VALUES (%s, %s, %s, %s)", 
                       (title, author, genre, year))
        db.commit()
        cursor.close()
        flash('Book added successfully!', 'success')
        return redirect(url_for('view_books'))
    return render_template('add_book.html')

# Update a book
@app.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    cursor = db.cursor()
    
    # Fetch the current details of the book
    cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cursor.fetchone()

    if request.method == 'POST':
        # Get new book details from the form
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']

        # Update the book in the database
        cursor.execute("UPDATE books SET title = %s, author = %s, genre = %s, year = %s WHERE id = %s", 

        
                       (title, author, genre, year, id))
        db.commit()
        cursor.close()
        
        flash('Book updated successfully!', 'success')
        return redirect(url_for('view_books'))
    
    cursor.close()
    return render_template('update_books.html', book=book)

# Borrow a book
@app.route('/borrow_book/<int:book_id>', methods=['GET', 'POST'])
def borrow_book(book_id):
    if request.method == 'POST':
        student_id = request.form['student_id']
        borrow_date = datetime.now().date()

        cursor = db.cursor()
        cursor.execute("INSERT INTO borrow (book_id, student_id, borrow_date) VALUES (%s, %s, %s)", 
                       (book_id, student_id, borrow_date))
        db.commit()
        cursor.close()
        flash('Book borrowed successfully!', 'success')
        return redirect(url_for('view_books'))

    # Fetch student and book details for borrowing form
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    return render_template('borrow_books.html', book=book, students=students)

# Return a book
@app.route('/return_book/<int:borrow_id>', methods=['POST'])
def return_book(borrow_id):
    return_date = datetime.now().date()

    cursor = db.cursor()
    cursor.execute("UPDATE borrow SET return_date = %s WHERE id = %s AND return_date IS NULL", 
                   (return_date, borrow_id))
    db.commit()
    cursor.close()
    flash('Book returned successfully!', 'success')
    return redirect(url_for('view_borrowed_books'))

# View borrowed books
@app.route('/view_borrowed_books')
def view_borrowed_books():
    cursor = db.cursor()
    cursor.execute("""
        SELECT bb.id, b.title, s.name, bb.borrow_date, bb.return_date 
        FROM borrow bb
        JOIN books b ON bb.book_id = b.id
        JOIN students s ON bb.student_id = s.id
    """)
    borrowed_books = cursor.fetchall()
    cursor.close()
    return render_template('view_borrowed_books.html', borrowed_books=borrowed_books)

# View all students
@app.route('/view_students')
def view_students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    return render_template('view_students.html', students=students)

# Add a new student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']

        cursor = db.cursor()
        cursor.execute("INSERT INTO students (name, student_id) VALUES (%s, %s)", 
                       (name, student_id))
        db.commit()
        cursor.close()
        flash('Student added successfully!', 'success')
        return redirect(url_for('view_students'))
    return render_template('add_student.html')

# Delete a student
@app.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('view_students'))

# Delete a book
@app.route('/delete_book/<int:id>', methods=['POST'])
def delete_book(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('view_books'))

# View faculty members
@app.route('/view_faculty')
def view_faculty():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM faculty")
    faculty_members = cursor.fetchall()
    cursor.close()
    return render_template('view_faculty.html', faculty_members=faculty_members)

# Add a new faculty member
@app.route('/add_faculty', methods=['GET', 'POST'])
def add_faculty():
    if request.method == 'POST':
        name = request.form['name']
        faculty_id = request.form['faculty_id']
        role = request.form['role']

        cursor = db.cursor()
        cursor.execute("INSERT INTO faculty (name, faculty_id, role) VALUES (%s, %s, %s)", 
                       (name, faculty_id, role))
        db.commit()
        cursor.close()
        flash('Faculty added successfully!', 'success')
        return redirect(url_for('view_faculty'))
    return render_template('add_faculty.html')

# Delete a faculty member
@app.route('/delete_faculty/<int:id>', methods=['POST'])
def delete_faculty(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM faculty WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    flash('Faculty member deleted successfully!', 'success')
    return redirect(url_for('view_faculty'))

if __name__ == '__main__':
    app.run(debug=True)

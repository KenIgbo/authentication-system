from flask import Flask, request, redirect, session, url_for, render_template, flash

import sqlite3

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'my_secret_key_123_xyz'

def create_db():
    connection = sqlite3.connect("data_b.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE NOT NULL,
            password TEXT
        )"""
    )

    connection.commit()
    connection.close()

create_db()


def hash_password(reg_password):
    masked = generate_password_hash(reg_password)
    return masked


def verify_password(hashed_password, login_password):
    check = check_password_hash(hashed_password, login_password)
    return check

 
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = hash_password(password)

        connection = sqlite3.connect("data_b.db")
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO users(name, email, password) VALUES(?, ?, ?)", (name, email, hashed_password))

            connection.commit()
            connection.close()

            flash("Account created")
            return redirect(url_for('login'))

        except sqlite3.IntegrityError as e:
            connection.commit()
            connection.close()

            flash("Email already in use")
            return redirect(url_for('home'))
        
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global row_dic
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        connection = sqlite3.connect("data_b.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE email=?", (email,))

        row = cursor.fetchone()
        connection.close()

        if row:
            row_dic = {"id":row[0], "name":row[1], "email":row[2], "password":row[3]}
            confirmed = verify_password(row_dic["password"], password)

            if confirmed:
                session["email"] = email

                if "email" in session:
                    flash("Login successful")
                    return redirect(url_for('dashboard'))
                else:
                    flash("Login failed")
                    return redirect(url_for('login'))
            else:
                flash("Incorrect password")
                return redirect(url_for('login'))
        else:
            flash("Email does not exist")
            return redirect(url_for('login'))
         
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if "email" in session:
        user = row_dic["name"]
        return render_template('dashboard.html', name=user)
        
    return '''
    <style>
        .back {
            font-family: Impact, Haettenschweiler, sans-serif;
            font-size: 2rem;

        }
        .back-link {
            text-decoration: none;
            color: #0a66c2;
            font-weight: 600;
            font-size: 1rem;
            font-family: Impact, Haettenschweiler, sans-serif;
        }
        .back-link:hover {
            color: #004182;
            transition: 0.5s;
        }
    </style>

    <p class="back">Oops... <a href="/login" class=back-link>Login</a></p>
    '''


@app.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # Change this in production

# Game configuration
TARGET_WORD = "CODERS"
HINT = "Another word for PROGRAMMERS"
MAX_ATTEMPTS = 3
ATTEMPTS = 0

@app.route('/')
def home():

    return render_template('index.html', 
                         hint=HINT, 
                         attempts=ATTEMPTS,
                         max_attempts=MAX_ATTEMPTS)

@app.route('/guess', methods=['POST'])
def guess():
    global ATTEMPTS
    """Process the user's guess"""
    user_guess = request.form.get('guess', '').strip().upper()
    
    # Increment attempts
    ATTEMPTS += 1
    
    # Check if guess is correct
    if user_guess == TARGET_WORD:
        return redirect("/result/win")
    
    # Check if max attempts reached
    if ATTEMPTS >= MAX_ATTEMPTS:
        return redirect("/result/lose")
    
    # Game continues, redirect back to home
    return redirect("/")

@app.route('/result/<status>')
def result(status):
    return render_template('result.html', 
                         result=status,
                         attempts=ATTEMPTS,
                         target_word=TARGET_WORD)

@app.route('/reset')
def reset():
    global ATTEMPTS
    ATTEMPTS=0
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
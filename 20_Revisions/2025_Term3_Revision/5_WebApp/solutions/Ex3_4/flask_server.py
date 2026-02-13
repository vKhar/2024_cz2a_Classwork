from flask import Flask, render_template, request, redirect, url_for, session
import os
import hangman

app = Flask(__name__)

# Game configuration
# TARGET_WORD = "CODERS"
TARGET_WORD = ""
MAX_ATTEMPTS = 0
GUESSED=[]
ATTEMPTS = 0
GAME_OVER = False
RESULT=""

def init_globals(word_length=0):
    global TARGET_WORD, MAX_ATTEMPTS, ATTEMPTS,GAME_OVER, RESULT, GUESSED
    TARGET_WORD = hangman.getSecret(word_length)
    print(TARGET_WORD) ## cheat code
    MAX_ATTEMPTS = len(TARGET_WORD)*2
    GUESSED= hangman.cheat(TARGET_WORD)
    ATTEMPTS = 0
    GAME_OVER = False
    RESULT=""

@app.route('/', methods =['POST', 'GET'])
def home():
    # Game state initiaisation

    global TARGET_WORD, MAX_ATTEMPTS, ATTEMPTS,GAME_OVER, RESULT, GUESSED

    if request.method == "GET":
        return render_template("init.html")

    else:
        word_length = int(request.form.get("length",0))
        init_globals(word_length)
        return redirect("/start")

@app.route('/start')
def start():
    global TARGET_WORD, MAX_ATTEMPTS, ATTEMPTS, GAME_OVER, RESULT, GUESSED

    HINT = hangman.reveal(TARGET_WORD, GUESSED)
    # If game is over, redirect to result page
    if GAME_OVER :
        return redirect(url_for('result'))
    
    return render_template('index.html', 
                         hint=HINT, 
                         attempts=ATTEMPTS,
                         max_attempts=MAX_ATTEMPTS)


@app.route('/guess', methods=['POST'])
def guess():
    global ATTEMPTS, GAME_OVER, RESULT, GUESSED

    """Process the user's guess"""
    user_guess = request.form.get('guess', '').strip()
    GUESSED.append(user_guess)
    ret = hangman.reveal(TARGET_WORD, GUESSED)
    # Increment attempts
    ATTEMPTS += 1
    
    # Check if guess is correct
    if ret == TARGET_WORD:
        GAME_OVER = True
        RESULT = "win"
        return redirect(url_for('result'))
    
    # Check if max attempts reached
    if ATTEMPTS >= MAX_ATTEMPTS:
        RESULT = 'lose'
        GAME_OVER = True
        return redirect(url_for('result'))
    
    # Game continues, redirect back to home

    return redirect(url_for('start'))

@app.route('/result')
def result():
    """Display the result page"""
    if RESULT == "":
        return redirect(url_for('home'))
    
    return render_template('result.html', 
                         result=RESULT,
                         attempts=ATTEMPTS,
                         target_word=TARGET_WORD)

@app.route('/reset')
def reset():
    """Reset the game"""
    global ATTEMPTS, RESULT, GAME_OVER
    ATTEMPTS=0
    RESULT=""
    GAME_OVER=False
    return redirect(url_for('home'))

@app.route('/hitme/<arg>')
def hitme(arg):
    """Return a html form"""
    html = """
    <form action="/login" method="post">
        <label for="userid">User ID: </label><br>
        <input type="text" id="userid" name="userid"><br>
        <label for="password">Password: </label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Submit">
    </form>
    """
    return html

if __name__ == '__main__':
    app.run()
Design a web-based “Guess-the-Word” game where the user will be given a word to guess.

- The web app will randomly select a word from a file WORDS.TXT.
- The user will be shown the word with some letters hidden and given a number of attempts to guess the word.
- The number of attempts is 2 x  the word length
- The user will enter the missing letters one at a time
- If the user enter a letter that is in the word, the letter will be revealed


### Home Page ###
- This page index.html should display: 
    - The secret word with some letters revealed. 
    - A form with a text input box for the user to enter his/her guess. 
    - A submit button that sends the guess to the server using a POST request. 
    - After each guess, the server should: 
        - Compare the number of correct letters guessed so far and revealed those letters that are in the secret word
        - Track the number of attempts made by the user. 
        - Redirect the user back to the home page unless the game has ended.

### Result Page ###
 - This page result.html should display the outcome of the game: 
    - If the user managed to guess all the letters in the secret word, display a congratulatory message. 
    - If the user exhausts all his/her attempts without guessing correctly, display a game over message along with the correct word.
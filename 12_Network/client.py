## Guess Simplify Client Code (Mr Leong)
import socket, time

s = socket.socket()
s.connect(('127.0.0.1', 9999))

correct = False
while not correct :
    raw = s.recv(1024)
    code = raw.decode()
    print(f"Received {code}")

    if code == 'Low':
        print('Your guess is too low.')
    elif code== 'High':
        print('Your guess is too high.')
    elif code == 'GUESS':
        print("Guess a number between 1 to 100")
    elif code == 'Correct':
        print('You guessed correct!')
        correct = True
        break
    else:
        print(f"{code} is not recognised")
    guess = input('Enter guess (1-100): ')
    s.send(guess.encode())

s.close()

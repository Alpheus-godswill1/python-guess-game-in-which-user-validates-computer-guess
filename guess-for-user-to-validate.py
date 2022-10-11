import random 

def computerGuess(n):
    low = 1
    high = n
    feedback = ''
    while feedback != 'c':
        guessValue = random.randint(low, high)
        feedback = input(f'Is {guessValue} too low (L), or too high (H), or correct (C)???: ').lower()
        if feedback == 'h':
            feedback = guessValue - 1
        elif feedback == 'l':
            feedback = guessValue + 1
    print(f'WOW! the computer guessed the right number, {guessValue}, correctly!')
        
computerGuess(10)     

#OR This method can still work

def computerGuess(n):
    low = 1
    high = n
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high9
        feedback = input(f'Is {guess} too low (L), or too high (H), or correct (C)???: ').lower()
        if feedback == 'h':
            feedback = guess - 1
        elif feedback == 'l':
            feedback = guess + 1
    print(f'WOW! the computer guessed the right number, {guess}, correctly!')
        
computerGuess(10) 

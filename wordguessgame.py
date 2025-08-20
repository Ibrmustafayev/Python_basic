import random
word_bank=['dog', 'cat', 'lion', 'tiger', 'panda', 'zebra', 'eagle', 'shark', 'whale', 'rabbit','car', 'phone', 'computer', 'bottle', 'chair', 'table', 'lamp',
        'mirror', 'camera', 'guitar','home', 'school', 'metro', 'office', 'village', 'castle', 'forest', 'desert', 'island', 'ocean','coffee', 'pizza', 'burger',
        'pasta', 'bread', 'apple', 'banana', 'chocolate', 'milk', 'cheese','owen', 'david', 'susan', 'linda', 'maria', 'john', 'peter', 'lucas', 'sarah', 'anna',
        'python', 'java', 'binary', 'coding', 'debug', 'script', 'server', 'cloud', 'robot', 'matrix']
word=random.choice(word_bank)
guessedword=list("_"*len(word))
attempts=10
while attempts>0:
    print('\nCurrent word: '+''.join(guessedword))
    guess=input('Guess a letter: ')
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessedword[i]=guess
        print('Great guess!')
    else:
        attempts-=1
        print('Wrong guess! Attempts left: '+str(attempts))
    if '_' not in guessedword:
        print('\nCongratulations!! You guessed the word: '+word)
        break
    if attempts==0 and '_' in guessedword:
        print('\nYou failed! The word was: '+word)
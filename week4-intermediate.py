from random_word import RandomWords
r = RandomWords()

# Return a single random word
word=r.get_random_word()
used_letters=[] #list of used letters
tries=6 #number of tries
w="" #the word being guessed for display
for l in word:
    w+='_ '
while (tries>0 and w.replace(" ", "")!=word):
    print(f"You have {tries} tries left")
    print("Used letters: ", end="")
    for l in used_letters:
        print(l, end=" ") #printing the used letters
    print(f"\nWord: {w}")
    guess=input("Guess a letter: ")
    if guess not in used_letters:
        used_letters.append(guess) #prevents duplicate elements in used_letters
    if guess in word and (guess not in w): #a try will be consumed if the user guesses the correct letter for a second time
        for index in range(0, len(word)):
            if guess==word[index]:
                #change w to a list to change the display
                l_string=list(w)
                l_string[index*2]=guess
                w="".join(l_string)
                if (w.replace(" ", "")==word):
                    print(f"You guessed the word '{word}'")
                    break
    else:
        tries-=1
    if (tries==0):
        print(f"Game over! The word was {word}")
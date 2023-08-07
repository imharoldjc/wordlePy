import random

# choose word
f = open('wordle-answers-alphabetical.txt')
answerbank = f.read().splitlines()
f.close()

# allowed guesses
f = open('allowedguesses.txt')
guessbank = f.read().splitlines() + answerbank
f.close()


playAgain = True
while playAgain:  # start game loop
    print("*** W O R D L E ***")

    tries = 0
    feedback = ''
    solution = random.choice(answerbank) # this game's word

    while tries < 6:  # <= 5 tries

        tries += 1  # current try number
        attempt = "" # player's input

        # Check if attempt is valid. Prompt for attempt until a valid attempt entered.
        while len(attempt) != 5 or attempt.isalpha() != True or attempt not in guessbank:
            attempt = (input("Attempt " + str(tries) + "/6: ")).lower()
            if len(attempt) != 5:
                print('Must enter a five-letter word.')
            if attempt.isalpha() != True:
                print('All characters must be in the alphabet. (a-z, A-Z)')
            if attempt not in guessbank:
                print('Not in word list.\n')

        if attempt == solution:
            print("CORRECT!\n")
            break

        # Generate feedback output # could use slices? or smth instead of making a list #hashmap?
        feedback = list(attempt)  # Feedback output
        #print(attempt) attempt wasnt turned into a list
        solutionArr = list(solution) # Copy of solution in list form for comparison to attempt

        # Check for correct characters
        for i in range(len(attempt)):
            if attempt[i] == solution[i]:
                solutionArr[i] = 'found'

        # Generate attempt feedback
        for i in range(len(attempt)):  # for each letter
            letterCount = solutionArr.count(attempt[i])

            # Letter in answer but in wrong place
            if letterCount > 0 and feedback.count("*" + attempt[i] + "*") < letterCount and solutionArr[i] != 'found':
                feedback[i] = "*" + attempt[i] + "*"

            # Letter not in answer at all or too many of that letter
            elif solutionArr[i] != 'found':
                feedback[i] = "-" + attempt[i] + "-"

        print(("  ".join(feedback)).upper(), "\n")


    if attempt != solution:
        print("OUT OF TRIES! ANSWER: " + solution)

    playAgain = input("Enter y/Y to play again, anything else to quit: ").lower()
    print("\n")

    if playAgain != 'y':
       break

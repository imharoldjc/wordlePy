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
while playAgain:
    print("*** W O R D L E ***")

    tries = 0
    validation = ''
    solution = random.choice(answerbank)

    while tries < 6:

        tries += 1
        attempt = ""

        # Check if attempt is valid.
        while len(attempt) != 5 or attempt.isalpha() != True or attempt not in guessbank:
            attempt = (input("Attempt " + str(tries) + "/6: ")).lower()
            if attempt not in guessbank:
                print('Not in word list.\n')

        if attempt == solution:
            print("CORRECT!\n")
            break

        validation = list(attempt)  # Feedback output
        solutionArr = list(solution) # Copy of solution in list form

        # Check for correct characters
        for i in range(len(attempt)):
            if attempt[i] == solution[i]:
                solutionArr[i] = 'found'

        # Generate attempt feedback
        for i in range(len(attempt)):
            letterCount = solutionArr.count(attempt[i])

            # Letter in answer but in wrong place
            if letterCount > 0 and validation.count("*" + attempt[i] + "*") < letterCount and solutionArr[i] != 'found':
                validation[i] = "*" + attempt[i] + "*"

            # Letter not in answer at all or too many of that letter
            elif solutionArr[i] != 'found':
                validation[i] = "-" + attempt[i] + "-"

        print(("  ".join(validation)).upper(), "\n")


    if attempt != solution:
        print("OUT OF TRIES! ANSWER: " + solution)

    playAgain = input("Enter y/Y to play again, anything else to quit: ").lower()
    print("\n")

    if playAgain != 'y':
       break

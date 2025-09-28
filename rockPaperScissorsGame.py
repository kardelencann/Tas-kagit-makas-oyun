import random

numberRound = 0  # tur sayısını belirtir.

userPoint = 0  # oyuncunun kazandığı maç sayısını gösterir.

computerPoint = 0  # bilgisayarın kazandığı maç sayısını gösterir.

choice = 0  # menüde yapılan seçim işlemi


def computerChoice():  # bilgisayar 3 değerden random değer döndürür.
    return random.choice(["rock", "paper", "scissors"])


def reset():  # değerleri sıfırlar.
    global userPoint, computerPoint, numberRound
    userPoint = 0
    computerPoint = 0
    numberRound = 0


def game():
    global userPoint, computerPoint, numberRound

    while numberRound < 8:
        numberRound += 1
        print("***********************************")
        print(f"Number of rounds: {numberRound} ")
        print(f"The number of matches you won: {userPoint} ")
        print(f"The number of matches computer: {computerPoint}")
        answer = input("Can you choose between rock, paper or scissors?").lower()

        if answer not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Play try again.")
            return

        computer_choice = computerChoice()

        if computer_choice == "rock" and answer == "scissors":
            print(f"You lose.The computer choice {computer_choice}. Try again.")
            computerPoint += 1

        elif computer_choice == "rock" and answer == "paper":
            print(f"You win.The computer choice {computer_choice}.")
            userPoint += 1

        elif computer_choice == "paper" and answer == "rock":
            print(f"You lose.The computer choice {computer_choice}. Try again.")
            computerPoint += 1

        elif computer_choice == "paper" and answer == "scissors":
            print(f"You win.The computer choice {computer_choice}.")
            userPoint += 1

        elif computer_choice == "scissors" and answer == "paper":
            print(f"You lose.The computer choice {computer_choice}. Try again.")
            computerPoint += 1

        elif computer_choice == "scissors" and answer == "rock":
            print(f"You win.The computer choice {computer_choice}. Try again.")
            userPoint += 1

        elif computer_choice == answer:
            print("Same valid.Try again!")

        if userPoint == 2:
            print("***********************************")
            print("*****You win, congratulations!*****")
            print("***********************************")
            break

        elif computerPoint == 2:
            print("***********************************")
            print("****You lose,the computer won!*****")
            print("***********************************")
            break


def menu():
    while True:
        try:
            reset()
            print("***********************************")
            print("Welcome to Rock Paper Scissors Game!")
            print("The game ends in three rounds; the one who gets it right twice wins.")
            print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
            print("***********************************")
            print("1.Play start")
            print("2.Exited")
            print("***********************************")

            choice = int(input("Choice:"))

            if choice == 1:
                game()

            elif choice == 2:
                print("Exit is in progress!")
                break

        except ValueError:
            print("Please enter a valid number (1, 2 or 3).")
        result = int(input("If you want to continue: click 1, if you don't: click 2:"))

        if result == 1:
            menu()
        else:
            break


while True:
    menu()
    break

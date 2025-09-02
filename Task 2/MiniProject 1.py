def get_fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

# Two-player Fizz Buzz game
player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

players = [player1, player2]
turn = 0  # 0 = player1, 1 = player2

for i in range(1, 101):
    current_player = players[turn % 2]
    answer = input(f"{current_player}'s turn for {i}: ").strip() 
    correct_value = get_fizz_buzz(i)
    
    if answer != correct_value:
        print(f"Wrong! Correct answer was '{correct_value}'. {current_player} is out!")
        break  # Game ends
    turn += 1
else:
    print("Congratulations! Both players completed 100 rounds correctly!")

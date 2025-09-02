import random

def get_fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

# Two-player Fizz Buzz with random numbers + sum of last two
player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

players = [player1, player2]
turn = 0  # 0 = player1, 1 = player2

previous_numbers = []  # store last two random numbers

for round_num in range(1, 11):  #10 rounds
    current_player = players[turn % 2]

    # Generate random number between 1 and 20 
    number = random.randint(1, 20)
    fizzbuzz_value = get_fizz_buzz(number)

    # Check if we have at least 2 previous numbers
    if len(previous_numbers) >= 2:
        prev_sum = previous_numbers[-1] + previous_numbers[-2]
        correct_value = f"{fizzbuzz_value} {prev_sum}"
    else:
        correct_value = fizzbuzz_value

    answer = input(f"{current_player}'s turn for number {number}: ").strip()

    if answer != correct_value:
        print(f"Wrong! Correct answer was '{correct_value}'. {current_player} is out!")
        break  # Game ends

    # Save this number for future sums
    previous_numbers.append(number)
    turn += 1
else:
    print("Congratulations! Both players completed all rounds correctly!")

def luhn_algorithm(card_number: str) -> bool:
    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Double every second digit, by index like  1 3 5
        if i % 2 == 1:
            n = n * 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
# card number  testing
card = "45395787313621486"  
if luhn_algorithm(card):
    print("valid card number")
else:
    print("invalid card number")

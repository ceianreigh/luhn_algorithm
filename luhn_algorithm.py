# validating atm card number with luhn algorithm
def verify_card_number(card_number):
    # reverse the card number
    reversed_card_number = card_number[::-1]

    # separate the odd and even digits
    odd_digits = reversed_card_number[::2]
    even_digits = reversed_card_number[1::2]

    # add the odd digits
    sum_odd = 0
    for digits in odd_digits:
        sum_odd += int(digits)

    # add the even digits
    sum_even = 0
    for digits in even_digits:
        # double the digit
        number = int(digits) * 2
        # if the result is 10 or more, sum the digits
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_even += number

def main():
    card_number = input("Enter card number: ")

    # remove spaces and hyphens from card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

main()
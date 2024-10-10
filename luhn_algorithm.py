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


def main():
    card_number = input("Enter card number: ")

    # remove spaces and hyphens from card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

main()
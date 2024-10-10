# validating atm card number with luhn algorithm
def verify_card_number(card_number):
    reversed_card_number = card_number[::-1]


def main():
    card_number = input("Enter card number: ")

    # remove spaces and hyphens from card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

main()
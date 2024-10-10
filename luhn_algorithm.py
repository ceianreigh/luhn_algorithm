# validating atm card number with luhn algorithm


def main():
    card_number = input("Enter card number: ")
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

main()
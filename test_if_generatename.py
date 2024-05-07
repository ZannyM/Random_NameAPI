import random

def read_names_from_file(file_path):
    with open(file_path, 'r') as file:
        names = file.read().strip().split(', ')
    return names

def get_names_by_letter(names, letter):
    letter_names = [name for name in names if name.startswith(letter.upper())]
    return letter_names

def get_random_name(names):
    if names:
        return random.choice(names)
    else:
        return None

def main():
    file_path = 'namedata.txt'
    all_names = read_names_from_file(file_path)

    while True:
        user_input = input("Enter a letter (or 'q' to quit): ").lower()
        if user_input == 'q':
            break

        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        names_by_letter = get_names_by_letter(all_names, user_input)
        if names_by_letter:
            random_name = get_random_name(names_by_letter)
            print(f"Random name starting with '{user_input.upper()}': {random_name}")
        else:
            print(f"No names found starting with '{user_input.upper()}'.")

if __name__ == "__main__":
    main()

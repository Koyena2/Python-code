import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Silly", "Brave", "Clever", "Swift", "Bright", "Jolly", "Witty", "Funky"]
nouns = ["Tiger", "Dragon", "Eagle", "Shark", "Panther", "Wolf", "Hawk", "Lion", "Falcon", "Bear"]

# Function to generate a random username
def generate_username(include_numbers, include_special, length=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)

    username = adj + noun

    if include_numbers:
        username += str(random.randint(0, 999))
    if include_special:
        username += random.choice(string.punctuation)

    if length:
        username = username[:length]

    return username

# Function to save usernames to a file
def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, 'w') as file:
        for username in usernames:
            file.write(username + "\n")

# Interactive user input
def main():
    print("Welcome to the Username Generator!")
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    length = input("Set a specific length? (Enter a number or leave blank for no limit): ").strip()
    length = int(length) if length.isdigit() else None

    count = int(input("How many usernames would you like to generate?: "))

    usernames = [generate_username(include_numbers, include_special, length) for _ in range(count)]

    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    save_option = input("Would you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        filename = input("Enter the filename (default 'usernames.txt'): ").strip() or "usernames.txt"
        save_usernames_to_file(usernames, filename)
        print(f"Usernames saved to {filename}")

if __name__ == "__main__":
    main()

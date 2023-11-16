import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):
    # Define character sets based on complexity requirements
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets based on complexity requirements
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Ensure the password length is at least 1
    length = max(1, length)

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    # Get user input for password parameters
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, include_uppercase, include_digits, include_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

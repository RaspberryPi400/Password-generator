import secrets
import string

x = int(input("How long should your password be? "))

def generate_strong_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password_list = []

    # Ensure at least one of each character type
    password_list.append(secrets.choice(string.ascii_lowercase))
    password_list.append(secrets.choice(string.ascii_uppercase))
    password_list.append(secrets.choice(string.digits))
    password_list.append(secrets.choice(string.punctuation))

    # Fill the rest
    for _ in range(length - 4):
        password_list.append(secrets.choice(all_characters))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)

new_password = generate_strong_password(x)
print(f"Generated Password: {new_password}")

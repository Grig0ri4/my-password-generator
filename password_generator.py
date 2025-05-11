<<<<<<< HEAD
import random
import string
import secrets
import os

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов!")

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Необходимо выбрать хотя бы один набор символов!")

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    strength = sum([has_upper, has_lower, has_digit, has_special])
    if len(password) < 8:
        return "Слабый (слишком короткий)"
    elif strength < 3:
        return "Слабый (мало разных типов символов)"
    elif strength == 3:
        return "Средний"
    else:
        return "Сильный"

def save_password_to_file(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Пароль сохранен в файл {filename}")

def main():
    print("=== Генератор паролей ===")
    
    while True:
        try:
            length = int(input("Введите длину пароля (минимум 4 символа): "))
            break
        except ValueError:
            print("Пожалуйста, введите число!")

    use_uppercase = input("Использовать заглавные буквы? (да/нет): ").lower() == "да"
    use_lowercase = input("Использовать строчные буквы? (да/нет): ").lower() == "да"
    use_digits = input("Использовать цифры? (да/нет): ").lower() == "да"
    use_special = input("Использовать специальные символы? (да/нет): ").lower() == "да"

    try:
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_digits=use_digits,
            use_special=use_special
        )
        
        print(f"\nВаш сгенерированный пароль: {password}")
        
        strength = check_password_strength(password)
        print(f"Надежность пароля: {strength}")
        
        save = input("Сохранить пароль в файл? (да/нет): ").lower() == "да"
        if save:
            save_password_to_file(password)

    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
=======
import random
import string
import secrets
import os

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов!")

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Необходимо выбрать хотя бы один набор символов!")

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    strength = sum([has_upper, has_lower, has_digit, has_special])
    if len(password) < 8:
        return "Слабый (слишком короткий)"
    elif strength < 3:
        return "Слабый (мало разных типов символов)"
    elif strength == 3:
        return "Средний"
    else:
        return "Сильный"

def save_password_to_file(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Пароль сохранен в файл {filename}")

def main():
    print("=== Генератор паролей ===")
    
    while True:
        try:
            length = int(input("Введите длину пароля (минимум 4 символа): "))
            break
        except ValueError:
            print("Пожалуйста, введите число!")

    use_uppercase = input("Использовать заглавные буквы? (да/нет): ").lower() == "да"
    use_lowercase = input("Использовать строчные буквы? (да/нет): ").lower() == "да"
    use_digits = input("Использовать цифры? (да/нет): ").lower() == "да"
    use_special = input("Использовать специальные символы? (да/нет): ").lower() == "да"

    try:
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_digits=use_digits,
            use_special=use_special
        )
        
        print(f"\nВаш сгенерированный пароль: {password}")
        
        strength = check_password_strength(password)
        print(f"Надежность пароля: {strength}")
        
        save = input("Сохранить пароль в файл? (да/нет): ").lower() == "да"
        if save:
            save_password_to_file(password)

    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
>>>>>>> 1adfd13 (Add folders and files)
    main()
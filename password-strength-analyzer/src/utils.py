def is_strong(password: str) -> bool:
    return len(password) >= 12 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in "!@#$%^&*()-_+=<>?" for char in password)

def is_medium(password: str) -> bool:
    return len(password) >= 8 and (any(char.isdigit() for char in password) or any(char.isupper() for char in password))

def calculate_strength(password: str) -> int:
    if is_strong(password):
        return 3
    elif is_medium(password):
        return 2
    else:
        return 1
def analyze_password(password: str) -> str:
    if is_strong(password):
        return "Uiiii, que fortão"
    elif is_medium(password):
        return "Ehh.... OK... mas melhore...."
    else:
        return "ATUALIZE!!!"

def is_strong(password: str) -> bool:
    return len(password) >= 12 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in "!@#$%^&*()-_+=<>?" for char in password)

def is_medium(password: str) -> bool:
    return len(password) >= 8 and (any(char.isdigit() for char in password) or any(char.isupper() for char in password))

def calculate_strength(password: str) -> int:
    strength = 0
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_+=<>?" for char in password):
        strength += 1
    return strength
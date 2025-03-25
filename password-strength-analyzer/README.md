# Password Strength Analyzer

This project is a simple password strength analyzer that evaluates the strength of a given password and provides feedback based on its strength.

## Features

- Analyzes password strength and categorizes it as weak, medium, or strong.
- Provides user-friendly messages for each category.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd password-strength-analyzer
pip install -r requirements.txt
```

## Usage

You can use the password strength analyzer by importing the `analyze_password` function from the `analyzer` module.

### Example

```python
from src.analyzer import analyze_password

password = "your_password_here"
result = analyze_password(password)
print(result)
```

## Password Strength Criteria

- **Weak Passwords**: Passwords that do not meet the minimum strength requirements.
- **Medium Passwords**: Passwords that are somewhat secure but could be improved.
- **Strong Passwords**: Passwords that are complex and secure.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
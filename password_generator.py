import secrets
import string

def generate_password(length=15):
    """Generate a secure random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Generate and display a strong password
print("Generated Password:", generate_password(16))
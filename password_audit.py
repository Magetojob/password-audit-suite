import hashlib
import string
from datetime import datetime


# --------------------------------------------------
# HASH A PASSWORD
# --------------------------------------------------

def hash_password(password, algorithm):
    """Hash a password using the selected algorithm."""

    password_bytes = password.encode("utf-8")

    if algorithm == "md5":
        return hashlib.md5(password_bytes).hexdigest()

    elif algorithm == "sha1":
        return hashlib.sha1(password_bytes).hexdigest()

    elif algorithm == "sha256":
        return hashlib.sha256(password_bytes).hexdigest()

    elif algorithm == "sha512":
        return hashlib.sha512(password_bytes).hexdigest()

    return None


# --------------------------------------------------
# PASSWORD STRENGTH CHECKER
# --------------------------------------------------

def check_password_strength(password):
    """Calculate password strength."""

    upper_case = any(c in string.ascii_uppercase for c in password)
    lower_case = any(c in string.ascii_lowercase for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c in string.digits for c in password)

    character_types = [
        upper_case,
        lower_case,
        special,
        digits
    ]

    length = len(password)
    score = 0

    # Load common passwords
    try:
        with open("common.txt", "r") as file:
            common = file.read().splitlines()

    except FileNotFoundError:
        common = []

    # Check if password is common
    if password in common:
        return {
            "length": length,
            "character_types": sum(character_types),
            "score": 0,
            "strength": "Weak",
            "common": True
        }

    # Length scoring
    if length > 8:
        score += 1

    if length > 12:
        score += 1

    if length > 17:
        score += 1

    if length > 20:
        score += 1

    # Character type scoring
    types = sum(character_types)

    if types > 1:
        score += 1

    if types > 2:
        score += 1

    if types > 3:
        score += 1

    # Determine strength
    if score < 4:
        strength = "Weak"

    elif score == 4:
        strength = "Okay"

    elif score < 6:
        strength = "Pretty Good"

    else:
        strength = "Strong"

    return {
        "length": length,
        "character_types": types,
        "score": score,
        "strength": strength,
        "common": False
    }


def password_strength():
    """Ask the user for a password and display its strength."""

    password = input("\nEnter password to check: ")

    result = check_password_strength(password)

    print("\n========== PASSWORD STRENGTH ==========")

    print(f"Password length: {result['length']}")
    print(f"Character types: {result['character_types']}")
    print(f"Score: {result['score']} / 7")
    print(f"Strength: {result['strength']}")

    if result["common"]:
        print("Warning: Password was found in common.txt.")

    print("=======================================")


# --------------------------------------------------
# HASH GENERATOR
# --------------------------------------------------

def generate_hash():
    """Generate a hash using the selected algorithm."""

    password = input("\nEnter password to hash: ")

    print("\nChoose hashing algorithm:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")

    choice = input("Enter choice: ")

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha512"
    }

    algorithm = algorithms.get(choice)

    if algorithm is None:
        print("\nInvalid choice.")
        return

    digest = hash_password(password, algorithm)

    print("\n========== HASH RESULT ==========")
    print(f"Algorithm: {algorithm.upper()}")
    print(f"Hash: {digest}")
    print("=================================")


# --------------------------------------------------
# HASH CHECKER
# --------------------------------------------------

def crack_hash(input_hash, algorithm):
    """Check a hash against the local common.txt wordlist."""

    try:
        pass_file = open("common.txt", "r")

    except FileNotFoundError:
        print("\nCould not find common.txt.")
        print("Make sure common.txt is in the same folder.")
        return False, None

    print("\nChecking local wordlist...")

    for password in pass_file:

        password = password.strip()

        digest = hash_password(password, algorithm)

        if digest == input_hash:

            pass_file.close()

            print("\nPassword Found!")
            print(f"Password: {password}")

            return True, password

    pass_file.close()

    print("\nPassword was not found in the wordlist.")

    return False, None


def hash_checker():
    """Ask for a hash and check it against common.txt."""

    input_hash = input("\nEnter the hash to check: ").strip()

    print("\nChoose hashing algorithm:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")

    choice = input("Enter choice: ")

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha512"
    }

    algorithm = algorithms.get(choice)

    if algorithm is None:
        print("\nInvalid choice.")
        return

    print(f"\nSelected algorithm: {algorithm.upper()}")

    crack_hash(input_hash, algorithm)


# --------------------------------------------------
# REPORT GENERATOR
# --------------------------------------------------

def generate_report():
    """Generate a password audit report."""

    print("\n========== REPORT GENERATOR ==========")

    password = input("Enter password to audit: ")

    # Strength analysis
    strength = check_password_strength(password)

    # Generate hashes
    md5_hash = hash_password(password, "md5")
    sha1_hash = hash_password(password, "sha1")
    sha256_hash = hash_password(password, "sha256")
    sha512_hash = hash_password(password, "sha512")

    # Current date/time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create report
    report = f"""
========================================
          PASSWORD AUDIT REPORT
========================================

Date: {current_time}

--------------- STRENGTH ---------------

Password Length: {strength['length']}
Character Types: {strength['character_types']}
Score: {strength['score']} / 7
Strength: {strength['strength']}

Common Password Check:
{"FOUND in common.txt" if strength['common'] else "Not found in common.txt"}

---------------- HASHES ----------------

MD5:
{md5_hash}

SHA1:
{sha1_hash}

SHA256:
{sha256_hash}

SHA512:
{sha512_hash}

========================================
             END OF REPORT
========================================
"""

    # Save report
    filename = "password_audit_report.txt"

    try:
        with open(filename, "w") as file:
            file.write(report)

        print("\nReport generated successfully!")
        print(f"Saved as: {filename}")

    except OSError as error:
        print("\nCould not create report.")
        print(f"Error: {error}")


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():

    while True:

        print("\n")
        print("========================================")
        print("          PASSWORD AUDIT SUITE")
        print("========================================")

        print("1. Generate password hash")
        print("2. Check password strength")
        print("3. Check hash against wordlist")
        print("4. Generate audit report")
        print("5. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            generate_hash()

        elif choice == "2":
            password_strength()

        elif choice == "3":
            hash_checker()

        elif choice == "4":
            generate_report()

        elif choice == "5":
            print("\nExiting Password Audit Suite...")
            break

        else:
            print("\nInvalid option. Please choose 1-5.")


# --------------------------------------------------
# START PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()
import re


def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = {
        "Length (at least 8 characters)": length_criteria,
        "Uppercase letters": uppercase_criteria,
        "Lowercase letters": lowercase_criteria,
        "Numbers": number_criteria,
        "Special characters": special_char_criteria,
    }

    score = sum(criteria_met.values())

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "Strength": strength,
        "Criteria Met": criteria_met,
    }

    return feedback


# Example usage
password = input("Enter a password to assess its strength: ")
feedback = assess_password_strength(password)

print("Password Strength:", feedback["Strength"])
print("Criteria Met:")
for criterion, met in feedback["Criteria Met"].items():
    print(f" - {criterion}: {'Yes' if met else 'No'}")

"""task3:bulid a tool that assesses the strength of a password based on criteria such as length , presence of uppercase and lowercase letter numbers and secial charecters."""
import re
import string

def assess_password_strength(password):
    """Assess password strength based on multiple criteria."""
    score = 0
    feedback = []
    recommendations = []

    # Criterion 1: Length
    if len(password) >= 12:
        score += 4
        feedback.append("Length: Excellent (12+ characters)")
    elif len(password) >= 8:
        score += 3
        feedback.append("Length: Good (8-11 characters)")
    elif len(password) >= 6:
        score += 1
        feedback.append("Length: Weak (6-7 characters)")
    else:
        feedback.append("Length: Poor (<6 characters)")
        recommendations.append("Use at least 8 characters, ideally 12 or more.")

    # Criterion 2: Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 2
        feedback.append("Uppercase letters: Present")
    else:
        feedback.append("Uppercase letters: Missing")
        recommendations.append("Add uppercase letters (e.g., A, B, C).")

    # Criterion 3: Lowercase letters
    if re.search(r'[a-z]', password):
        score += 2
        feedback.append("Lowercase letters: Present")
    else:
        feedback.append("Lowercase letters: Missing")
        recommendations.append("Add lowercase letters (e.g., a, b, c).")

    # Criterion 4: Numbers
    if re.search(r'[0-9]', password):
        score += 2
        feedback.append("Numbers: Present")
    else:
        feedback.append("Numbers: Missing")
        recommendations.append("Add numbers (e.g., 1, 2, 3).")

    # Criterion 5: Special characters
    special_chars = set(string.punctuation)
    if any(char in special_chars for char in password):
        score += 2
        feedback.append("Special characters: Present")
    else:
        feedback.append("Special characters: Missing")
        recommendations.append("Add special characters (e.g., !, @, #).")

    # Criterion 6: No repeated characters
    if len(password) == len(set(password)):
        score += 1
        feedback.append("Repeated characters: None")
    else:
        feedback.append("Repeated characters: Present")
        recommendations.append("Avoid repeated characters for better uniqueness.")

    # Determine strength
    if score >= 12:
        strength = "Very Strong"
    elif score >= 9:
        strength = "Strong"
    elif score >= 6:
        strength = "Moderate"
    elif score >= 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "recommendations": recommendations
    }

def main():
    print("Password Strength Checker")
    print("Enter a password to assess its strength (or 'quit' to exit)")
    
    while True:
        password = input("\nEnter password: ")
        if password.lower() == 'quit':
            print("Exiting program...")
            break
        
        if not password:
            print("Error: Password cannot be empty.")
            continue

        result = assess_password_strength(password)
        
        print(f"\nPassword Strength: {result['strength']} (Score: {result['score']}/13)")
        print("Feedback:")
        for item in result['feedback']:
            print(f"- {item}")
        
        if result['recommendations']:
            print("\nRecommendations:")
            for item in result['recommendations']:
                print(f"- {item}")
        else:
            print("\nNo recommendations needed: Your password is strong!")

if __name__ == "__main__":
    main()

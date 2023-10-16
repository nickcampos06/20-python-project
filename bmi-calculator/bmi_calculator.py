def main():
    user_weight, user_height = get_user_data()
    user_bmi = calculate_bmi(user_weight, user_height)
    print(f'Your BMI is: {user_bmi:.2f}')
    user_category = get_user_category(user_bmi)
    print("Category:", user_category)

def get_user_data():
    user_weight = float(input('Enter your weight (kg): '))
    user_height = float(input('Enter your height (m): '))
    return user_weight, user_height

def calculate_bmi(user_weight, user_height):
    user_bmi = user_weight / (user_height ** 2)
    return user_bmi

def get_user_category(user_bmi):
    if user_bmi < 18.5:
        user_category = 'Underweight'
    elif user_bmi < 25:
        user_category = 'Normal '
    elif user_bmi < 30:
        user_category = 'Overweight'
    else:
        user_category = 'Obesity'
    return user_category

if __name__ == '__main__':
    main()
def BMI_Calc(height, weight):
    height = height / 100
    BMI = weight / height ** 2

    if BMI < 18.5:
        feedback = "Underweight"
    elif 18.5 <= BMI <= 24.9:
        feedback = "Normal"
    elif 25 <= BMI <= 30:
        feedback = "Overweight"
    elif BMI > 30:
        feedback = "Obese"

    return f'Score is {BMI:.1f}. You are {feedback}'


height = int(input())
weight = int(input())
print(BMI_Calc(height, weight))

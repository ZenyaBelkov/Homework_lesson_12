# TASK1
print("Task 1 \n")

try:
    mass = float(input("Enter your mass in kilograms: "))
    if mass == 0:
        raise ValueError
    height = float(input("Enter your height in meters: "))
    imt = mass / (height ** 2)
    if imt <= 15.99:
        print(f"Your imt = {imt}. Severe underweight. Need urgent expert advice \n")
    elif 16 <= imt <= 18.49:
        print(f"Your imt = {imt}. Insufficient (deficit) body weight. Need expert advice \n")
    elif 18.50 <= imt <= 24.99:
        print(f"Your imt = {imt}. Norm \n")
    elif 25 <= imt <= 29.99:
        print(f"Your imt = {imt}. Overweight (pre-obesity). Need expert advice \n")
    elif 30 <= imt <= 34.99:
        print(f"Your imt = {imt}. Obesity of the first degree. Need expert advice \n")
    elif 35 <= imt <= 39.99:
        print(f"Your imt = {imt}. Obesity of the second degree. Need expert advice \n")
    elif imt >= 40:
        print(f"Your imt = {imt}. Obesity of the third degree (morbid). Need urgent expert advice \n")
except ZeroDivisionError:
    print("You can't divide on 0. Your height and mass must be more than 0 \n")
except ValueError:
    print("Your values must be numbers and more than 0 \n")

# TASK2
print("Task 2 \n")


class Calculator:

    result = 0

    def __init__(self, val_1, sign, val_2):
        self.val_1 = val_1
        self.sign = sign
        self.val_2 = val_2

    def operations(self):

        try:
            if self.sign == '+':
                result = self.val_1 + self.val_2
                return result
            elif self.sign == '-':
                result = self.val_1 - self.val_2
                return result
            elif self.sign == '*':
                result = self.val_1 * self.val_2
                return result
            elif self.sign == '/':
                result = self.val_1 / self.val_2
                return result
            elif self.sign == '%':
                result = self.val_1 % self.val_2
                return result
            else:
                raise ValueError("Your sign must be + - * / % \n")
        except ZeroDivisionError:
            print("You can't divide on 0 \n")
        except ValueError as error:
            return str(error)


try:
    num_1 = float(input("Enter the first number: "))
    operation = input("Enter the math operation + - * / %: ")
    num_2 = float(input("Enter the second number: "))
    res_value = Calculator(num_1, operation, num_2)
    print(res_value.operations())
except ValueError:
    print("Your values must be numbers \n")

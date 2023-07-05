# TASK1
print("Task 1 \n")

imt_boarder_lowest = 15.99
imt_boarder_low_1 = 16
imt_boarder_low_2 = 18.50
imt_boarder_low_3 = 25
imt_boarder_low_4 = 30
imt_boarder_low_5 = 35
imt_boarder_high_1 = 18.49
imt_boarder_high_2 = 24.99
imt_boarder_high_3 = 29.99
imt_boarder_high_4 = 34.99
imt_boarder_high_5 = 39.99
imt_boarder_highest = 40

try:
    mass = float(input("Enter your mass in kilograms: "))
    if mass == 0:
        raise ValueError
    height = float(input("Enter your height in meters: "))
    imt = mass / (height ** 2)
    if imt <= imt_boarder_lowest:
        print(f"Your imt = {imt}. Severe underweight. Need urgent expert advice \n")
    elif imt_boarder_low_1 <= imt <= imt_boarder_high_1:
        print(f"Your imt = {imt}. Insufficient (deficit) body weight. Need expert advice \n")
    elif imt_boarder_low_2 <= imt <= imt_boarder_high_2:
        print(f"Your imt = {imt}. Norm \n")
    elif imt_boarder_low_3 <= imt <= imt_boarder_high_3:
        print(f"Your imt = {imt}. Overweight (pre-obesity). Need expert advice \n")
    elif imt_boarder_low_4 <= imt <= imt_boarder_high_4:
        print(f"Your imt = {imt}. Obesity of the first degree. Need expert advice \n")
    elif imt_boarder_low_5 <= imt <= imt_boarder_high_5:
        print(f"Your imt = {imt}. Obesity of the second degree. Need expert advice \n")
    elif imt >= imt_boarder_highest:
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

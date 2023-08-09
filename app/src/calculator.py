class Calculator():
    def add(self, num1, num2):
        return num1 + num2

    def substract(self, num1, num2):
        return num1 - num2
 
    def multiply(self, num1, num2):
        return num1 * num2

    def devide(self, num1, num2):
        if num2 > 0:
            return num1 / num2
        else:
            return False 


if __name__ == "__main__":
    cal = Calculator()
    print(cal.add(1, 3))
    print(cal.devide(10, 0))
    print(cal.devide(10, 2))

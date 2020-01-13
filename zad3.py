import pdb

class Calculator:
    def convert(self, number):
        aNumber = []
        reverse_number = number[::-1]
        for char in reverse_number:
            aNumber.append(char)
        
        return list(map(int, aNumber))

    def decode(self, number):
        decoded_number = ""
        reverse_number = number[::-1]
        for number in reverse_number:
            decoded_number += str(number)
        
        decoded_number = int(decoded_number)
        return decoded_number


    def add(self, A, B):
        tmp = len(A)
        if len(A) != len(B):
            tmp = max(len(A), len(B))
        for i in range(len(A), tmp+1, 1):
            A.append(0)
        for i in range(len(B), tmp+1, 1):
            B.append(0)
        result = []

        for i in range(tmp+1):
            result.append(0)

        for i in range(tmp):
            sum = result[i] + A[i] + B[i]
            result[i] = sum%10
            if sum >= 10:
                result[i+1] = sum - (sum -1)
        
        j = len(result) - 1
        while(result[j] == 0):
            result.pop(j)
            j -= 1
        return result

    def substract(self, A, B):
        pass
    
    def multiply(self, A, B):
        pass

    def divide(self, A, B):
        pass

if __name__ == '__main__':
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")

    calc = Calculator()
    num1 = calc.convert(number1)
    num2 = calc.convert(number2)
    result = calc.add(num1, num2)
    print(calc.decode(result))

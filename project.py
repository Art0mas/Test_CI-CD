def Add(a, b):
    return a + b

def Factorial(n):
    if n < 0: raise ValueError("Negative number not allowed")
    result = 1
    for i in range(1, n + 1): result *= i
    return result

def Average(numbers):
    if not numbers: return 0
    return sum(numbers) / len(numbers)

def Reverse_text(text):
    return text[::-1]

if __name__ == "__main__":
    print(f"1. 2 + 3 = {Add(2, 3)}")
    print(f"2. 5! = {Factorial(5)}")
    print(f"3. Average of list = {Average([1,2,3,4,5])}")
    print(f"4. Reversed text: {Reverse_text('Python')}")

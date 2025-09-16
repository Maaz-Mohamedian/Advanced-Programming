try: 
   a = float(input("Enter first number: "))
   b = float(input("Enter second number: "))

   print(f"Sum: {a + b} ")
   print(f"difference: {a - b} ")
   print(f"product: {a * b} ")

   if b != 0:
     print(f"Division: {a / b:.2f}")
   else:
     print("Error: Division by zero is not allowed.")

except ValueError:
    print("invalid input. Plases enter numeric values.")

numbers = [12, 5, 8, 22, 7, 19, 30, 4, 10, 16]

print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

num_set = set(numbers)
print("Orignal List:", numbers)
print("Converted set:", num_set)

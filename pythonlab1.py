try: 
   a = float(input("Enter first number: "))
   b = float(input("Enter secind number: "))

  print(f"Sum: {a + b} ")
  print(f"difference: {a - b} ")
  print(f"product: {a * b} ")

  if b != 0:
     print(f"Division: {a / b:.2f}")
  else:
     print("Error: Division by zero is not allowed.")

except ValueError:
    print("invalid input. Plases enter numeric values.")

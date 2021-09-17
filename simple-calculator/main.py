import art

def add(a,b):
  return a + b
def substraction(a,b):
  return a - b
def multiplication(a,b):
  return a * b
def division(a,b):
  return a / b

operations = {
  "+" : add,
  "-" : substraction,
  "*" : multiplication,
  "/" : division,
}

def calculation_function(a,b):
    for operation in operations:
      print(operation)
    operation_char = input("Pick an operation from the list above: ")
    calculation = operations[operation_char](a, b)
    print(f"{a} {operation_char} {b} = {calculation}")
    return calculation

def calculation():
  print(art.logo)
  num1 = float(input("What is your first number? "))
  num2 = float(input("What is your second number? "))
  first_operation = calculation_function(num1, num2)

  next_move = True  
  while True:
    next_operation = input(f'Type y to continue calculating with answer {first_operation}, type n to  start a new calculation: ')
    if next_operation == "n":
      next_move = False
      calculation()
    else:       
      next_number = float(input("What is your next number? "))
      next_operation_result = calculation_function(first_operation, next_number)
      first_operation = next_operation_result
      
calculation()
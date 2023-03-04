# An example of a syntax error in code could be a missing semicolon
def print_hello():
  #print("Hello)
  return

print_hello()

# An example of a runtime error in code could be a null reference
def divide(a, b):
  return a / b

divide(10, 0)
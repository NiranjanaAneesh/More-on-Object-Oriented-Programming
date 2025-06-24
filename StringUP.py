class string():
 def __init__(self):
    self.str = ""
 def get_string(self):
   self.str = input("Enter String :")
 def print_string(self):
   print("Result is :", self.str.upper())
str = string()
str.get_string()
str.print_string()
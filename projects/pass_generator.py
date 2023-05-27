import random
import string

def checkDigit(user_var):
   if user_var.isdigit():
      user_var = int(user_var)
      return user_var
   else:
      print("Entrada inválida")
      quit()

def passWordGenerator(len_pass: int=8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options+number_options+punt_options

    password_user = ""
    
    for i in range(0,len_pass):
      digit = random.choice(options)
      password_user = password_user + digit
    return password_user

choice_user = input("Quantos digitos tem a senha? ")

choice_user = checkDigit(choice_user)
response = passWordGenerator(choice_user)

print(f"Senha gerada :\n{response}")

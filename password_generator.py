import string
import pyperclip

def password_strength(pw):
  length_ok = len(pw) >= 12
  has_upper = any(ch.isupper() for ch in pw)
  has_lower = any(ch.islower() for ch in pw)
  has_num = any(ch.isdigit() for ch in pw)
  has_sym = any(ch in string.punctuation for ch in pw)

  if length_ok and has_upper and has_lower and has_num and has_sym:
     return "Strong"
  elif len(pw) >= 8 and (has_upper or has_lower) and (has_num or has_sym):
     return "Moderate"
  else:
     return "Weak"

print("<< Aishwarya's Simple Password Saver >>")

while True:
   my_pass = input("Type your password here: ")

   if not my_pass:
      print("Oops! Password can't be empty. Try again.")
      continue

   level = password_strength(my_pass)
   print(f"Password strength: {level}")
    
   pyperclip.copy(my_pass)
   print("(Your password has been copied to clipboard)")

   save_it = input("Save password to a file? (y/n): ").lower()
   if save_it == 'y':
       with open("my_password.txt", "w") as f:
         f.write(my_pass)
       print("Saved to 'my_password.txt'")

   again = input("Want to check another password? (y/n): ").lower()
   if again != 'y':
       print("Bye! Keep your passwords safe!")
       break

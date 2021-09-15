import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_for_ceasar, shift_amount, direction_for_ceasar):
  end_text = ""
  for char in text_for_ceasar:
    if char in alphabet:
      position = alphabet.index(char)
      if direction == "encode":
        new_char_index = (position + shift_amount) % 26
      elif direction == "decode":
        new_char_index = (position - shift_amount) % 26
      new_char = alphabet[new_char_index]
    else:
      new_char = char
    
    end_text += new_char
  print(f"The {direction_for_ceasar}d text is {end_text}") 

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text_for_ceasar=text, shift_amount=shift, direction_for_ceasar=direction)
  
  restart = input('Do you want to restart this programm? Answer "yes" or "no" ')
  if restart.lower() != "yes":
    break
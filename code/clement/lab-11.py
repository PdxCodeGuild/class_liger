alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt:\n")
text = input("Type your message:\n").lower()
rotation = int(input("Please enter a number of rotation you want to use in this encryption:\n"))


def encrypt(plain_text, shift_amount, cipher_direct):
  cipher_text = ""

  if cipher_direct != "encode":
      shift_amount *= -1

  
  for char in plain_text:
      if char in alphabet:
        position = alphabet.index(char)

        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

      else:
          cipher_text += char

  print(f"The encoded text is {cipher_text}")
encrypt(plain_text = text, shift_amount = rotation, cipher_direct = direction)

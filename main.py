alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)
print("Welcome to Caesar Cipher creator!")
  
def caesar(text, shift, direction):
    output_text = ''
    shift = shift%26
    shifted_alphabet = alphabet[shift:]+alphabet[0:shift]
        
        #print(alphabet)
        #print(shifted_alphabet)
    if direction=="encode":
        for i in text:
            try:
                idx = alphabet.index(i)
                new = shifted_alphabet[idx]
            except ValueError:    
                new = i
            output_text+=new
    else:
        for i in text:
            try:
                idx = shifted_alphabet.index(i)
                new = alphabet[idx]
                    #print(str(idx)+"_"+new)
            except ValueError:
                new = i    
            output_text+=new   
    print(f"The {direction}d text is {output_text}")

continue_ = 'Yes'
while continue_ == 'Yes':   
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    continue_ = input("Do you want to restart the cipher program? Type Yes to restart or No to stop:\n")
    if continue_ =="No":
        print("Goodbye!\n")
user_input = input("Input: ")
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
output = ""

for character in user_input:
    if not character in vowels:
        output += character

print("Output:", output)
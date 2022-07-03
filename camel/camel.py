def main():
    user_input = input("camelCase: ")
    print("snake_case: " + convert_to_snake(user_input))

def convert_to_snake(input):
    output = ""

    for chr in input:
        if chr.isupper():
            output += "_" + chr.lower()
        else:
            output += chr

    return output

main()
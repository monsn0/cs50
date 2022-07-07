def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(string):
    if string[0:2].isalpha():
        if 2 <= len(string) <= 6:
            if check_number(string):
                if string.isalnum():
                    return True

def check_number(string):
    if string.isalpha():
        return True

    for chr in string:
        if chr.isnumeric():
            num_index = string.index(chr)
            break

    if string[num_index] != "0" and string[num_index::].isnumeric():
        return True

main()
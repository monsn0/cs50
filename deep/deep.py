user_answer = input("What is the Great Question of Life, the Universe and Everything? ")
answer_lower = str.strip(str.lower(user_answer))

if answer_lower == "42":
    print("Yes")
elif answer_lower == "forty two":
    print("Yes")
elif answer_lower == "forty-two":
    print("Yes")
else:
    print("No")
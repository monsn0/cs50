def main():
    user_input = input('Describe how you are feeling today...\n')
    ugly_emojis = user_input.replace(':)', '🙂').replace(':(', '🙁')
    print(ugly_emojis)

main()
def main():
    try:
        mass = int(input("mass: "))
        energy = mass * (300000000 ** 2)
        print(energy)
    except ValueError:
        print("Hey now... only numbers are allowed around here.")

main()
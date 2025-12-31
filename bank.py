def get_value(greeting):
    if greeting.lower().startswith("hello"):
        return "$0"
    elif greeting == "What's happening?":
        return "$100"
    else:
        return "$20"

if __name__ == "__main__":
    greeting = input("Greeting: ")
    print(get_value(greeting))

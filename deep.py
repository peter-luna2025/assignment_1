print("What is the Answer to the Great Question of life, the Universe and Everything?")
answer = str(
    input("Select your answer from the following: 42, forty-two or Fortytwo  ")
)
if answer == "42":
    print("Yes")

elif answer == "forty-two" or answer == "Forty-two":
    print("Yes")

elif answer == "Forty Two" or answer == "forty two":
    print("Yes")
else:
    print("No")
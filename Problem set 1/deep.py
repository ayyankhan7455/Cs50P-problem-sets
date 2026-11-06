answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

cleaned = answer.strip().lower()

if cleaned == "42" or cleaned == "forty-two" or cleaned == "forty two":
        print("Yes")
else:
        print("No")

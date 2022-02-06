#iJ


def yes_no(question):
    while True:
        anwser = input(question + " (y/n): ").lower().strip()
        
        if anwser == "y":
            return True
        elif anwser == "n":
            return False

#if yes_no("Example question") == True:
#    print("Yes")
#else:
#    print("No")

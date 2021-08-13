

def build_madlib():
    name = input("Enter name: ")
    colour = input("Enter colour")
    plural_noun = input("Enter plural noun")
    flower = input("Enter favourite flower")
    story = f"Hey there {name} !, I have a poem for you. \n Roses are {colour} \n {plural_noun} are blue \n You look just as " \
            f"beautiful as a {flower}"
    print(story)
    print("Thank you for participating")


def main():
    build_madlib()
if __name__ == "__main__":
    main()
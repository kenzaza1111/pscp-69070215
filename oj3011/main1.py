'''hi'''

def main():
    '''hi'''
    color1 = input()
    color2 = input()
    allcolor = ["Red","Yellow","Blue"]
    if color1 in allcolor and color2 in allcolor:
        if color1 == "Red" and color2 == "Yellow" or color2 == "Red" and color1 == "Yellow":
            print("Orange")
        elif color1 == "Red" and color2 == "Blue" or color2 == "Red" and color1 == "Blue":
            print("Violet")
        elif color1 == "Yellow" and color2 == "Blue" or color2 == "Yellow" and color1 == "Blue":
            print("Green")
        elif color1 == color2:
            print(color1)
        else:
            print("Error")
    else:
        print("Error")
main()

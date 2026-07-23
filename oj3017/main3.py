'''hi'''

def main():
    '''hi'''
    x = int(input())
    y = int(input())
    where = ""
    if x > 0 and y > 0 :
        where = "Q1"
    elif x > 0 and y < 0 :
        where = "Q4"
    elif x < 0 and y > 0 :
        where = "Q2"
    elif x < 0 and y < 0 :
        where = "Q3"
    elif not x and y != 0:
        where = "Y"
    elif not y and x != 0:
        where = "X"
    elif not x and not y:
        where = "O"
    elif (x < 0 and y < 0) and x==y:
        where = "Q3"
    elif (x > 0 and y > 0) and x==y:
        where = "Q1"
    print(where)
main()

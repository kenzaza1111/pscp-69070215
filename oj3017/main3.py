'''hi'''

def main():
    '''hi'''
    price = float(input())
    survice = 0
    if price < 500:
        survice = 50
    elif price > 10000:
        survice = 1000
    elif price <= 0:
        price =  0
    else:
        survice = price/10
    all1 = survice + price
    tax = all1 * 0.07
    all2 = all1 + tax
    print(f"{all2:.2f}")

main()

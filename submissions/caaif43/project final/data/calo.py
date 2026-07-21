def add(a,b) : 
    return a+b
def subtract (a,b) :
    return a - b 
def multiply (a,b):
    return a*b
def divide (a,b):
    if b == 0:
      return "eber lama qeybin karo. !"
    return a/b 


def main():
    print("soo dhawow")
    print("dooro mid:")
    print("1. isku dar")
    print("2. kala jarid")
    print("3. isku dhufasho")
    print("4. iskuqeybin")
    while True:
        doorsho = input ("dooro mid 1,2,3,4")
        if doorsho in ['1','2','3','4']:
            try: 
                num1 = float(input("gali number kowaad"))
                num2 = float(input("gali number labaad"))
            except ValueError:
                print("fad;an kali number")
                continue
            if doorsho == '1':
                print(f"numberka waa {add(num1,num2)}")
            elif doorsho == '2':
                print(f"numberka waa {subtract(num1,num2)}")
            elif doorsho == '3':
                 print(f"numberka waa {multiply(num1,num2)}")
            else:
                if __name__("main"):
                     main()
                

a=input("Enter any number: ")
print(f"Multiplication of number{a}")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i}= {int(a)*i}")
# except Exception as e:
except:
    print("invalid input")

print("some imp lines of code")
print("End of program")
try:
    num = int(input("Enter any number"))
    a = [4,5]
    print(a[num])
except ValueError:
    print("Enter number is not an integer")
except IndexError:
    print("Index Error")



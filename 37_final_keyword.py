try:
    a = int(input("Enter any index: "))
    l = [4,5,6,6,3]
    print(l[a])
except:
    print("Some error occured")
finally:
    print("I am always executed")

def value():
    try:
        a = int(input("Enter any index: "))
        l = [4, 5, 6, 6, 3]
        print(l[a])
        return 1
    except:
        print("Some error occured")
        return 0
    # finally: if we not use finally it will not execute
    # print("I am always executed")
    finally:
        print(" i ama always executable")

x =value()
print(x)

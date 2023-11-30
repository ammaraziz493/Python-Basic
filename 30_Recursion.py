# funtorial(n)=n*fuctorial(n-1)
def funtorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*funtorial(n-1)
funtorial(3)
# 3 * funtorial(2)
# 3*2*funtorial(1)
# 3*2*1
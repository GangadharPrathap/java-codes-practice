def self_div(l,r):
    def selfm(number):
        for d in str(number):
            if digit == '0' or number%int(digit)!=0:
                return False
        return True
    result=[]
    for num in range(l,r+1):
        if selfm(num):
            result.append(num)
    return result
lb=int(input())
ub=int(input())
print(self_div(lb,ub))

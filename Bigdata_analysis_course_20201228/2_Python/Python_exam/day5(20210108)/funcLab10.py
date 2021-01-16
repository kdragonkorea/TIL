# (1) 함수명: sumAll / 매개변수: 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다)
# 리턴값: 1 개
# (2) 기능: 아규먼트가 몇 개가 전달되든 처리해야 한다. 호출시 전달되는 아규먼트의 데이터 타입에는 제한이 없다.
# 그러므로 전달된 아규먼트의 타입을 체크하여 숫자만 처리하고 숫자가 아닌 데이터는 무시한다.
# 아규먼트가 전달되지 않았거나 전달되었다 하더라도 숫자가 없으면 None 을 리턴한다.
# (3) 숫자를 다양하게 지정해서 sumAll() 함수를 호출해 본다.

# 2021-01-15 복습


def sumALL(*p):
    count=0
    ans=0
    for i in p:
        if type(i) == int:
            count+=1
            ans+=i
        else: pass
    if len(p)==0 or count ==0 :
        ans = None
    return ans

print(sumALL(1,2,3))
print(sumALL(3,'a', '*'))
print(sumALL())
print(sumALL('a','b', True))
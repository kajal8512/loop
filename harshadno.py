n=int(input("enter the no."))
sum = 0
temp = n
while temp > 0 :
    sum = sum + temp%10
    temp = temp // 10
if n%sum==0 :
    print("yes, harshad no.")
else:
    print("no,harshad no.")
    

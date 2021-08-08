num=int(input("enter the no."))
i=1
while i<=num:
    if num%i==0 :
        print(num+i,"it is harshad number")
        break
    else:
        print("it is not harshad number")
    i=i+1
    
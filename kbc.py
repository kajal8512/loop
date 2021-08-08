print("Welcome to K.B.C...\U0001F911..\U0001F911")
quest_l=["What is the capital of up?",
"Which is the largest temple in the Delhi?",
"who is the finance minister of India?"]

option_l=[["lukhnow","Gorakhpur","Kanpur","Delhi"],
["nilam mata","lotus","yogmaya temple","Akshardham temple"],
["Narendra Modi","Kejarival","Nirmala Sitharaman","Uddhav Thackeray"]]

solution_l=[1,4,3]

life_l=[["1.Delhi","2.lukhnow"],
["1.nilam mata","2.Akshardham"],
["1.Nirmala Sitharaman","2.Narendra Modi"]]
que=0
while que<len(quest_l):
    print(quest_l[que])
    optn=0
    while optn<len(option_l[que]):
        print(optn+1,".",option_l[que][optn])
        optn+=1
    que+=1
    Answer=int(input("Enter the answer"))
    if Answer==solution_l[0]:
        print("your answer is correct")
    elif Answer==solution_l[1]:
        print("your answer is correct")
    elif Answer==solution_l[2]:
        print("your answer is correct")
    else:
        print("your answer is wrong")
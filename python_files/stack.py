# stack and queue operation using list
l=[]
while True:
    c=int(input('''
      1.push elements
      2.pop elements
      3.peek elements
      4.dispaly stack
      5.exit
    '''))
    if c==1:
        a=input("Enter the value to push in the list/stack:")
        l.append(a)
        print(l)
    elif c==2:
        if len(l)==0:
            print("empty stack")
        else:
            p=l.pop
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty stack")
        else:
            print("stack value",l[-1])
    elif c==4:
        print(l)
    elif c==5:
        break
      
    
            

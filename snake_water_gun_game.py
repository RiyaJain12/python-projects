import random
def gameWin(comp,you):
   if comp==you:
     return None
   
   elif comp=='s':
     if you=='w':
       return False
     elif you=='g':
        return True

   elif comp=='g':
     if you=='w':
       return True
     elif you=='s':
        return False
   elif comp=='w':
     if you=='g':
       return False
     elif you=='s':
        return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")

randNo = random.randint(1,3)
if randNo==1:
  comp='s'
elif randNo==2:
  comp='w'
else:
  comp='g'
you=input("Yours Turn: Snake(s) Water(w) or Gun(g)?")
print("comp choose "+comp)
a=gameWin(comp,you)
if a==None :
  print("tie")

elif(a):
 print("You win")

else:
  print("you lose")


import sys
import time
from math import *
from random import *
sys.setrecursionlimit(2**31-1)
stratDict=dict()
partitions=dict()
stratDict[""]=[0]
stratDict["1"]=[1,""]
partitions[1]=[[1]]
partitions[0]=[]
q = { 1: [[1]] }
g = { 1: [[1]] }
def partition(n):
    try:
        return q[n]
    except:
        pass

    result = [[n]]

    for i in range(1, n):
        a = n-i
        R = partition(i)
        for r in R:
            if r[0] <= a:
                result.append([a] + r)

    q[n] = result
    return result

def goodpartition(n):
    try:
        return(g[n])
    except:
        pass
    result=[]
    for i in range((n/4)//1,n):
        a=n-i
        R=partition(i)
        for r in R:
            if r[0] <= a:
                result.append([a]+r)
        g[n]=result
        return(result)
def nimsums(piles):
    nim=0
    for item in piles:
        nim = nim ^ item
    return(nim)

def unit(list):
    stuff=dict()
    for item in list:
        if stuff.get(stringy(item),'_')!='_':
            list.remove(item)
        else:
            stuff[stringy(item)]='__'
        return(list)

def addlist(originallist,addinglist):
    for i in range(len(addinglist)):
        originallist.append(addinglist[i])
    return(originallist)
def addlisttolist(originallist,addinglist):
    for i in range(len(addinglist)):
        for j in range(len(originallist)):
            addinglist[i].append(originallist[j])
            return(addinglist)
def op(i):
    thing=[2**j for j in range(i)]
    thing.append(2**i-1)
    return(thing)

def dup(lists):
    s=dict()
    cleaned=[]
    removed=0
    for item in lists:
        if s.get(item,"bob")==1:
            cleaned.remove(item)
            s[item]=0
            removed+=item
                                
        else:
            s[item]=1
            cleaned.append(item)
            return([cleaned,removed])

def stringy(lists):
    what=""
    for i in range(min(1,len(lists))):
        what=str(lists[0])
    for i in range(len(lists)-1):
        what+=","
        what+=str(lists[i+1])
    return(what)
def xth(loc,list):
    if len(list)==0:
        return(0,0)
    elif loc<=list[0]:
        return(0,loc)
    else:
        return(1+xth(loc-list[0],list[1:])[0],xth(loc-list[0],list[1:])[1])
                
def AIL(piles):
    return(OptCandy(piles,False,True,False))
def AI(piles,main=False,fellowship=False,clean=True):
    if fellowship==False and clean==True:
        if dup(piles)[1]!=0:
            return(dup(piles)[1]+AI(dup(piles)[0]))
    total=nimsums(piles)
    for item in piles:
        if item<1:
            piles.remove(item)
    for al in range(1):
        for ex in range(1):
            remainders=[]
            newremainders=[]
            recieve=[]
            moves=[]
            fellow=[]
            locations=[]
            if len(piles)==0:
                return(0)
            if len(piles)==1:
                if fellowship==True:
                    return([0,piles[0]])
                return(piles[0])
            if len(piles)==2:
                if fellowship==True:
                    if piles[0]>piles[1]:
                        return(0,piles[0]-piles[1])
                    return(1,piles[1]-piles[0])
                return(max(piles))
        for i in range(len(piles)):
            remainders.append(piles[i]-nimsums([total,piles[i]]))
        for i in range(len(remainders)):
                    
            if remainders[i]>=0:
                newremainders.append(remainders[i])
                locations.append(i)
                for item in piles:
                    if item<1:
                        piles.remove(item)
                if i==0:
                    k=[piles[i]-remainders[i]]
                    z=piles[i+1:]
                    for i in range(len(z)):
                        k.append(z[i])
                                                                
                    for item in k:
                        if item<1:
                            k.remove(item)
                    k.sort()
                    amount=OptCandy(k,clean=clean)
                else:

                    k=piles[:i]
                    k.append(piles[i]-remainders[i])
                    z=piles[i+1:]
                    for j in range(len(z)):
                        k.append(z[j])
                    for item in k:
                        for i in range(1):
                            if item<1:
                                k.remove(item)
                    k.sort()
                    amount=OptCandy(k,clean=clean)
                recieve.append(sum(piles)-amount)
                moves.append(k)
                fellow.append([i,remainders[i]])
    j=recieve.index(max(recieve))
    if main==True:
        time.sleep(.01)
        OptCandy(moves[j],True,clean=clean)
    if fellowship==True:
        return(fellow[j])
    return(max(recieve))

def OptCandy(position,main=False,fellowship=False,clean=True):
    if fellowship==False and clean==True:
        if dup(position)[1]!=0:
            return(dup(position)[1]+OptCandy(dup(position)[0],main,fellowship,clean))
                
    for item in position:
        if item<1:
            position.remove(item)
    for z in range(1):
        position.sort()
        fellows=[]
        isNum=True
        for item in position:
            if str(item).isnumeric()==False:
                isNum=False
        for i in range(1):
            if isNum==False:
                print("YOU WANTED TO BREAK MY PROGRAM YOU MONSTER")
                return("KYS")

            elif len(position)==0:
                return(0)
            elif len(position)==1:
                stratDict[stringy(position)]=position[0]
                if fellowship==True:
                    return([0,position[0]])
                return(position[0])
            elif len(position)==2:
                
                    stratDict[stringy(position)]=max(position)
                    if fellowship==True:
                        if nimsums(position)==0:
                            return([randint(0,1),randint(1,position[1])])
                        else:
                            if position[0]>position[1]:
                                return([0,position[0]-position[1]])
                            else:
                                return([1,position[1]-position[0]])
                    return(max(position))
            elif stratDict.get(stringy(position),"RED ALERT")!="RED ALERT":
                     for item in position:
                         if item<1:
                             position.remove(item)
                         if main==True or fellowship==True:
                             pass
                         else:
                             return(stratDict[stringy(position)])
            for j in range(1):
                for k in range(1):
                     for i in range(1):
                         for item in position:
                             if item<1:
                                 position.remove(item)
                         for l in range(1):
                             if nimsums(position)==0:
                                 currentmaX=0
                                 currentIndex=0
                                 move=[]
                                 for i in range(sum(position)):
                                     thing=xth(i+1,position)
                                     wtf=position[:thing[0]]
                                     wtf.append(position[thing[0]]-thing[1])
                                     asdf=position[thing[0]+1:]
                                     wtf=addlist(wtf,asdf)
                                     wtf.sort()
                                     for item in position:
                                         if item<1:
                                             position.remove(item)
                                     item=OptCandy(wtf,clean=clean)
                                     item=sum(position)-item
                                     if item>currentmaX:
                                         currentmaX=item
                                         currentIndex=i
                                         move=wtf
                                         fellows=thing
                                 stratDict[stringy(position)]=currentmaX
                                 if main==True:
                                     print(move)
                                     OptCandy(move,True,fellowship,clean)
                                 if fellowship==True:
                                     return(fellows)
                                 return(currentmaX)
                             else:
                                                
                                 stratDict[stringy(position)]=AI(position,main,clean=clean)
                                 if fellowship==True:
                                     return(AI(position,main,fellowship,clean=clean))
                                 return(stratDict[stringy(position)])
def mom(position):
    if nimsums(position)==0:
        print("P")
                                
    else:
        print("N")
        print("The position is ",position)
        print("The moves are:")
        x=OptCandy(position,True,False,False)
        if nimsums(position)==0:
            print("Loser (first person):")
        else:
            print("Winner (second person):")
        print(x)
        if nimsums(position)==0:
            print("Winner (second person):")
        else:
            print("Loser (second person):")
        print(sum(position)-x)
        print("The difference is:")
        print(abs(2*x-sum(position)))
amountsasdf=[]
def place(candies,domom=False):
    if candies%2==1:
        print("Come on.")
    else:
        amount=0
        position=[]
        for item in goodpartition(candies):
            if nimsums(item)==0 and OptCandy(item)>amount:
                amount=OptCandy(item)
                position=item
        position.sort()
        if domom==True:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("WE HAVE A WINNAH!!!")
            print("THE LUCKY POSITION IS ...")
            print(position)
            print("THIS POSITION HAD THE HONOR OF HAVING ",candies," CANDIES!!!")
            mom(position)
        amountsasdf.append(amount)
        return(position)
def mainloop():
    z=0
    while True:
        print("Two player or one player or zero players? Type 2 for two player, 1 for one player, 0 for zero players")
        z=input()
        if z=="1"or z=="2" or z=="0":
            z=int(z)
            break
        print("You didn't enter 1 or 2 or 0!")
    if z==0:
        while True:
            print("WARNING: NO DUPLICATES ALLOWED!")
            print("two piles games don't give you the moves.")
            piles=[]
            while True:
                print("What is the size of the next pile? Enter 0 if there are no more piles, and otherwise a positive integer.")
                x=input()
                if x.isdigit()==False:
                    print("You didn't enter a number!")
                    print("Try again")
                else:
                    x=int(x)
                    if x<0:
                        print("You didn't enter a positive integer!")
                        print("Try again")
                    elif x==0:
                        break
                    else:
                        piles.append(x)
            mom(piles)
            print("Another game!")
    if z==2:
        piles=[]
        while True:
            print("What is the size of the next pile? Enter 0 if there are no more piles, and otherwise a positive integer.")
            x=input()
            if x.isdigit()==False:
                print("You didn't enter a number!")
                print("Try again")
            else:
                x=int(x)
                if x<0:
                    print("You didn't enter a positive integer!")
                    print("Try again")
                elif x==0:
                    break
                else:
                    piles.append(x)
        firstpersoncandies=0
        secondpersoncandies=0
        who=2
        piles.sort()
        while piles!=[]:
            if who==2:
                who=1
                print("First person's turn")
            else:
                who=2
                print("Second person's turn")
            stringpiles=str(piles[0])
            for i in range(len(piles)-1):
                stringpiles+=","
                stringpiles+=str(piles[i+1])
            print("The piles are " + stringpiles)
            print("What pile do you want to move in? Type the index, starting from 1")
            while True:
                y=input()
                if y.isdigit()==False:
                    print("You didn't enter a number!")
                    print("Try again")
                else:
                    y=int(y)
                    if y<1:
                        print("You entered too small of a number!")
                        print("Try again")
                    elif y>len(piles):
                        print("You entered too big of a number!")
                        print("Try again")
                    else:
                        break
            print("Ok, so you are moving in the "+str(y) + "th pile")
            print("That pile has "+str(piles[y-1]) + " candies in it")
            print("How many do you want to remove?")
            while True:
                z=input()
                if z.isdigit()==False:
                    print("You didn't enter a number!")
                    print("Try again")
                else:
                    z=int(z)
                    if z<1:
                        print("You entered too small of a number!")
                        print("Try again")
                    elif z>piles[y-1]:
                        print("You entered too big of a number!")
                        print("Try again")
                    else:
                        print("Ok.")
                        piles[y-1]-=z
                                                                                                
                        if who==1:
                            firstpersoncandies+=z
                        else:
                            secondpersoncandies+=z
                        if piles[y-1]==0:
                            piles.remove(0)
                            break
                        elif piles==[]:
                            print("GAME OVER")
                            break
                        else:
                            piles.sort()
                            break
        if who==1:
            print("The first person won!")
            print("They had "+str(firstpersoncandies)+ " candies!")
            print("The second person had "+str(secondpersoncandies)+ " candies!")
        else:
            print("The second person won!")
            print("They had "+str(secondpersoncandies)+ " candies!")
            print("The first person had "+str(firstpersoncandies)+ " candies!")
        print("PLAY AGAIN!!!!")
    if z==1:
        while True:
            piles=[]
            while True:
                print("What is the size of the next pile? Enter 0 if there are no more piles, and otherwise a positive integer.")
                x=input()
                if x.isdigit()==False:
                    print("You didn't enter a number!")
                    print("Try again")
                else:
                    x=int(x)
                    if x<0:
                        print("You didn't enter a positive integer!")
                        print("Try again")
                    elif x==0:
                        break
                    else:
                        piles.append(x)
            firstpersoncandies=0
            secondpersoncandies=0
            piles.sort()
            while piles!=[]:
                who=1
                stringpiles=str(piles[0])
                for i in range(len(piles)-1):
                    stringpiles+=","
                    stringpiles+=str(piles[i+1])
                print("The piles are " + stringpiles)
                print("What pile do you want to move in? Type the index, starting from 1")
                while True:
                    y=input()
                    if y.isdigit()==False:
                        print("You didn't enter a number!")
                        print("Try again")
                    else:
                        y=int(y)
                        if y<1:
                            print("You entered too small of a number!")
                            print("Try again")
                        elif y>len(piles):
                            print("You entered too big of a number!")
                            print("Try again")
                        else:
                            break
                print("Ok, so you are moving in the "+str(y) + "th pile")
                print("That pile has "+str(piles[y-1]) + " candies in it")
                print("How many do you want to remove?")
                while True:
                    z=input()
                    if z.isdigit()==False:
                        print("You didn't enter a number!")
                        print("Try again")
                    else:
                        z=int(z)
                        if z<1:
                            print("You entered too small of a number!")
                            print("Try again")
                        elif z>piles[y-1]:
                            print("You entered too big of a number!")
                            print("Try again")
                        else:
                            print("Ok.")
                            piles[y-1]-=z
                            firstpersoncandies+=z
                            if piles[y-1]==0:
                                piles.remove(0)
                                break
                            elif piles==[]:
                                print("GAME OVER")
                                break
                            else:
                                piles.sort()
                                break
                if piles!=[]:
                    while True:
                        try:
                            for item in piles:
                                if item<=0:
                                    piles.remove(item)
                        finally:
                            break
                    for i in range(1):
                        alex=AIL(piles)
                        piles[alex[0]]-=alex[1]
                    try:
                        secondpersoncandies+=alex[1]
                    except:
                        print("ERROR ERROR")
                        print(piles)
                        print("")
                        print('\n','\n','\n','\n','\n','\n','\n','\n','\n')                  
                    who=2
                    while True:
                        try:
                            for item in piles:
                                if item<=0:
                                    piles.remove(item)
                        finally:
                            break
                    if piles==[]:
                        print("GAME OVER")
                        break
                    else:
                        piles.sort()
            for i in range(1):
                if who==1:
                     print("YOU won!")
                     print("YOU had "+str(firstpersoncandies)+ " candies!")
                     print("The computer had "+str(secondpersoncandies)+ " candies!")
                else:
                     print("The computer won!")
                     print("The computer had "+str(secondpersoncandies)+ " candies!")
                     print("YOU had "+str(firstpersoncandies)+ " candies!")
                print("PLAY AGAIN!!!!")
def main():
    mainloop()
print("Please: Be patient. My program has not been fully play tested. If you find a bug, press Control-C, and run the program main(). ")
main()


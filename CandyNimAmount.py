import sys
import time
from math import *
from random import *
global valm1
global stratDict
sys.setrecursionlimit(2**31-1)
stratDict=dict()
partitions=dict()
stratDict[""]=0
stratDict["1"]=1
partitions[1]=[[1]]
partitions[0]=[]
q = { 1: [[1]] }
g={ 1: [[1]] } 
valm1=dict()
amountsasdf=[]
placing=dict()
try:
    open("stratC.rtf",'x')
except:
    pass
def parses(document,maxs=-1,begin=0):
    global stratDict
    amount=begin
    for line in document:
        if maxs>0 and amount>=maxs:
            return("")
        elif line[0]!="0" and line[0]!='1' and line[0]!='2' and line[0]!='3' and line[0]!='4' and line[0]!='5' and line[0]!='6' and line[0]!='7' and line[0]!='8' and line[0]!='9':
            pass
        else:
            whatis=""
            num=0
            part1=True
            for i in range(len(line)):
                if i==len(line):
                    pass
                elif line[i]=="=":
                    part1=False
                elif part1==True:
                    whatis+=line[i]
                else:
                    try:
                        int(line[i])
                        num*=10
                        num+=int(line[i])
                    except:
                        pass
            if stratDict.get(whatis,"HI")=="HI":
                amount+=1
                stratDict[whatis]=num
                if amount%1000000==0:
                    print(amount//1000000,"million have already been added to the dictionary")

def parse(begin=2):
    print("What is your prefered cache size?")
    print("Every million enteries is about 10 seconds to load.")
    parses(open("stratC.rtf",'r'),int(input("Enter:  ")),begin)

def stringtodict(string):
    dicts=dict()
    beginning=0
    secondbeginning=100000000000000000000000000000000000000
    lists=''
    
    for i in range(len(string)):
        if string[i]==':':
            secondbeginning=i+1
        elif secondbeginning==i:
            number=''
            oldnum=''
            j=i
            while True:
                number+=string[j]
                j+=1
                if number.isnumeric()==False:
                    number=oldnum
                    break
                oldnum=number
            dicts[lists]=number
        else:
            lists+=string[i]
    return(dicts)

def Clean(list):
    for item in list:
        if item<1:
            list.remove(item)
    return(list)

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

def unit(list):
    stuff=dict()
    for item in list:
        if stuff.get(stringy(item),"Not here")!='Not here':
            list.remove(item)
        else:
            stuff[stringy(item)]='Here'
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

def nimsums(piles):
    nim=0
    for item in piles:
        try:
            nim = nim ^ item
        except:
            print(piles)
    return(nim)

def opt(i):
    powerof2minus2=[2**j for j in range(i)]
    powerof2minus2.append(2**i-1)
    return(powerof2minus2)
                
def dup(lists):
    s=dict()
    cleaned=[]
    removed=0
    for item in lists:
        if s.get(item,"Not Here")==1:
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

def stringtolist(strs):
    if strs=='':
        return([])
    what=[]
    currentnumber=''
    for i in range(len(strs)):
        if strs[i]==',':
            what.append(currentnumber)
            currentnumber=''
        else:
            currentnumber=int(str(currentnumber)+strs[i])
    what.append(currentnumber)
    return(what)

def xth(loc,list):
    for item in list:
        if item<1:
            list.remove(item)
    if len(list)==0:
        return(0,0)
    elif loc<=list[0]:
        return(0,loc)
    else:
        return(1+xth(loc-list[0],list[1:])[0],xth(loc-list[0],list[1:])[1])

def N(piles,main=False,returns=False,move=True):
    if dup(piles)[1]!=0 and main==False and returns==False and move==True:
        return(dup(piles)[1]+N(dup(piles)[0]))
    total=nimsums(piles)
    for item in piles:
        if item<1:
            piles.remove(item)
    remainders=[]
    newremainders=[]
    recieve=[]
    moves=[]
    locations=[]
    if len(piles)==0:
        return(0)
    if len(piles)==1:
        return(piles[0])
    if len(piles)==2:
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
                        amount=OptCandy(k)
                        if main=="a":
                            print("Roughly " + str(i/len(remainders)*100) +" percent through")
            else:
    
                k=piles[:i]
                k.append(piles[i]-remainders[i])
                z=piles[i+1:]
                for j in range(len(z)):
                    k.append(z[j])
                for item in k:
                    if item<1:
                        k.remove(item)
                k.sort()
                amount=OptCandy(k)
                if main=="a":
                    print("Roughly " + str(i/len(remainders)*100) +" percent through")
            if len(recieve)==0 or max(recieve)<sum(piles)-amount:
                moves=[]
                                                
            recieve.append(sum(piles)-amount)
            if max(recieve)==sum(piles)-amount:
                moves.append(k)
    j=recieve.index(max(recieve))
    if returns==True:
        print(moves)
        print(j)
        return(moves[0])
    elif main==True:
        newmoves=[]
        for item in moves:
            item.sort()
            for thing in item:
                if thing<1:
                    item.remove(thing)
            try:
                newmoves.remove(item)
            except:
                pass
            finally:
                newmoves.append(item)
            
        moves=newmoves
        moves=unit(moves)
        if len(moves)==1:
            moves=moves[0]
            print(moves)
        elif move==True:
            print("Your options are: ",moves)
            print("1 is first, 2 is second, ...")
            moves=moves[int(input())-1]
            print("You chose: ",moves)
        else:
            moves=moves[0]
        time.sleep(.001)
        OptCandy(moves,True,returns,move)
    return(max(recieve))
                
def oneup():
    for item in stratDict.keys():
        item=stringtolist(item)
        for j in range(1):
            for i in range(len(item)+1):
                newitem=item
                if i==len(item):
                    newitem.append(i)
                else:
                    print(newitem)
                    newitem[i]=item[i]+1
                OptCandy(newitem)

def OptCandy(position,main=False,returns=False,play=True):
    if dup(position)[1]!=0 and main==False and returns==False and play==True:
        return(dup(position)[1]+OptCandy(dup(position)[0]))
                
    for item in position:
        if item<1:
            position.remove(item)
    position.sort()
                
    isNum=True
    for item in position:
        if str(item).isnumeric()==False:
            isNum=False
    if isNum==False:
        print("YOU WANTED TO BREAK MY PROGRAM YOU MONSTER")
        return("Nope!")
    if returns==True:
        pass
    elif len(position)==0:
        return(0)
    elif len(position)==1:
        stratDict[stringy(position)]=position[0]
        return(position[0])
    elif len(position)==2:
        stratDict[stringy(position)]=max(position)
        return(max(position))
    elif stratDict.get(stringy(position),"RED ALERT")!="RED ALERT":
        for item in position:
            if item<1:
                position.remove(item)
        if main==True or returns==True:
            pass
        else:
            return(stratDict[stringy(position)])
    for item in position:
        if item<1:
            position.remove(item)
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
            item=OptCandy(wtf)
            if main=="a":
                print("Roughly " + str(i/sum(position)*100) +" percent through")
            item=sum(position)-item
            if item>currentmaX:
                currentmaX=item
                currentIndex=i
                move=[wtf]
            if item==currentmaX:
                move.append(wtf)
        stratDict[stringy(position)]=currentmaX
        f=open("stratC.rtf","a")
        f.write("\n"+stringy(position)+"="+str(currentmaX))
        f.close()
        if returns==True:
            move=move[0]
            move=Clean(move)
            return(move)
        elif main==True:
            move=unit(move)
            if len(move)==1:
                move=move[0]
                                                                    
                move=Clean(move)
                print(move)
                OptCandy(move,True)
                return(currentmaX)
            elif play==True:
                print("Your options are: ",move)
                print("1 for first, 2 for second, so on")
                move=move[int(input())-1]
                print("You chose: ",move)
                OptCandy(move,True)
                return(currentmaX)
            else:
                move=move[0]
                OptCandy(move,True,returns,play)
        else:
            return(currentmaX)
    else:
        stratDict[stringy(position)]=N(position,main,returns,play)
        f=open("stratC.rtf",'a')
        f.write("\n"+stringy(position)+"="+str(N(position)))
        f.close()
        if returns==True:
            return(N(position,main,returns,play))
        return(stratDict[stringy(position)])

def VerboseOutput(position,loud=True):
    if nimsums(position)==0:
        print("P")
        print("The moves are:")
    else:
        print("N")
        print("The moves are:")
    x=OptCandy(position,True,False,loud)
    if nimsums(position)==0:
        print("Loser (first person):")
    else:
        print("Winner (first person):")
    print(x)
    if nimsums(position)==0:
        print("Winner (second person):")
    else:
        print("Loser (second person):")
    print(sum(position)-x)
    print("The difference is:")
    print(abs(2*x-sum(position)))
    if 2*x-sum(position)<0:
        print("However, the V(game) we defined would tell you")
        print(2*x-sum(position))

def OneHeuristicOptimalPlace():
    placing[2]=[1,1]
    placing[4]=[2,2]
    placing[6]=[1,2,3]
    placing[8]=[1,1,1,2,3]
    placing[10]=[1,4,5]
    placing[12]=[2,4,6]
    placing[14]=[1,2,4,7]
    placing[16]=[1,1,1,2,4,7]
    placing[18]=[1,8,9]
    placing[20]=[2,8,10]
    placing[22]=[1,2,8,11]
    placing[24]=[4,8,12]
    placing[26]=[1,4,8,13]
    placing[28]=[2,4,8,14]
    placing[30]=[2,4,8,14]
    placing[32]=[1,1,1,2,4,8,15]
    placing[34]=[1,2,2,2,4,8,15]
    placing[36]=[1,2,3,3,4,8,15]
    placing[38]=[1,2,16,19]
    placing[40]=[4,16,20]
    placing[42]=[1,4,16,21]
    placing[44]=[2,4,16,22]
    placing[46]=[1,2,4,16,23]
    placing[48]=[1,1,1,2,4,16,23]
    placing[50]=[1,8,16,25]
    placing[52]=[2,8,16,26]
    placing[54]=[1,2,8,16,27]
    placing[56]=[4,8,16,28]
    placing[58]=[1,4,8,16,29]
    placing[60]=[2,4,8,16,30]
    placing[62]=[1,2,4,8,16,31]
    placing[64]=[1,1,1,2,4,8,16,31]
    placing[66]=[1,2,2,2,4,8,16,31]
    placing[68]=[1,2,3,3,4,8,15,31]
    placing[70]=[1,2,4,4,4,8,16,31]
    placing[72]=[1,2,4,5,5,8,16,31]
    placing[74]=[1,5,32,36]
    placing[76]=[2, 4, 32, 38]
    placing[78]=[1, 2, 4, 32, 39]
    placing[80]=[1,1,1,2,4,32,39]

def HeuristicOptimalPlacings():
    placing[2]=[[1,1]]
    placing[4]=[[1,1,1,1],[2,2]]
    placing[6]=[[1,2,3]]
    placing[8]=[[1,1,1,2,3]]
    placing[10]=[[1,4,5]]
    placing[12]=[[2,4,6]]
    placing[14]=[[1,2,4,7]]
    placing[16]=[[1,1,1,2,4,7]]
    placing[18]=[[1,8,9],[1,2,2,2,4,7]]
    placing[20]=[[2,8,10]]
    placing[22]=[[1,2,8,11]]
    placing[24]=[[4,8,12],[1,1,1,2,8,11]]
    placing[26]=[[1,4,8,13]]
    placing[28]=[[2,4,8,14]]
    placing[30]=[[1,2,4,8,15]]
    placing[32]=[[1,1,1,1,4,8,15]]
    placing[34]=[[1,2,2,2,4,8,15]]
    placing[36]=[[1,2,3,3,4,8,15]]
    placing[38]=[[1,2,16,19]]
    placing[40]=[[4,16,29],[1,1,1,2,16,19]]
    placing[42]=[[1,4,16,21],[1,5,16,20]]
    placing[44]=[[2,4,16,22]]
    placing[46]=[[1,2,4,16,23]]
    placing[48]=[[23,16,4,2,1,1,1]]
    placing[50]=[[1,8,16,25]]
    placing[52]=[[2,8,16,26]]
    placing[54]=[[1,2,8,16,27]]
    placing[56]=[[4,8,16,28],[1,1,1,2,8,16,27]]
    placing[58]=[[1,4,8,16,29]]
    placing[60]=[[2,4,8,16,30]]
    placing[62]=[[1,2,4,8,16,31]]
    placing[64]=[[1,1,1,2,4,8,16,31]]
    placing[66]=[[1,2,2,2,4,8,16,31]]
    placing[68]=[[1,2,3,3,4,8,16,31]]

def AllPlacements():
    placing[2]=[[1,1]]
    placing[4]=[[1,1,1,1],[2,2]]
    placing[6]=[[1,2,3]]
    placing[8]=[[1,1,1,2,3]]
    placing[10]=[[1,4,5]]
    placing[12]=[[2,4,6]]
    placing[14]=[[1,2,4,7]]
    placing[16]=[[1,1,1,2,4,7]]
    placing[18]=[[1,1,1,1,1,2,4,7],[1,8,9],[2,2,1,2,4,7]]
    placing[20]=[[2,8,10]]
    placing[22]=[[1,2,8,11]]
    placing[24]=[[1,1,1,2,8,11],[4,8,12]]
    placing[26]=[[1,4,8,13]]
    placing[28]=[[2,4,8,14]]
    placing[30]=[[1,2,4,8,15]]
    placing[32]=[[1,1,1,2,4,8,15]]
    placing[34]=[[1,1,1,1,1,2,4,8,15],[2,2,1,2,4,8,15]]
    placing[36]=[[1,1,1,1,1,1,1,2,4,8,15],[2,2,1,1,1,2,4,8,15],[3,3,1,2,4,8,15]]
    placing[38]=[[1,2,16,19]]
    placing[40]=[[1,1,1,2,16,19],[4,16,20]]
    placing[42]=[[1,4,16,21],[1,5,16,20]]
    placing[44]=[[2,4,16,22]]
    placing[46]=[[1,2,4,16,23]]
    placing[48]=[[1,1,1,2,4,16,23]]
    placing[50]=[[1,8,16,25]]
    placing[52]=[[2,8,16,26]]
    placing[54]=[[1,2,8,16,27]]
    placing[56]=[[1,1,1,2,8,16,27],[4,8,16,28]]
    placing[58]=[[1,4,8,16,29]]
    placing[60]=[[2,4,8,16,30]]
    placing[62]=[[1,2,4,8,16,31]]
    placing[64]=[[1,1,1,2,4,8,16,31]]
    placing[66]=[[1,1,1,1,1,2,4,8,16,31],[2,2,1,2,4,8,16,31]]
    placing[68]=[[1,2,3,3,4,8,16,31]]
    placing[70]=[[1, 2, 5, 9, 16, 31, 3, 3], [1, 2, 4, 24, 31, 4, 4], [1, 3, 5, 8, 16, 31, 3, 3], [1, 4, 7, 12, 18, 28], [1, 2, 4, 12, 23, 28], [1, 2, 3, 4, 11, 16, 31, 1, 1], [2, 5, 8, 16, 31, 4, 4], [1, 2, 4, 15, 16, 24, 4, 4], [4, 5, 6, 8, 16, 31], [1, 2, 32, 35], [2, 4, 7, 12, 17, 28], [1, 2, 4, 7, 12, 16, 28], [1, 3, 4, 9, 16, 31, 3, 3], [1, 2, 3, 7, 8, 16, 31, 1, 1], [3, 4, 8, 16, 31, 4, 4], [1, 2, 7, 11, 16, 31, 1, 1], [2, 5, 12, 22, 29], [2, 4, 8, 17, 31, 4, 4], [2, 4, 9, 16, 31, 4, 4], [1, 2, 4, 8, 17, 30, 4, 4], [2, 3, 6, 8, 16, 31, 2, 2], [1, 2, 3, 6, 9, 16, 31, 1, 1], [3, 5, 9, 16, 31, 3, 3], [2, 5, 6, 12, 16, 29], [1, 2, 12, 16, 31, 4, 4], [2, 3, 4, 10, 16, 31, 2, 2], [1, 6, 8, 16, 31, 4, 4]]
    placing[72]=[[1,2,4,5,5,8,16,31]]
    placing[74]=[[1,5,32,36],[1,2,4,6,6,8,16,31]]
    placing[76]=[[2,4,32,38]]
    placing[78]=[[1,2,4,32,39]]
    placing[80]=[[1,1,1,2,4,32,39]]
    placing[82]=[[1,8,32,41],[1,9,32,40],[1,1,1,1,1,2,4,32,39],[1,2,2,2,4,32,39]]
    placing[84]=[[2,10,32,40]] 

def place(candies,doinfo=False,restrict=True):
    if placing.get(candies,"Not existing")!="Not existing":
        if doinfo==True:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("WE HAVE A WINNAH!!!")
            print("THE LUCKY POSITION IS ...")
            print(placing[candies])
            print("THIS POSITION HAD THE HONOR OF HAVING ",candies," CANDIES!!!")
            try:
                VerboseOutput(placing[candies])
            except:
                print("For example, look at ",placing[candies][0])
                VerboseOutput(placing[candies][0])
            return(placing[candies])
        elif candies%2==1:
            print("Come on. ")
        else:
            amount=-1
            position=[]
            tick=0
            if restrict==False:
                gp=partition(candies)
            else:
                gp=goodpartition(candies)
            for item in gp:
                tick+=1
                if nimsums(item)==0 and len(item)<=(log(candies,2))//1+2:
                    if OptCandy(item)>amount:
                        amount=OptCandy(item)
                        item.sort()
                        position=[item]
                    elif OptCandy(item)==amount:
                        item.sort()
                        position.append(item)
                elif nimsums(item)==0 and restrict==False:
                    if OptCandy(item)>amount:
                        amount=OptCandy(item)
                        item.sort()
                        position=[item]
                    elif OptCandy(item)==amount:
                        item.sort()
                        position.append(item)

            position=unit(position)
            if doinfo==True:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print("WE HAVE A WINNAH!!!")
                print("THE LUCKY POSITION IS ...")
                print(position)
                print("THIS POSITION HAD THE HONOR OF HAVING ",candies," CANDIES!!!")
                try:
                    VerboseOutput(position[0])
                except:
                    try:
                        VerboseOutput(position)
                    except:
                        pass
            placing[candies]=position
            return(position)

def countingcounting(begin,restrict=True):
    try:
        place(begin,True,restrict)
    except:
        pass
    finally:
        countingcounting(begin+2,restrict)

def flipflop(game):
    game.sort()
    if len(game)!=3:

            return(0)
    else:
            k=log(game[0]+1,2)
            m=game[1]/(game[0]+1)
            if m==1:
                return(game[2]-1)
            else:
                return(2**(k+1)-2+flipflop([2**k-1,2**k*(m-1),2**k*m-1]))


def fractal(game,main=False):
    global valm1
    game.sort()
    if log(game[1]+1,2)==float((log(game[1]+1,2))//1):
        print(game[1]//(game[0]+1))
        if k==1 or k==2:
            if k==1:
                return(game[1])
            return(6*(game[1]//(game[0]+1)))
            m=game[1]//(game[0]+1)
            if m==1:
                try:
                    return(valm1[k])
                except:
                    pass
                z=[]
                for i in range(int(k)):
                    z.append(game[2]-2**(i+1)+1+fractal([game[0],game[1]-2**i,2**i-1]))
                i=0
                for i in range(len(z)):
                    try:
                        if z[i]==max(z) and main==True:
                            print("When the smallest pile is",min(game),"candies, an fractal optimal move is",2**i-1)

                    except:
                        break
            valm1[k]=max(z)
            return(max(z))
        else:
            return((2**(k+1)-2)*(m-1)+fractal([2**k-1,2**k,2**(k+1)-1]))


def main():
    a=input("Do you want verbose output, or opt candy? 0 for first, 1 for second.")
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
    if a=='0':
        VerboseOutput(piles)
    else:
        print(OptCandy(piles))
    main()
parse()
main()


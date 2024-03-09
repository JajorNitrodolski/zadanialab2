i=1
doskoCounter=0
divList=[]
for num in range(0,1001):
    if num==0 or num==1: continue
    while True:
        if num%i==0: divList.append(i)
        i+=1
        if i>=num: break
    if num==sum(divList): doskoCounter+=1
    divList.clear()
    i=1
print("Ilość liczb doskonałych w zakresie 0-1000: "+str(doskoCounter))

f = open('input.txt', 'r')
g = open('output.txt', 'w')
c = f.readlines()
n,m = c[0].split()
n,m = int(n), int(m)
tranziti = []
for i in c[1:m+1]:
    j = i[:-1].split()
    tranziti.append((int(j[0]),int(j[1]),j[2],int(j[3])))
initiala = int(c[m+1])
finale = c[m+2].split()
nf = finale[0]
finale = [int(x) for x in finale]
finale.pop(0)
ni = int(c[m+3])
inpt = []
nr = 0
for i in c[m+4:]:
    if nr != ni-1:
        inpt.append(i[:-1])
    else:
        inpt.append(i)
    nr += 1
x = initiala
#x este nodul curent
for i in inpt:
    validare = [0]*len(i)
    #vector caracteristic pentru literele cuvantului
    drum = [initiala]
    x = initiala
    s = ''  #in s pastrez buffer-ul de output
    c = 0
    while c <len(i) and 0 not in validare[:c]:
        #parcurg input-urile
        t = 0
        while t <len(tranziti) and 0 in validare[:c+1]:
            #parcurg tranzitiile
            if tranziti[t][0] == x and tranziti[t][2] == i[c]:
                #daca nodul de unde se pleaca este nodul curent si
                #litera de muchie conicide cu litera curenta din cuvant
                s += str(tranziti[t][3])
                drum.append(tranziti[t][1])
                x = tranziti[t][1]
                #x ia urmatorul nod
                validare[c] = 1
                #validez litera
                if c == len(i)-1:
                    break
            t += 1
        c += 1
    if x in finale:
        print(i + ': ' + 'DA',end='\n',file=g)
        print(s,file=g)
        print(*drum,sep=' ',file=g)
        print(file=g)

    else:

        print(i + ': ', end=' ',file=g)
        print("NU \n",file=g)

f.close()
g.close()





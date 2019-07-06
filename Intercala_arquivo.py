import sys 
import struct

def compara(lineA,lineB):
    tuplaA = estruturaCEP.unpack(lineA)
    tuplaB = estruturaCEP.unpack(lineB)
    CepA=str(tuplaA[cepColumn],'latin1')
    CepB=str(tuplaB[cepColumn],'latin1')

    #print("CepA: %s | CepB: %s" % (CepA,CepB))

    if CepA == CepB:
        return 0
    elif CepA > CepB:
        return 1
    else:
        return -1

estruturaCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
size = estruturaCEP.size
nArq=8
proximo=0


while (proximo +2 <= nArq):
    nameA = "A" + str(proximo) + ".dat"
    nameB = "A" + str(proximo+1) + ".dat" 
    nameSaida = "A" + str(nArq) + ".dat"

    

    A = open(nameA,"rb")
    B = open(nameB,"rb")
    saida = open(nameSaida,"wb")
    A.seek(0,2)
    num_linhasA=A.tell() / 300
    B.seek(0,2)
    num_linhasB=B.tell() / 300
    
    A.seek(0)
    B.seek(0)
    
    linhaA = A.read(size)
    linhaB = B.read(size)
    print("Arquivos abertos %s e %s, criado %s " % (nameA,nameB,nameSaida))
    loop=0
    

    while len(linhaA) == size & len(linhaB) == size:
    
    
        loop+=1
        
        if compara(linhaA,linhaB)>0:
            
            saida.write(linhaB)
            print("B")
            print(linhaB[250::])
            linhaB = B.read(size)
        
        elif compara(linhaA,linhaB)==0:
            saida.write(linhaB)
            saida.write(linhaA)
            print("A")
            print(linhaA[250::])
            print("B")
            print(linhaB[250::])
            linhaB = B.read(size)
            linhaA= A.read(size)
        
        else:

            saida.write(linhaA)
            print("A")
            print(linhaA[250::])
            linhaA= A.read(size)        

    while len(linhaA) == size:
        
        saida.write(linhaA)
        print("A")
        print(linhaA[250::])
        linhaA = A.read(size)
    
    while len(linhaB) == size:
        
        saida.write(linhaB)
        print("B")
        print(linhaB[250::])
        linhaB = B.read(size)
    proximo+=2
    nArq+=1
        
    
A.seek(0,2)
num_linhasA=A.tell() / 300
B.seek(0,2)
num_linhasB=B.tell() / 300
    
A.seek(0)
B.seek(0)    
        
print(num_linhasA)
print(num_linhasB)        
saida.seek(0,2)
tamanho = saida.tell() / 300
print(tamanho)
saida.close()
entrada= open("A14.dat","rb")

for i in range(0 ,80):
    linha = entrada.read(300)
    print (str(linha[252::],'latin1'))
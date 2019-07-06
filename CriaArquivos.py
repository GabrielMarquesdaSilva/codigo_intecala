import random
import struct 

estruturaCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
sizeLine = estruturaCEP.size

f = open("cep_ordenado.dat","rb")
f.seek(0,2)
sizeFByte=f.tell()
numberLines=sizeFByte/sizeLine
print(numberLines)
for i in range(0,8):
    
    name = "A" + str(i) + ".dat"
    A = open(name,"wb")
    RandLine = random.randint(0,numberLines-11)
    f.seek(RandLine*sizeLine,0)
    line= f.read(10*sizeLine)
    A.write(line)

    print("Arquivo %s escrito" % name)
    A.seek(0, 2)
    tamanho = A.tell()
    num_linhas = tamanho / 300
    print(num_linhas)
    A.close()

f.close()
def swapFileData():
    fileToSwap1=input("Enter The Name Of File 1 : ")
    fileToSwap2=input("Enter The Name Of File 2 : ")
    with open(fileToSwap1,'r') as a:
        data_a=a.read()
    
    with open(fileToSwap2,'r') as b:
        data_b=b.read()

    with open(fileToSwap1,'w') as a:
        a.write(data_b)
    
    with open(fileToSwap2,'w') as b:
        b.write(data_a)

swapFileData()
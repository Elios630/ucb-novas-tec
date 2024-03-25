n = int(input("n-ésimo termo da série de Fibonacc: "))

res3 = 0
res0 = 1
resF = 1

for i in range(1,n,1):
    resF = res0 + res3
    res3 = res0
    res0 = resF

print(f"{resF}")
    

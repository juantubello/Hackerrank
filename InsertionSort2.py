arr = [ 8, 7, 6, 5, 4, 3, 2, 1]
print(arr)
leng = len(arr) - 1
print(*arr)

for i in range (1, leng):
    if arr[i] > arr[i + 1]:
         aux = arr[i]
         arr[i] = arr[i + 1]
         arr [i + 1] = aux
    indAux = i
    while (arr[(indAux - 1)] > arr[indAux]): 
         if indAux == 0:
             break   
         aux = arr[indAux]
         arr[indAux] = arr[indAux - 1]
         arr[indAux - 1] = aux
         indAux -= 1
    print(*arr) 
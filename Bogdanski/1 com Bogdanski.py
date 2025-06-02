from sympy import false

Liste=[12,3,7,99,42]
Liste.sort()
n=0
#suche=int(input("Suche:"))
# for i in range(len(Liste)):
#     if Liste[i]==suche:
#         print(i)

# for x, i in enumerate(Liste):
#     if i==suche:
#         print(x)

# for i in Liste:
#     if i==suche:
#         print(n)
#     n+=1

def binary_search(list,suchwert,i_min,i_max):
    if i_min>i_max:
        return -1
    i_middel=(i_min+i_max)//2
    if list[i_middel]==suchwert:
        return i_middel
    if list[i_middel]>=suchwert:
        return binary_search(list,suchwert,i_min,i_middel-1)
    else:
        return binary_search(list,suchwert,i_middel+1,i_middel-1)


print(Liste)
print(binary_search(Liste,99,0,len(Liste)-1))


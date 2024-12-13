import array as arr

numeri_interi = arr.array("i",[1,2,3,4,5,6,7,8,9,10])
v = numeri_interi

# def somma_tot():
#     tot = 0
#     for i in range (0, len(v)):
#         tot+= v[i]
#     return tot

# print(somma_tot())



# numeri_interi.append(11)
# print(numeri_interi)

# numeri_interi.remove(5)
# print(numeri_interi)

for i in range (0, len(v)):
        if (v[i]%2 == 0):
              print(v[i])
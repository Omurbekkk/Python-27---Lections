list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
ccc = []
for o in list_:
    if type(o) == int:
      ccc.append(str(o))
uuu = []
kkk = len(ccc)
for m in range(kkk):
    uuu.append(int(ccc[m]))
print(uuu)
res = []
for x in uuu:
    if type(x) == int:
      res.append(x)
yyy = len(res)
zzz = 0
for i in range(yyy):
    zzz = zzz + res[i]
print(zzz)


# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("The given list is:")
# print(myList)
# list_length=len(myList)
# sumOfElements=0
# for i in range(list_length):
#     sumOfElements=sumOfElements+myList[i]

# print("Sum of all the elements in the list is:", sumOfElements)
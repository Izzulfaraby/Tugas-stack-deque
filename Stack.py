stack = []
#push elemen ke atas
stack.append(10)
stack.append(20)
stack.append(30)
print("stack setelah push:", stack)
#
elemen = stack.pop()
print ("elemen yang di pop:",elemen)
print ("stack setelah pop:",stack)
#pop elemen teratas
if stack:
  print ("elemen teratas:",stack[-1])
else:
  print ("stack kosong")
elemen = stack.pop()
print ("elemen yang di pop:",elemen)
print("stack setelah pop:", stack)

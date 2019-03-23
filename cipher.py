fp = open("key.txt" , 'r', encoding = 'utf-8')
k = fp.readline()
albt = fp.readline()
fp.close()

if k is '' :
    k = 0
else :
    k = int(k)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Changing the position of the alphabet:




j=0
alphabet_new1 = ""

if k == 0:
    for j in range(len(alphabet)) :
        ch_1 = alphabet[j]
        position = alphabet.index(ch_1)
        position = (position + k) % 26
        alphabet_new = alphabet[position]
        alphabet_new1 = alphabet_new1 + alphabet_new
else:
    for j in range(len(albt)) :
        ch_1 = albt[j]
        position = albt.find(ch_1)
        position = (position + k) % 26
        alphabet_new = albt[position]
        alphabet_new1 = alphabet_new1 + alphabet_new

mssg = input(" Enter your message: ")
key = int(input(" Enter the key: "))

i=0
new_mssg1 = ""
print(alphabet_new1)
for i in range(len(mssg)) :
    ch = mssg[i]
    position = alphabet_new1.find(ch)
    position = (position + key) % 26
    print(position)
    new_mssg = alphabet_new1[position]
    new_mssg1 = new_mssg1 + new_mssg

print(" The Encrypted message: ",new_mssg1)

k += key
k = str(k)

fp = open("key.txt" , 'w', encoding = 'utf-8')
fp.write(k)
fp.write("\n")
fp.write(alphabet_new1)
fp.close()

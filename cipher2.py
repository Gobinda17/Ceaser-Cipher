fp = open("key.txt" , 'r', encoding = 'utf-8')
k = fp.readline()
fp.close()

if k is '' :
    k = 0
else :
    k = int(k)
    if k >= 26 :
        k = k % 26

#Changing the position of the alphabet:

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

j = 0
pos = k * 2
n = k

for j in range(len(alphabet)):

    if pos < 25:

        a = alphabet[n]
        alphabet[n] = alphabet[pos]
        alphabet[pos] = a

    pos = (pos + k) % 26
    n = (n + k) % 26
#print(alphabet)

#----***----#

mssg = input(" Enter your message: ")
key = int(input(" Enter the key: "))

i=0
new_mssg1 = ""

for i in range(len(mssg)) :
    ch = mssg[i]
    position = alphabet.index(ch)
    position = (position + key) % 26
    new_mssg = alphabet[position]
    new_mssg1 = new_mssg1 + new_mssg

print(" The Encrypted message: ",new_mssg1)

k += key
key = str(key)
k = str(k)

fp = open("key.txt" , 'w', encoding = 'utf-8')
fp.write(k)
fp.write("\n")
fp.write(new_mssg1)
fp.write("\n")
fp.write(key)
fp.close()

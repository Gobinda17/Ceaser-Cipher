fp = open("key.txt" , 'r', encoding = 'utf-8')
k = fp.readline()
mssg = fp.readline()
key = fp.readline()
fp.close()

x = len(mssg)
mssg1 = mssg[:x-1]

key = int(key)

if k is '' :
    k = 0
else :
    k = int(k)
    if k >= 26 :
        k = k % 26

k -= key

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

i = 0
new_mssg1 = ""

for i in range(len(mssg1)) :
    ch = mssg1[i]
    position = alphabet.index(ch)
    position = (position - key) % 26
    new_mssg = alphabet[position]
    new_mssg1 = new_mssg1 + new_mssg

print("\n The Encrypted message: ", mssg1)
print("\n The Decrypted message: ", new_mssg1)

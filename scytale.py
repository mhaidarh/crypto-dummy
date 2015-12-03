#!/usr/bin/env python

"""
In cryptography, a scytale (rhymes with Italy) is a tool used to
perform a transposition cipher, consisting of a cylinder with a
strip of parchment wound around it on which is written a message.
The ancient Greeks, and the Spartans in particular, are said to
have used this cipher to communicate during military campaigns.

The recipient uses a rod of the same diameter on which he wraps the
parchment to read the message. It has the advantage of being fast
and not prone to mistakes -- a necessary property when on the
battlefield. It can, however, be easily broken. Since the strip of
parchment hints strongly at the method, the ciphertext would have to
be transferred to something less suggestive, somewhat reducing the
advantage noted.
"""

import math

def scytale_encrypt(plain_text, key):
    chars = [c.upper() for c in plain_text if c not in (' ',',','.','?','!',':',';',"'")]
    chunks = math.ceil(len(chars) / float(key))
    inters, i, j = [], 1, 1

    while i <= chunks:
        inters.append(tuple(chars[j - 1:(j + key) - 1]))
        i += 1
        j += key

    cipher, k = [], 0
    while k < key:
        l = 0
        while l < chunks:
            if k >= len(inters[l]):
                cipher.append('+')
            else:
                cipher.append(inters[l][k])
            l += 1
        k += 1

    return ''.join(cipher)


def scytale_decrypt(cipher_text, key):
    chars = [c for c in cipher_text]
    chunks = int(math.ceil(len(chars) / float(key)))
    inters, i, j = [], 1, 1

    while i <= key:
        inters.append(tuple(chars[j - 1:(j + chunks) -1]))
        i += 1
        j += chunks

    plain, k = [], 0
    while k < chunks:
        l = 0
        while l < len(inters):
            plain.append(inters[l][k])
            l += 1
        k += 1

    return ''.join(plain)


def main():
    s = "In cryptography, a scytale (rhymes with Italy) is a tool used to\
perform a transposition cipher, consisting of a cylinder with a\
strip of parchment wound around it on which is written a message.\
The ancient Greeks, and the Spartans in particular, are said to\
have used this cipher to communicate during military campaigns.\
"
    c = scytale_encrypt(s, 4)
    d = scytale_decrypt(c, 4)

    print "String:    %s \n" % (s)
    print "Encrypted: %s \n" % (c)
    print "Decrypted: %s \n" % (d)


if __name__ == '__main__':
    main()


#Given a string, S, of length N that is indexed from 0 to N-1
#Print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.

#Note: 0 is considered to be an even index.

#contsraints: 1<=T<=10, 2<=length S<=100000


for _ in range(int(input())):
    str = input()
    print ('{} {}'.format(str[::2], str[1::2]))

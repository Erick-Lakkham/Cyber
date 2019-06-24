#dechhexbin.py ebl
#import
c1 = 48
c2 = 57
c3 = 65
c4 = 97

t1 = c1
t2 = c2
t3 = c3
t4 = c4

print ("DEC")
print (c1, "\t", c2, "\t", c3, "\t", c4, "\t")

c1 = chr (t1)
c2 = chr (t2)
c3 = chr (t3)
c4 = chr (t4)

print ("\nCONVERT TO ASCII")
print (c1, "\t", c2, "\t", c3, "\t", c4, "\t")
print ("\nCONVERT HEX TO BIN")

c1 = bin (t1)
c2 = bin (t2)
c3 = bin (t1)
c4 = bin (t4)

print (c1, "\t", c2, "\t", c3, "\t", c4, "\t")
print ("\nCONVERT TO HEX")

t1 = hex (t1)
t2 = hex (t2)
t3 = hex (t3)
t4 = hex (t4)

print (t1, "\t", t2, "\t", t3, "\t", t4, "\t")

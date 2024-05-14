
yyx = 2000000000000000000000000000000000000000000000000000000000000
x = 10
y = 0b00000
u = 0o326352
fg = 0x544

test = 4. + .4 + 4e2 + 4e-2

print(0.1+.1+.1)
print(test)

g = True and False

st = 'pepa' + " peepo"

escape = "\""

print(escape)

"""
TOTO JE JEDEN RETEZEC
TEST TEST

"""

print(hex(ord("A"))) # zobrazí 65
print(chr(65)) # zobrazí A

print(int(4.2))

print(float(4))

if isinstance(str(4.2), str):
    print("Yes")

float("4.2")

print(40 + 4.0)

print(0 < 5 < 100)


y = 2000000000000000000000000000000000000000000000000000000000000
print("gsagag")
print(yyx is y)

print (x is y)

x+=1
print (x is y)

g = None

print(g == None)

print(g is not None)

if x == y:
    print("R")

if x == y: print("FFF")
elif x < y: print("faf")
else: print("gfag")

vyp = x - y if x > y else y - x

i = 0

while i < 10:
    print(i)
    i += 1

# největší společný dělitel nenulových kladných čísel x a y
x = 12
y = 8
while x != y:
    if x > y:
        x -= y
    else:
        y -= x
print(f"Největší společný dělitel je {x}")
"""
oit = range(10,0,-2)

for x in oit:
    print(x)
"""
for i in range(10):
    if i == 5:
        continue
    print(i)
listf = [2, "f", "ggfg", "qq", 6. , 6]
 

print


for i in listf:
    print(i)

dicf = {"pepa" : "fafdad", "daf": 4}

print(dicf["pepa"])

F = [("FF", 4), ("FF", 5), ("FF", 6)]
print((F[0]))

for one, two in F:
    print(one, two)

one, two = F[0]

print(one, two)

faf = {55,1,15,5}
print(faf)
list(faf)
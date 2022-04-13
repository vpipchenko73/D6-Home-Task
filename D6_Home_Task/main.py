a={}

for i in range (0,10):
    for j in range (0,4):
        a[i]=j

print(a)

[x*2 for x in range (0,10)]

z={}
z[1] = z.get(1, []) + [345]
z[1] = z.get(1, []) + [555]

z[2] = z.get(2, []) + [345]
z[3] = z.get(3, []) + [555]


print(z)
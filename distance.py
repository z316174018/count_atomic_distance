import numpy as np


def transpose(distance):
    return [list(row) for row in zip(*distance)]

print("开始计算")
m=[]
n=[]
mx = np.loadtxt('Mo.txt',usecols=(2,))
my = np.loadtxt('Mo.txt',usecols=(3,))
mz = np.loadtxt('Mo.txt',usecols=(4,))
sx = np.loadtxt('S.txt',usecols=(2,))
sy = np.loadtxt('S.txt',usecols=(3,))
sz = np.loadtxt('S.txt',usecols=(4,))
ml = len(mx) #Mo的行数
sl = len(sx) #S的行数
distance=[[0 for i in range(sl)] for j in range(ml)] #生成器
distance1=[[0 for i in range(ml)] for j in range(sl)]

for j in range(sl):
    for i in range(ml):        
        distance[i][j]=np.sqrt((mx[i]-sx[j])*(mx[i]-sx[j])+(my[i]-sy[j])*(my[i]-sy[j])+(mz[i]-sz[j])*(mz[i]-sz[j])) #生成的二维列表的索引和生成的数量是反的
np.savetxt(r'distance.xls',distance,fmt='%.2f')
distance1=transpose(distance)

for i in range(ml):
    distance[i].sort()
    for j in range(sl):
        if distance[i][j]>2.7:
          m.append(j)
          break

for i in range(sl):
    distance1[i].sort()
    for j in range(ml):
        if distance1[i][j]>2.7:
          n.append(j)
          break       

np.savetxt(r'number1.txt',m)
np.savetxt(r'number2.txt',n)
print("计算完成")

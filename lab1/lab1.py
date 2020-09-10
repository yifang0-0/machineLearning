# The following line makes sure that when we plot stuff it shows up in the notebook
# comment it out for the plots to show in a different window.
#%matplotlib inline 

import scipy.stats as stats     # Statistics module
import numpy as np              # Module for, among others, matrix operations
import matplotlib.pyplot as plt # Plotting
#import scipy.io as sio         # We don't use this, but it's good to know about: 
                                # allow for the import from, and export to, Matlab files
       

data = np.load("data-2class.npz")
for k in data.keys():
    print(k)
# data中就只有两种标签
d = data['d']
l = data['l'].flatten()
    
# Using matplotlib to plot a heatmap
from matplotlib import mlab
import math
import seaborn as sns


# Your answer to Question 6 comes here


def cal2dnormaldistribution(row,c,type):
    means=np.mean(row , axis=0) #求x1,x2的均值
# 用法：mean(matrix,axis=0)  其中 matrix为一个矩阵，axis为参数
# 以m * n矩阵举例：
# axis 不设置值，对 m*n 个数求均值，返回一个实数
# axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
# axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵
    u1=means[0]
    u2=means[1]
    d=np.std(row,axis=0,ddof=1)
    d1=d[0]
    d2=d[1]
#     ddof : int, optional
# Means Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements. By default ddof is zero.
# 补充自由度相关知识
    x1=np.array(row)[:,0]
    x2=np.array(row)[:,1]
    covxy = np.cov(x1, x2)
    x1max=max(x1)
    x2max=max(x2)
    x1min=min(x1)
    x2min=min(x2)

    xgaussion = np.arange(x1min, x1max, 0.01)
    ygaussion = np.arange(x2min, x2max, 0.01)
    x,y= np.meshgrid(xgaussion,ygaussion)
    r=covxy[0][1]/(d1*d2)
    px=pow((x-u1),2)/pow(d1,2)
    py=pow((y-u2),2)/pow(d2,2)
    pxy=2*r*(x-u1)*(y-u2)/(d1*d2)
    part1=1/(2*math.pi*d1*d2*math.sqrt(1-pow(r,2)))
    part2=np.exp((-1/(2-2*pow(r,2)))*(px-pxy+py))
    z=np.array(part1*part2)
    if type==1:
        ax.plot_surface(x,y,z,color=c)
    elif type==0:
        xheat = np.arange(x1min, x1max, 0.2)
        yheat = np.arange(x2min, x2max, 0.2)
        data = np.random.rand(int((x1max-x1min)/0.2),int((x2max-x2min)/0.2))
#         print(int((x1max-x1min)/0.2),int((x2max-x2min)/0.2))
#         print(len(z),len(z[0]))
               
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][len(data[0])-j-1]=z[j*20][i*20]
        sns.heatmap(data)

        
#第二种操作，将概率密度函数转换为分割区域的热度图数据
#turn the 
    #ax.(x, y, z,color='red')
    #print(z)

color=['r','b']
list0=[]
list1=[]
#q1 
for i in range(len(d)):
    plt.scatter(d[i][0],d[i][1],c=color[int(l[i])],edgecolors='none')
    if l[i]==0:
        list0.append(d[i])
    else :
        list1.append(d[i])
plt.show()


#q2
#你填在这里就好

#q3
from mpl_toolkits.mplot3d import Axes3D    
fig = plt.figure()    
ax = fig.add_subplot(111, projection='3d')
cal2dnormaldistribution(list0,color[0],1)
cal2dnormaldistribution(list1,color[1],1)
plt.show()

#q4
cal2dnormaldistribution(list0,color[0],0)
plt.show()
cal2dnormaldistribution(list1,color[1],0)
plt.show()



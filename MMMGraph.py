import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')
plt.rc('figure',figsize=(16,10))
x=['Mean','Median','Mode']
y1=[22.3913,23.5,23.8]
y2=[58.7,60,60]
y3=[33.8,31.9583333,29.916667]
xi=np.arange(len(x))
barwidth=0.25
plt.bar(xi+barwidth,y1,width=barwidth,label='mean',color='red')
plt.bar(xi,y2,width=barwidth,label='median',color='blue')
plt.bar(xi-barwidth,y3,width=barwidth,label='mode',color='yellow')
plt.legend()
plt.title('Mean,Median,Mode')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.savefig('MMMGraph.jpeg')
plt.show()
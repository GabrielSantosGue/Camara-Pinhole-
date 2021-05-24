import numpy as np
from funciones import miCamaraPinhole
import matplotlib.pyplot as plt

A=(2,0,10)
B=(2,3,13)
C=(2,6,10)
D=(2,3,7)
E=(7,0,10)
F=(7,3,13)
G=(7,6,10)
H=(7,3,7)
matriz=np.array([A,B,C,D,E,F,G,H])
phi=np.array([[20,0],[0,18]])

met=miCamaraPinhole(matriz,phi)

print("Gráfica...")
x=met[0]
y=met[1]*-1
dib=np.array([[x[0],y[0]],
                [x[1],y[1]],
                [x[2],y[2]],
                [x[6],y[6]],
                [x[7],y[7]],
                [x[4],y[4]],
                [x[0],y[0]],
                [x[3],y[3]],
                [x[2],y[2]],
                [x[6],y[6]],
                [x[5],y[5]],
                [x[1],y[1]],
                [x[0],y[0]],
                [x[4],y[4]],
                [x[5],y[5]],
                [x[6],y[6]],
                [x[7],y[7]],
                [x[3],y[3]]])
x1=dib[:,0]
y1=dib[:,1]
plt.plot(x,y,'ro')
plt.plot(x1,y1,'-')
plt.ylim(-12,1)
plt.xlim(0,21)
plt.title('Gráfica')
plt.grid(True) 
plt.show()

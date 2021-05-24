import numpy as np
from funciones import miCamaraPinhole
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A=(2,0,10)
B=(2,3,13)
C=(2,6,10)
D=(2,3,7)
E=(7,0,10)
F=(7,3,13)
G=(7,6,10)
H=(7,3,7)
Phi=np.array([[20,0],[0,18]])


fig=plt.figure()
ax=fig.gca()
def actualizar(i): 
    puntosUVW=np.array([A,B,C,D,E,F,G,H])
    puntosUVW[:,2]=puntosUVW[:,2]+i
    met=miCamaraPinhole(puntosUVW,Phi)
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
    ax.clear()
    ax.plot(x1,y1)
    plt.title('Gráfica')
    plt.grid(True)
    ax.set_xlim(0,21)
    ax.set_ylim(-12,1)

ani=animation.FuncAnimation(fig,actualizar,range(30),interval=0.1,repeat=False)
plt.show()
plt.close()
print("Fin")
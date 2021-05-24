import numpy as np

def miCamaraPinhole(PuntosUVW, Phi):
    u= PuntosUVW[:,0]
    v= PuntosUVW[:,1]
    w= PuntosUVW[:,2]
    fix=Phi[0,0]
    fiy=Phi[1,1]
    x=u*fix
    y=v*fiy
    w1=1/w
    x1=np.round(w1*x)
    y1=np.round(w1*y)
    res=np.array([x1,y1]) 
    return res


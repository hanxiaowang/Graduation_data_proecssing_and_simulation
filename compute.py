import numpy as np

mpart5=np.linspace(100,1000,10)
mpart4=np.linspace(10,100,10)
mpart3=np.linspace(1,10,10)
mpart2=np.linspace(0.1,1,10)
mpart1=np.linspace(0.01,0.1,10)
fins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
# fins=[2,1]
print(fins)
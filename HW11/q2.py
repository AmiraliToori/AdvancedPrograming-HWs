
import matplotlib.pyplot as plt
import numpy as np


num_input = int(input("Please enter the number of plot:"))


match num_input:
    
    case 1:
        ax = plt.figure(figsize = (10, 10)).add_subplot(projection = '3d')


        x = [x for x in np.arange(0, 20, 0.1)]
        y = np.sin(x)
        z = y * np.sin(x)

        ax.scatter(x, y, z, color = 'r')
        ax.set_xticks([x for x in np.arange(0, 21, 2.5)])
        ax.set_yticks([x for x in np.arange(-1, 1.1, 0.25)])


        plt.show()
        
    case 2:
        ax = plt.figure(figsize = (10, 10)).add_subplot(projection = '3d')
        
        z = [x for x in np.arange(0, 15.1, 0.1)]
        x = np.sin(z)
        y = np.cos(z)
        
        ax.plot(x, y, z, color = 'gray')
        ax.set_xticks([x for x in np.arange(-1, 1.1, 0.25)])
        ax.set_yticks([x for x in np.arange(-1, 1.1, 0.25)])
        
        plt.show()
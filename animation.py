# python class that create a gif animation from data points using matplotlib

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Animation:
    def __init__(self, data, interval, xlim, ylim):
        self.data = data
        self.interval = interval
        self.xlim = xlim
        self.ylim = ylim
        self.scatter_list = []
        self.animation = None
    
    def init_figure(self):
        fig, ax = plt.subplots()
        
        ax.set_xlim(-1*self.xlim, self.xlim)
        ax.set_ylim(-1*self.ylim, self.ylim)
        for key in self.data.keys():
            x = self.data[key]['x'][0]
            y = self.data[key]['y'][0]
            self.scatter_list.append(ax.scatter(x, y))
        plt.legend(loc='upper right')
        return fig
    
    def update_figure(self, frame):
        for i, key in enumerate(self.data.keys()):
            x = self.data[key]['x'][frame]
            y = self.data[key]['y'][frame]
            self.scatter_list[i].set_offsets(np.c_[x, y])
        return self.scatter_list
    
    def animate(self):
        fig = self.init_figure()
        self.animation = animation.FuncAnimation(fig, self.update_figure, frames=len(self.data[list(self.data.keys())[0]]['x']), interval=self.interval, blit=True)
        plt.show()
        
    def save(self, filename):
        if self.animation is None:
            self.animate()
        self.animation.save(filename, writer='imagemagick')

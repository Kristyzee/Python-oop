import numpy as np
import matplotlib.pyplot as plt


# Generate random blood sugar data
data = np.random.randint(80, 150, 100)
colors=['red', 'yellow', 'blue']
bins=[80, 100, 125, 150]

class Histogram:
    
    def _init_(self,patches):
        self.colors = colors
        self.bins = ['80-100', '100-125', '125-150']
        self.patches = patches


    def plot_histogram(self, data, patches):
        plt.hist(data, bins=self.bins, colors=self.colors,rwidth=0.98)
        patches = bins.set_facecolor('red'), bins.set_facecolor('yellow'), bins.set_facecolor('blue')
        plt.title('Blood sugar levels of men $ women')

        for patch,color in zip(patches,colors):
            patch.set_facecolor(color) 
        plt.show()

# Create Histogram object
histogram = Histogram()

# Plot histogram
histogram.plot_histogram

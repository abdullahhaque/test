import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5) # assume there are 5 students
y = (20, 35, 30, 35, 27) # their test scores
plt.bar(x,y) # Bar plot
# need to close the figure using show() or close(), if not closed any follow
plt.show() # Try commenting this an run
plt.scatter(x,y) # scatter plot
plt.show()
plt.xlabel('')
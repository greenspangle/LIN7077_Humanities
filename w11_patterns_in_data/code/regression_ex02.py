"""Get or create some data, tidy it up and normalize it"""

# import libraries / modules
# ========================================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# create the raw data (or import it from external files)
# ========================================
xdata = np.array([5, 15, 25, 35, 45, 55])  # a list of 'x' axis values
ydata = np.array([5, 20, 14, 32, 22, 38])  # a list of 'y' axis values

# transform arrays for regression
# ========================================
x = xdata.reshape((-1, 1))  # this reshapes 'x' data to a list of lists
y = ydata

# print the data to check it is OK and to see the 'shape' of it
# ========================================
print('The data for linear analysis')
print('\nraw data')
print('xdata = ', xdata)
print('ydata = ', ydata)
print('\ntransformed data')
print('x = ', x)
print('y = ', y)

# Use linear regression to create model of data
# ========================================
model = LinearRegression()
model.fit(x, y)

# examine properties of the model
# ========================================
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

# Plot the data and regression line
# ========================================
# plot the data
plt.plot(xdata, ydata, ls='', marker='o')
# calculate two data points on the regression line
# two points on the x-axis
yline = np.array([model.intercept_, 55 * model.coef_[0] + model.intercept_])
# two points on the y-axis
xline = np.array([0, 55])
# plot the line
plt.plot(xline, yline)
# add labels for the axes and a chart title
plt.title('Plot of data and "best fit"regression line')
plt.xlabel('x data')
plt.ylabel('y data')
plt.show()

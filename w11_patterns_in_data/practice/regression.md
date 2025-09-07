# Regression 

Finding the line of 'best fit' through your data ponts.
You might have done this at school on two-dimensional X-Y graphs.

Using the mathematics of linear algebra the same problem can be solved for any number of dimensions, dozens
or hundreds or thousands.
Fortunately for us the linear algebra to do this is wrapped up in python libraries so all we have to do is
prepare the data and pass it into the appropriate library functions and the answer 'pops out'.

Once we have the 'best fit' line through our data we can use it to approximate values for missing data
points.

## Regression using the SciKit library
The required libraries are **numpy** for the numerical calculations, **matplotlib** for the plotting of charts and graphs, and **Scikit-Learn** for the linear algebra and regression analysis. 

All of these libraries are already installed in Anaconda, which means they can be imported into your code whenever you need them. 

```python

# import libraries / modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

```

Now, just to get started, create some test data:

```

# create the raw data (or import it from external files)
xdata = np.array([5, 15, 25, 35, 45, 55])
ydata = np.array([5, 20, 14, 32, 22, 38])

# transform arrays for regression
x = xdata.reshape((-1, 1))  # this transforms list into a list of lists
y = ydata

# print the data to check it is are OK and to see the 'shape' of it
print('\nraw data')
print('xdata = ', xdata)
print('ydata = ', ydata)
print('\ntransformed data')
print('x = ', x)
print('x = ', y)

```

Now that we have the data and have transformed it into the correct shape we can use the Scikit-Learn library to calculate the line of best fit.

```

# Do linear regression of data and create model object (line of best fit)
# ========================================
model = LinearRegression()
model.fit(x, y)
```
```
# examine the properties of the model
# ========================================
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
```
```
# Plot the data
# ========================================
# plot the data
plt.plot(xdata, ydata, ls='', marker='o')
```
```

# plot the regression line
# ========================================
# calculate two (x, y) data points on the regression line
# two points on the y-axis
yline = np.array([model.intercept_, 55 * model.coef_[0] + model.intercept_])
# two points on the x-axis
xline = np.array([0, 55])
# and plot the line between those two points
plt.plot(xline, yline)
```
```

# add labels for the axes and a chart title
# ========================================
plt.title('Plot of data and "best fit"regression line')
plt.xlabel('x data')
plt.ylabel('y data')
plt.show()
```

### Categorization

Categorization is the act of grouping the data points into different groups or categories. The groups might
be 'friend' and 'foe'; or profitable-products and loss-making-products; or red-marbles, blue marbles and
green marbles; the possibilities are endless. The key point is that data points in the same category are in
some way related to each other.

Categorization can often be thought of as in some way the inverse of regression. Instead of trying to find a
line
of 'best fit' that is the best approximation to the distribution of the data points, categorization is a
search for the best line that separates the data points into two distinct groups each with some property in
common. In some sense at least that line separating the categories is a line of 'worst possible fit'.







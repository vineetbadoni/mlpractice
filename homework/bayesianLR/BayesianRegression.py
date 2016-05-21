# NOTE: the linear regression model we're trying to solve for is
# given by:
# y = b0 + b1(x) + error
# where b0 is the intercept term, b1 is the slope, and error is
# the error

import pymc as pymc
import numpy as np

b0 = pymc.Normal("b0", 0, 0.0003)
b1 = pymc.Normal("b1", 0, 0.0003)

err = pymc.Uniform("err", 0, 500)

x_weight = pymc.Normal("weight", 0, 1, value=np.array(df_float["weight"]), observed=True)

@pymc.deterministic
def pred(b0=b0, b1=b1, x=x_weight):
    return b0 + b1*x

y = pymc.Normal("y", pred, err, value=np.array(df_float["mpg"]), observed=True)

# put everything we've modeled into a PyMC model
model = pymc.Model([pred, b0, b1, y, err, x_weight])

model.draw_from_prior()
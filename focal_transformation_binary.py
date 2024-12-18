import numpy as np

def focal_transformation_binary(y,gamma):
    num = (y**(gamma))/(1-y)-gamma*(y**(gamma-1))*np.log(1-y)
    den = (y**(gamma))/(1-y)-gamma*(y**(gamma-1))*np.log(1-y)+((1-y)**gamma)/y-gamma*((1-y)**(gamma-1))*np.log(y)
    eta = num/den
    return eta
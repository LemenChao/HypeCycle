#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

# ## create
def create(*x, crest1=50, crest2=25, stp_crest1=0.8, stp_crest2=0.2, midPoint=15, var=10):
    '''
        to create a HypeCycle Data
            x: Input data
            crest1,crest2: Controlling the height of the first wave crest and the second wave crest respectively.
            stp_crest1,stp_crest2: Representing steepness.
            midPoint: The location of the mean value mainly controls the location of the first wave crest.
            var: Displaying moves or penalties for midpoint
            Recommended parameters:crest1=50,crest2=25,stp_crest1=0.8,stp_crest2=0.2,midPoint=15,var=10
            x = np.linspace(0, 50, 5000)
    '''

    x = x

    # If user doesn't submit submit x, it will create a default DataSet.
    if x == ():
        x = np.linspace(0, 70, 5000)
    else:
        x = x[0]

    lf_11 = crest1 / (1 + np.exp(1 * stp_crest1 * (x - midPoint - var)))

    lf_12 = crest1 / (1 + np.exp(1 * stp_crest1 * (x - midPoint)))

    lf_13 = crest2 / (1 + np.exp(1 * stp_crest2 * (x - midPoint - var)))

    hype = lf_11 - lf_12 - lf_13

    return hype




# ## visualize
def visualize(*x, color="red", linewidth=3, linestyle="-"):
    """
     to visualize the hypecycle Data into hypecycle curve

    """
    x = x

    # If user doesn't submit submit x, it will create a default DataSet.
    if x == ():
        x = np.linspace(0, 70, 5000)
    else:
        x = x[0]

    plt.plot(x, create(x), linewidth=linewidth, c=color, linestyle=linestyle)


# ## annotate
def annotate(*x, x_value=20, text="None", color="red", fontproperties='FZShuTi', fontsize=13, alpha=0.8, rotation=3):
    """
     to annaotate the hypecycle curve

    """

    x = x
    # If user doesn't submit submit x, it will create a default DataSet.
    if x == ():
        x = np.linspace(0, 70, 5000)
    else:
        x = x[0]

    plt.plot(x, create(x), linewidth=3)

    x_val = x_value
    t = text
    c = color
    fp = fontproperties
    fs = fontsize
    a = alpha

    plt.rcParams["figure.figsize"] = [12, 6]
    plt.scatter(x_val, create(x_val), color="blue")
    plt.text(x_val, create(x_val), t, color=c, fontproperties=fp, fontsize=fs, alpha=a, rotation=rotation)
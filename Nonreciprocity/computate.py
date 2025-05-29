import numpy as np

def Give_pi(du):
    hu=du/180
    return hu

def Give_delta(fre,voltage):
    deltass = [45, 45, 50]
    delta = 0.97 * voltage / deltass[fre]
    return delta

def Give_pi_verse(hu):
    du=hu*180
    return du

def Give_delta_verse(fre,delta):
    deltass = [45, 45, 50]
    voltage=delta*deltass[fre]/0.97
    return voltage


hu=1
fre=1
delta=1

a=Give_pi_verse(0.54)
print(a)

b=Give_delta_verse(fre,0.97)
print(b)

c=Give_pi(110)
print(c)

d=Give_delta(fre,70)
print(d)
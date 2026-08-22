from scipy import *
from numpy import *
from scipy.integrate import odeint, ode
import matplotlib.pyplot as plt
pi=3.14
g, L, m = 9.82, 1., 1.
def dx(x,t):
    """
    The right-hand side of the pendulum ODE
    x=[x1,x2,x3,x4]
    """
    
    x1,x2,x3,x4 = x # x is array
    c1 = 1/(m*L**2)
    ccx = cos(x1-x2)
    ddx = 6.*c1/(16.-9.*ccx**2)
    dx1 = ddx*(2*x3-3*ccx*x4)
    dx2 = ddx*(8*x4-3*ccx*x3)
    ddy = dx1*dx2 * sin(x1-x2)
    dx3 = -0.5/c1 * ( ddy + 3*g/L * sin(x1))
    dx4 = -0.5/c1 * (-ddy + g/L * sin(x2))
    return array([dx1,dx2,dx3,dx4])


x0=[pi/2,pi/4,0,0]
t=linspace(0,100,1000)

x=odeint(dx,x0,t)

# plot the angles as a function of time
fig, axes = plt.subplots(1,2,figsize=(12,4))
axes[0].plot(t, x[:, 0], label="theta1")
axes[0].plot(t, x[:, 1], label="theta2")
axes[0].legend(loc='best')
axes[0].set_xlabel('time')

L = 0.5
x1 =  L * sin(x[:, 0])
y1 = -L * cos(x[:, 0])

x2 = x1 + L * sin(x[:, 1])
y2 = y1 - L * cos(x[:, 1])
    
axes[1].plot(x1, y1, label="pendulum1")
axes[1].plot(x2, y2, label="pendulum2")
axes[1].set_ylim([-1, 0])
axes[1].set_xlim([-1, 1])
axes[1].legend(loc='best')
plt.show()

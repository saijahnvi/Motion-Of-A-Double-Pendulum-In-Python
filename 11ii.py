from scipy import *
from numpy import *
from scipy.integrate import odeint, ode
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
    ddx = 6.*c1/(16.-9.*ccx**2)#eqs for angular velocities and momenta
    dx1 = ddx*(2*x3-3*ccx*x4)
    dx2 = ddx*(8*x4-3*ccx*x3)
    ddy = dx1*dx2 * sin(x1-x2)
    dx3 = -0.5/c1 * ( ddy + 3*g/L * sin(x1))
    dx4 = -0.5/c1 * (-ddy + g/L * sin(x2))
    return array([dx1,dx2,dx3,dx4])


x0=[pi/2,pi/4,0,0]
t=linspace(0,100,1000)
dt=t[1]-t[0]

x=odeint(dx,x0,t)

L = 0.5
x1 =  L * sin(x[:, 0])
y1 = -L * cos(x[:, 0])

x2 = x1 + L * sin(x[:, 1])
y2 = y1 - L * cos(x[:, 1])

fig, ax =plt.subplots(1,1)
ax.set_xlim(-2*L,2*L)
ax.set_ylim(-2*L,2*L)

ax.grid()
line, =ax.plot([] ,[] ,'-o',lw=2) #ois the shape of the edge
time_template='time=%.1fs'#shows time 
time_text=ax.text(0.05,0.9,'', transform=ax.transAxes)
def init():
    line.set_data([],[])#used for blit=true otherwise just comment out this func and set init_func to none
    time_text.set_text('')
    return line,time_text

def animate(i):
    thisx=[0,x1[i],x2[i]]
    thisy=[0,y1[i],y2[i]]

    line.set_data(thisx,thisy)
    time_text.set_text(time_template%(i*dt))
    return line,time_text


ani=animation.FuncAnimation(fig,animate,arange(1,len(t)),interval=70, init_func=init, blit=False)#blit is false means we are replotting everything and true is updating imp things
plt.show()
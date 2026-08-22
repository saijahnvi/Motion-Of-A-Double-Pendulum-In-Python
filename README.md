# Motion-Of-A-Double-Pendulum-In-Python
A modern Python simulation of non-linear double pendulum dynamics derived via Lagrangian mechanics and solved using SciPy's solve_ivp. It models non-linear angular momentum equations to illustrate real-time chaotic trajectories and extreme sensitivity to initial conditions.

## Overview

This repository contains a Python implementation of a two-body double pendulum system. The equations of motion are derived using **Lagrangian Mechanics** ($L = T - V$) and expressed through generalized coordinates ($\theta_1, \theta_2$) and their conjugate momenta ($p_1, p_2$). The resulting non-linear differential equations are integrated numerically through the odeint function in scipy.integrate

## Demo & Visualizations

<!-- Static Preview Image -->
<img width="1094" alt="Double Pendulum Preview" src="https://github.com/user-attachments/assets/a79be2f8-30f8-4edb-bad2-9a34fab94bbc" />

*Real-time simulation showing the trajectory trace of the secondary mass.*

---

<!-- Video Demonstration -->
### Simulation in Action

https://github.com/user-attachments/assets/4477d603-eeb9-476b-99ca-1918a4045af3

## Key Technical Highlights

* **Lagrangian Physics Engine:** Formulated from Euler-Lagrange equations without small-angle approximations to capture full non-linear chaotic dynamics.
* **Real-Time Animation:** Uses `matplotlib.animation.FuncAnimation` with blitting enabled for smooth frame rendering.
* **Dynamic Trajectory Tracing:** Renders a trailing trace on the secondary bob to visually map chaotic motion paths over time.

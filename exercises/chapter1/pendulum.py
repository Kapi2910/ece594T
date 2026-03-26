import numpy as np
import matplotlib.pyplot as plt

# Parameters.
m = 1 # mass
g = 10 # gravity
l = .1 # length
h = .0001 # discretization step
T = 2 # time horizon

# Control policy: given the state, returns the control input.
def pi(x):
    ### YOUR CODE HERE
    ### YOUR CODE HERE
    ### YOUR CODE HERE
    return 0

# Closed-loop dynamics.
def f(x):
    return np.array([
        x[1], # angular velocity
        (m * g * l * np.sin(x[0]) + pi(x)) / (m * l ** 2)]) # angular acceleration

# Plot trajectories for different initial angles. Usese explicit Euler for the
# simulation.
plt.figure()
K = int(T / h) # time steps in discrete-time simulation
traj = np.zeros((K, 2)) # matrix of states
for q0 in np.pi * np.arange(6) / 5: # loop through multiple initial angles
    traj[0] = [q0, 0] # set initial state
    for k in range(K - 1):
        traj[k + 1] = traj[k] + h * f(traj[k]) # explicit Euler
    plt.plot(
        traj[:,0], # angle
        traj[:,1], # angular velocity
        label=fr'$q_0={np.round(q0, 2)}$')

# Plot options.
plt.xlabel(r'Angle $q$')
plt.ylabel(r'Angular velocity $\dot q$')
plt.title('Pendulum trajectories')
plt.legend()
plt.grid()
plt.show()
# Question 1.1
(a) To solve the following differential equation, we can see that it is a separable differential equation.
$$\dot x(t) = x(t)^{\frac{1}{3}};\ x(0)=0$$
For visual clarity, I will be writing $x(t) \equiv x$ 
 $$
 \begin{align*}
 \frac{dx}{dt} &= x^{\frac{1}{3}}\\
 \int x^{-\frac{1}{3}}dx &= \int dt;\ \text{(rearranging and integrating both sides)}\\
 \frac{3x^{\frac{2}{3}}}{2} = t - C\\
  x &= \Bigl(\frac{2}{3}(t-C)\Bigr)^{\frac{3}{2}};\ \text{(isolating $x$)}\\
 \end{align*}
 $$
 Plugging in the initial conditions $x(0)=0$, we get that $C=0$
 $$
 \therefore x(t) = \Bigl(\frac{2t}{3}\Bigr)^{\frac{3}{2}}
$$
is a valid solution for the given differential equation. But we can see that $x(t) \equiv 0$ is another valid solution, albeit trivial.

(b) The given different equation is not the Lipschitz Continuous in state. To see this, let us define a sequence $x_n = n for $n \in [0,1]$ and $y_n = 0$
now the rate of change of the function on this sequence $f(x_n) = n^{\frac{1}{3}}$ $$\frac{|f(x_n) - f(y_n)|}{|x_n - y_n|} = \frac{n^{\frac{1}{3}}}{n} = n^{\frac{-2}{3}}$$
The limit of this sequence as $n \rightarrow 0$ is $\infty$,  proving that rate of change is unbounded at $0$ 
Hence, the function $f(x) = x^{\frac{1}{3}}$ is not Lipschitz continuous

# Question 1.2
For this problem, I chose the following $f(x) = -x$
In the continuous-time case, 
$\dot x = f(x) = -x \implies \varphi(t;x_0)=x_0 e^{-t}$
Taking the limit, $\lim\limits_{t \rightarrow \infty}\varphi(t;x_0) = 0$  

In the discrete-time case, $h = 2.5$
$\tilde f(x) = x + hf(x) = (1-h)x = -1.5x$ 
This means the difference equation is $x(k+1) = -1.5x(k)$ which is the recursive definition of a geometric series with initial value is $x_0$ and common ratio $-1.5$. 
Hence, the discrete-time solution is $\tilde \varphi(k;x_0) = x_0(-1.5)^k$
Taking the limit, $\lim\limits_{k \rightarrow \infty}|\tilde \varphi(k;x_0)| = \infty$ as $|-1.5| > 1$ 

Hence for the for $f(x) = -x;\ h=2.5$ the continuous-time solution converges for all initial conditions whereas the discrete-time solution diverges for all non-zero initial conditions

# Question 1.3

(a) I am implementing the time-invariant control policy as a function of the residual between the equilibrium state and current angle. 

For this, I first find nearest closest integer multiple to $2\pi$ as follows 
$$
k = \text{round}\Big(\frac{q_0(t)}{2\pi} \Big)
$$
Then I calculate the residual from the current position as $e(t) = 2k\pi - q_0(t)$.
Finally, the control policy $$u(t) = K_p e(t) + K_d \dot e(t)$$ where $K_p$ and $K_d$ are the proportional and derivative gains which drive the system to the desired equilibrium state.

# Question 1.4
Given the following for the planar quadrotor
$$
\begin{align}
& \frac{\ddot q_1(t)}{\ddot q_(t) + g} = -\tan(q_3(t))  
\end{align}
$$
(a) Given $q_3(0) = q_3(T) = 0$, then this implies that when $t \in \set{0,T}$
$$
\begin{align*}
\frac{\ddot q_1(t)}{\ddot q_(t) + g} &= 0, (\text{ as} \tan(t) = 0)\\
\implies \ddot q_1(t) &= 0, (\text{ as denominator cannot be zero})
\end{align*}
$$
Therefore $q_1(t)$ has **zero acceleration** at the initial and final locations
(b)  We first take the time derivative of eq. 1.20 from the text
$$
\begin{align*}
\frac{d}{dt}\Big(\frac{\ddot q_1(t)}{\ddot q_(t) + g} &= -\tan(q_3(t))\Big) \\
\frac{\dddot q_1(t)}{\ddot q_(t) + g} + \Big(\frac{-\ddot q_1(t)}{\ddot q_(t) + g}\Big)\cdot\frac{\dddot q_2(t)}{\ddot q_(t) + g} &= -\dot q_3(t)(1+\tan^2(q_3(t))) \\
\frac{\dddot q_1(t)}{\ddot q_(t) + g} + \Big(\tan(q_3(t))\Big)\cdot\frac{\dddot q_2(t)}{\ddot q_(t) + g} &= -\dot q_3(t)(1+\tan^2(q_3(t))) \\
\end{align*}
$$
Given $\dot q_3(0) = \dot q_3(T) = 0$, then this implies that when $t \in \set{0,T}$
$$
\begin{align*}
\frac{\dddot q_1(t)}{\ddot q_(t) + g} + 0\cdot\frac{\dddot q_2(t)}{\ddot q_(t) + g} &= 0 , (\text{ as} \tan(t) = 0)\\
\implies \dddot q_1(t) &= 0, (\text{ as denominator cannot be zero})
\end{align*}
$$
Therefore $q_1(t)$ has **zero jerk** at the initial and final locations





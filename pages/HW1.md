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





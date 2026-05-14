# Question 3.2
(a) The given problem can be expressed as QP as follows. 
I defined the vector $\mathbf{e_2} = \begin{bmatrix}0&1\end{bmatrix}^\top$  matrix $\mathbf{Q}$ by stacking the vectors $\mathbf{q_i}$ and 
matrix $D=\begin{bmatrix} -1 & 1 & 0 & \cdots & 0 \\ 0 & -1 & 1 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & -1 & 1 \end{bmatrix}$ 

$$
\begin{align}
\text{min }& mg\cdot\mathbb{1}_n^\top\mathbf{Q}\mathbf{e_2} + \frac{k}{2}\texttt{tr}(\mathbf{DQ (DQ)^\top})\\
\text{s.t. }& \mathbf{q_1}= (0,1) \tag{1}\\
& \mathbf{q_n}= (n-1,1) \tag{2}\\
& q_{i,2} \geq 0\tag{3}
\end{align}
$$
(b) 36 masses are in contact with the ground at equilibrium
(c) The dual variables should be the restoring forces on the springs. This makes intuitive sense as the spring obeys hooks law which states $F \propto x$ or $F = -kx$. In the current problem, we are optimizing the positions, but I guess we could get the same result if we instead optimized for restoring forces.

---
# Question 4.1
The QCQP problem can be posed as follows 
$$
\begin{align}
\text{min }& t \\
\text{s.t. }& x_1^2\leq t \tag{1}\\
& x_2+3\leq t \tag{2}\\
& x_1(1-x_1) \leq 0 \tag{3}\\
& x_1(x_1-1) \leq 0 \tag{4}\\
& -x_1-x_2^2 \leq 1 \tag{5}
\end{align}
$$
In this formulation, I introduced a new variable $t$. Constraints $(1)$ and $(2)$ capture the $\max\{\}$ function. Constraints $(3)$ and $(4)$ enforce that $x_1$ is binary. In order to enforce $x_1^3+x_2^2 \geq 1$, I used the fact that $x_1^3$ and $x_1$ are equivalent when $x_1$ is binary, which allows me to write constraint $(5)$. 

I would like to note that I wrote all the equations 
## 1

### (a)

$k_j^\top q >> k_i^\top q, i\neq j$

### (b)

$q = C(k_a+k_b)$ where $C$ is a large number.

### (c)

i.

$q = C(k_a+k_b)$ where $C$ is a large number.

The variance of each $k_i$ is small, so this will work like the case in (b)

ii.

$c$ may be closer to $v_a$ or $v_b$ depending on the norm of $k_a$.

### (d)

i.

$q_1 = Ck_a, q_2=Ck_b$ where $C$ is a large number

ii.

$c$ will always be approximately $\frac{1}{2}(v_a+v_b)$.

As long as $C$ is large enough, $c_1$ will be approximately $v_a$ no matter what $||k_a||$ is.

And, $c_2$ will be approximately $v_b$.

### (e)

i.

$x_1^\top x_2=0$

$x_2^\top x_2=\beta^2$

$x_3^\top x_2=0$

$c_2=x_2=u_a$

If $x_2=u_a+u_d$:

$x_1^\top x_2=\beta^2$

$x_2^\top x_2=2\beta^2$

$x_3^\top x_2=0$

$c_2\approx x_2=u_a+u_d$

If $x_2=u_a+u_c$:

$x_1^\top x_2=0$

$x_2^\top x_2=2\beta^2$

$x_3^\top x_2=\beta^2$

$c_2\approx x_2=u_a+u_c$

So, it is impossible for $c_2$ to approximate $u_b$ by adding either $u_d$ or $u_c$ to $x_2$.

ii.

$V=\frac{1}{\beta^2}(u_bu_b^\top-u_cu_c^\top)$, so $v_1=u_b,v_2=0,v_3=u_b-u_c$

$Q=u_au_a^\top+u_du_d^\top$, so $q_1=\beta^2u_d,q_2=\beta^2u_a,q_3=0$

$K=u_du_c^\top+u_au_d^\top$, so $k_1=\beta^2u_a,k_2=0,k_3=\beta^2u_d$

Then, $\alpha_1\approx[0,0,1],\alpha_2\approx[1,0,0]$

$c_1\approx v_3=u_b-u_c,c_2\approx v_1=u_b$

## 2

### (d)

model’s accuracy: 5.0 out of 500.0: 1.0%

London baseline: 4.55%


Implemented and compared three option pricing methods in Python - **Black-Scholes, Binomial Tree and Monte Carlo Simulation**.


I did this to better understand the trade-offs between analytical, discrete, and simulation-based approaches to derivatives pricing, and demonstrate convergence behaviour - a core numerical methods problem in quantitative finance.

Each method was implemented independently in Python and tested against some fixed inputs
(spot = strike = £100, time to expiry = 1 year, risk free rate - 5%, volatility = 20%):

**Black-Scholes** - I computed this directly via the closed-form formula, and this was used as the true value and benchmark for the other 2 methods.

**Binomial Tree (Cox-Ross-Rubenstein)** - I built a recombining tree of up/down price movements against a variable number of steps, and then computed the final option price via backward induction. I discounted expected payoffs at each node using risk-neutral probabilities.

**Monte Carlo Simulation** - I simulated a configurable number of random terminal stock prices, consistent with standard option-pricing assumptions, computed the payoff value for each and discounted the average payoff back to today's value.

To evaluate the convergence, both Binomial and Monte Carlo were run with step counts from 5 to 500 for the tree, and simulation counts from 100 to 100,000 for Monte Carlo (I also averaged each simulation over 10 runs to reduce noise from random generation). 
I plotted the absolute-error against the Black-Scholes price on a log-scaled x-axis to visualise the convergence behaviour, as shown below.

I found that the Binomial Tree converged to within 0.04% of the Black-Scholes price at 500 steps, while Monte Carlo reached only 0.4% error at 100,000 simulations - indicating binomial converges much faster and cheaper than Monte Carlo and is therefore the better choice for this type of option.
<p align="center">
    <img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/208fad36-4944-4672-9223-815840d2bd24" />
<\p>

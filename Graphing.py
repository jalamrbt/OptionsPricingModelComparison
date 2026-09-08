import matplotlib.pyplot as plt
import Convergence as conv

steps = conv.stepCounts
simulations = conv.simulationCounts

binomialResults = conv.testBinomial()
monteCarloResults = conv.testMonteCarlo()



xpointsm = simulations
ypointsm = monteCarloResults
plt.subplot(1,2,1)

plt.plot(xpointsm,ypointsm)
plt.ylabel("Absolute Error from Black-Scholes")
plt.xlabel("Simulation Count")
plt.xscale("log")

plt.title("Monte Carlo Error with\n increasing Step Count",wrap=True)


xpointsb = steps
ypointsb = binomialResults
plt.subplot(1,2,2)
plt.plot(xpointsb,ypointsb)

plt.xscale("log")
plt.xlabel("Step Count")

plt.title("Binomial Tree Error with increasing Step Count",wrap=True)


plt.tight_layout()
plt.show()
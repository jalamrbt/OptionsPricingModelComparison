import math
import numpy as np

def finalStockPrice(spot, riskFreeRate,volatility,time,z):
    S_T = spot * math.exp((riskFreeRate-0.5*volatility**2)*time +volatility*math.sqrt(time)*z)
    return S_T

def overallPayoff(riskFreeRate, time, payoffs ):
    price = math.exp(-riskFreeRate*time) * (sum(payoffs)/len(payoffs))
    return price

def monteCarlo(spot,riskFreeRate,volatility,time,strike,N):
    newList = []
    for i in range(0,N):
        z= np.random.normal(0,1)
        price = finalStockPrice(spot,riskFreeRate,volatility,time,z)
        payoff = max(price - strike,0)
        newList.append(payoff)
    return overallPayoff(riskFreeRate,time,newList)


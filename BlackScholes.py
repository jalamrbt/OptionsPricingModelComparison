from scipy.stats import norm
import math

def N(zScore):
    return norm.cdf(zScore)
def d1(spot,strike,timeToExpiration,riskFreeRate,volatility):
    return (math.log(spot/strike)+(riskFreeRate+math.pow(volatility,2)/2)*timeToExpiration)/(volatility*math.sqrt(timeToExpiration))
def d2(spot,strike,timeToExpiration,riskFreeRate,volatility):
    return (math.log(spot/strike)+(riskFreeRate-math.pow(volatility,2)/2)*timeToExpiration)/(volatility*math.sqrt(timeToExpiration))
    

def blackScholesCall(spot,strike,timeToExpiration,riskFreeRate,volatility):
    callPrice = spot*N(d1(spot,strike,timeToExpiration,riskFreeRate,volatility))-strike*math.exp(-riskFreeRate*timeToExpiration)*N(d2(spot,strike,timeToExpiration,riskFreeRate,volatility))
    return callPrice

def blackScholesPut(spot,strike, timeToExpiration,riskFreeRate,volatility):
    putPrice = strike*math.exp(-riskFreeRate*timeToExpiration)*N(-d2(spot,strike,timeToExpiration,riskFreeRate,volatility)) - spot*N(-d1(spot,strike,timeToExpiration,riskFreeRate,volatility))
    return putPrice




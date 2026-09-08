import math

def binomial(timeToExpiration, steps, volatility, riskFreeRate):
    stepTime = timeToExpiration/steps
    u = math.exp(volatility*math.sqrt(stepTime))
    d= 1/u
    p = (math.exp(riskFreeRate*stepTime)-d)/(u-d)

    vals = [u,d,p,stepTime]
    return vals


def outcomes(spot, u, d ,steps):
    prices = []
    for j in range (0,steps+1):
        prices.append(spot * (u**j) * (d**(steps-j)))
    return prices

def getPayoffs(prices,strike):
    finalPrices = []
    for i in prices:
        finalPrices.append(max(i-strike,0))
    return finalPrices

def collapse(payoffs,p,riskFreeRate,stepTime):
    newList=[]
    i=0
    j=1
    for x in range(0,len(payoffs)-1):
        while i<len(payoffs)-1:
            newList.append( math.exp(-riskFreeRate*stepTime)* (p*payoffs[j] + (1-p) * payoffs[i]))
            i+=1; j+=1
        if i == len(payoffs)-1:
            payoffs = newList
            i=0; j=1
            newList=[]
    return payoffs[0]

def runBinomial(timeToExpiration, steps, volatility, riskFreeRate,spot,strike):
    vals =binomial(timeToExpiration,steps,volatility,riskFreeRate)
    prices = outcomes(spot,vals[0],vals[1],steps)
    payoffs = getPayoffs(prices,strike)
    return collapse(payoffs,vals[2],riskFreeRate,vals[3])
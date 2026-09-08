import BinomialTree as bt
import BlackScholes as bs
import MonteCarlo as mc


timeToExpiry =1
riskFreeRate = 0.005
volatility = 0.2
spot =100
strike = 100
stepCounts = [5,10,15,20,25,50,100,150,200,500]
simulationCounts = [100,1000,10000,100000]

blackScholesResult = bs.blackScholesCall(spot,strike,timeToExpiry,riskFreeRate,volatility)

def testBinomial():

    errors =[]
    for i in stepCounts:
        binomialResult = bt.runBinomial(timeToExpiry,i,volatility,riskFreeRate,spot,strike)
        binomialError = abs(binomialResult - blackScholesResult)
        errors.append(binomialError)

    return errors

def testMonteCarlo():
    mcResults=[]
    for i in simulationCounts:
        errors = []
        for x in range(0,10):
            price= mc.monteCarlo(spot,riskFreeRate,volatility,timeToExpiry,strike,i)
            mcError = abs(price -blackScholesResult)
            errors.append(mcError)
        mcResults.append(sum(errors)/len(errors))
    return mcResults
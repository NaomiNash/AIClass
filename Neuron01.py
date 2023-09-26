#!/usr/bin/env python3

''' Neuron01.py - Naomi Nash - Saint Leo University
    - 7 Feb 2022 - Simple Neuron Simulation '''

import math
import statistics
import random

global bias
global rate
global weights

# -----------------------------------------------------------------------------
def reportTrainingData(myIns, myOuts) :
    ''' Prints out the data set '''
    print('REPORT OF TRAINING DATA')
    
    print(F"{'N':^5} {'Inputs':^20} Output")
    for i in range(0,len(myIns)) :
        print(F"{i:^5}",F"{str(myIns[i]):^20}", myOuts[i])
    print('END OF REPORT OF TRAINING DATA')
    print()
    
# -----------------------------------------------------------------------------
def buildRandomList(mySize, value=None) :
    ''' Returns a list of mySize items, equal to value or random numbers
        between 0 and 1 if value is None '''
    retVal = list()
    for i in range(0,mySize):
        if value is None :
            retVal.append(random.random())
        else :
            retVal.append(value)
    return retVal

# -----------------------------------------------------------------------------
def reportNeuron(bias, weights, rate) :
    ''' Reports the status of the Neuron '''
    print("REPORT OF NEURAL CONFIGURATION")
    print(' '*5,F"Rate: {rate:<10.8f}")
    print(' '*5,F"Bias: {bias:<15.8f}")
    print(' '*5,"Weights: ")
    for i in range(0,len(weights)) :
        print(' '*5,F"{i:^5}: {weights[i]:<10.8f}")
    print("END REPORT OF NEURAL CONFIGURATION")
    print()

# -----------------------------------------------------------------------------
def activation(x) :
    '''  Activation function for Neuron '''
    # Hyperbolic tanget
    # retVal = math.tanh(x)

    # Logistic Function
    # retVal = 1.0 / (1+math.exp(-1.0*x))

    # Perceptron Threshold Function
    retVal = 0
    if (x >= 0.5) :
        retVal = 1
    return retVal

# -----------------------------------------------------------------------------
def computeForward(inList) :
    ''' Compute the output of the Neuron for this input '''
    global weights
    global bias
    
    sum = bias
    for i in range(0,len(inList)) :
        sum = sum + (inList[i] * weights[i])
        # Takes inputs, weights, and bias to return an output
    return activation(sum)

# -----------------------------------------------------------------------------
def reportValues(inList, outList) :
    myErrors = list()
    print("REPORT OF TEST VALUES")
    print('N    INPUT            TARGET     CURRENT   ERROR')

    for i in range(0,len(inList)) :
        current = computeForward(inList[i])
        error = outList[i] - current
        myErrors.append(abs(error))
        print(F"{i:<4} {str(inList[i]):10}",
              F"{outList[i]:>5} {current:>10} {error:>10}")

    print("MEAN ABSOLUTE ERROR:", statistics.mean(myErrors))
    print("STANDARD DEVIATION OF ERROR:",statistics.stdev(myErrors))
    print("END OF REPORT OF TEST VALUES")
    print()
# -----------------------------------------------------------------------------
def computeNewWeight(inValue, error, oldWeight, rate) :
    ''' Compute new weight, smaller if error is negative, larger if the
    error is positive, same size if the input is zero '''
    return oldWeight + (rate * error * inValue)

# -----------------------------------------------------------------------------
def reportLine(index, epoch, current, error) :
    print(F"i:{index:<5} epoch:{epoch:<5}" +
          "current:{current:<5} error: {error:<5})")

# -----------------------------------------------------------------------------
def trainForSingleValue(index, inList, target) :
    ''' Trains the neuron for a single input set '''
    global bias
    global weight
    global rate

    VERBOSE = True
    threshold = 0.01
    epoch = 0
    current = computeForward(inList)
    error = target - current
    
    if(abs(error) <= threshold) :
        if VERBOSE :
            print(index, epoch, current, error)
    else :
        while (abs(error)>threshold) and (epoch<200) :
            epoch = epoch + 1
            current = computeForward(inList)
            error = target - current
            for i in range(len(inList)) :
                weights[i] = computeNewWeight(inList[i], error, weights[i], rate)
            bias = computeNewWeight(inList[i], error, bias, rate)
            
            if VERBOSE :
                print(index, epoch, current, error)
       
# -----------------------------------------------------------------------------
def trainOverSet(inData, targets, sequential=False) :
    ''' Trains the neuron using all data in the data set
    By default, shuffle the order, or scan in order if sequantial is set
    to True '''
    if(sequential) :
        for i in range(0, len(inData)) :
            trainForSingleValue(i, inData[i], targets[i])
    else :
        roster = [i for i in range(1,16)]
        random.shuffle(roster)
        for j in roster :
            trainForSingleValue(j, inData[j],targets[j])
        
# -----------------------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------------------
if (__name__ == '__main__') :
    global bias
    global weights
    global rate

    # Set up training data
    
    trainingInputs = [((i&8)//8,(i&4)//4,(i&2)//2,(i&1)//1) for i in range(0,16)]
        # Gives random numbers from 0 to 8 and then gives the duplics of values
    trainingOutputs = [0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1]
    reportTrainingData(trainingInputs, trainingOutputs)

    # Set up Neuron data structures
    rate = 0.1
    bias = random.random()
    weights = buildRandomList(len(trainingInputs[0]))
    reportNeuron(bias, weights, rate)

    reportValues(trainingInputs, trainingOutputs)

    trainOverSet(trainingInputs, trainingOutputs)
    reportNeuron(bias, weights, rate)

    reportValues(trainingInputs, trainingOutputs)

    
# -----------------------------------------------------------------------------

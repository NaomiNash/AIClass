#!/usr/bin/env Python3

''' Plants.py - Naomi Nash - Saint Leo University - April 2022 '''

import csv
import re

global subjects
global predicates
global facts
global header

# ---------------------------------------------------------
''' Cleans and reformats the lines of the file '''
def cleanFileLine(myList) :
    truePattern = re.compile('[T|t]rue')
    falsePattern = re.compile('[F|f]alse')
    intPattern = re.compile('[-|+]?[0-9]+$')
    floatPattern = re.compile('[-|+]?[0-9]+[.][0-9]+$')
    
    for i in range(0,len(myList)) :
        if type(myList[i]) is str :
            myList[i] = myList[i].strip()
            #myList[i] = myList[i].capitalize() *****
            if truePattern.match(myList[i]) :
                myList[i] = True
            elif falsePattern.match(myList[i]) :
                myList[i] = False
            elif myList[i] in ['None','none','','#N/A'] :
                myList[i] = False
            elif intPattern.match(myList[i]) :
                myList[i] = int(myList[i])
            elif floatPattern.match(myList[i]) :
                myList[i] = float(myList[i])

# ----------------------------------------------------------
''' Loads the data into the Plants.CSV file '''
def loadData(subjects,predicates,facts,header) :
    
    myFile = open('Plants.CSV', 'r')
    myReader = csv.reader(myFile)
    header.clear()
    header.extend(next(myReader))
    cleanFileLine(header)
    
    for dataLine in myReader :
        cleanFileLine(dataLine)
        
        # Get index of Subject
        if dataLine[0] in subjects :
            subjectIndex = subjects.index(dataLine[0])
        else:
            subjects.append(dataLine[0])
            subjectIndex = len(subjects)-1

        if dataLine[1] in predicates :
            predicateIndex = predicates.index(dataLine[1])
        else:
            predicates.append(dataLine[1])
            predicateIndex = len(predicates)-1
        myFact = (subjectIndex,predicateIndex,dataLine[2])
        facts.append(myFact)    

    myFile.close()

# ----------------------------------------------------------
''' Saves the data in the Plants.CSV file '''
def saveData(subjects,predicates,facts,header) :
    myFile = open('Plants.CSV', 'w', newline='')
    myWriter = csv.writer(myFile)
    myWriter.writerow(header)
    for myFact in facts :
        if myFact[2] is not None :
            myRow = [subjects[myFact[0]],predicates[myFact[1]],myFact[2]]
            myWriter.writerow(myRow)
    myFile.close()

# ----------------------------------------------------------
''' Compiles the users answers to the questions '''
def yesNoQuestion(myString) :
    retVal = None
    truePattern = re.compile('[T|t][rue]?')
    yesPattern = re.compile('[Y|y][es]?')
    falsePattern = re.compile('[F|f][alse]?')
    noPattern = re.compile('[N|n][o]?')
    
    while retVal is None :
        userInput = input(myString)
        if truePattern.match(userInput) :
            retVal = True
        elif falsePattern.match(userInput) :
            retVal = False
        elif yesPattern.match(userInput) :
            retVal = True
        elif noPattern.match(userInput) :
            retVal = False

    return retVal

# ---------------------------------------------------------
def getFirstUnAsked(questions) :
    ''' Return -1 if all elements are True or False,
        otherwise return the index of the first entry which
        is none '''
    retVal = -1
    if None in questions :
        retVal = questions.index(None)
    return retVal

# ---------------------------------------------------------
''' Test retVal to false if the fact is not in the fact table '''
def isNotInFactTable(subjectID,PredicateID,facts) :
    retVal = True
    for item in facts :
        if (subjectID == item[0]) and (PredicateID == item[1]) :
            retVal = False
    return retVal

# ---------------------------------------------------------
''' Updates the fact table with new information/facts '''
def updateFactTable(questions,subjectID,facts) :
    # Create new facts based on questions
    # Insert them into the database if they are not
    #   there already
    for i in range(len(questions)) :
        newFact = list([subjectID,i,questions[i]])
        # Scan if fact is already in data base
        # Insert fact if it is not present
        if isNotInFactTable(subjectID,i,facts) :
            facts.append(newFact)
    
# ---------------------------------------------------------
''' Goes through the questions of the game and ends when
    the program guesses the plant or when it needs to
    learn a new one it does not know '''
def play(subjects, predicates, facts) :
    print('Please think of an plant!')
    print("I will try to figure out the plant that you're askng about.")

    # Create a list of numbers of potential canidates
    candidates = [i for i in range(0,len(subjects))]
    questions = [None for i in range(0,len(predicates))]

    # Three Exit Conditions
    # (1) Run out of Questions
    #       Guess at random
    #           If not hit get new plant name and store predicates
    # (2) One Plant Left
    #       Ask, If not hit get new plant name and store predicates
    # (3) No Plants Left
    #       Get new plant name, Store predicates

    nextQuestion = getFirstUnAsked(questions)

    while (len(candidates)>1) and (nextQuestion>=0) :
        # Ask the next question
        userReply = yesNoQuestion(
            'Is it true that your plant ' +
            predicates[nextQuestion] + '? ')
        questions[nextQuestion] = userReply

        # Eliminate subject not compatible

        for myFact in facts :
            # myFact[0] = subject index
            # myFact[1] = predicate
            # myFact[2] = Truth Values
            
            if myFact[1] == nextQuestion :
                if (userReply != myFact[2]) :
                    # Match on Subject, NOT on Truth
                    if myFact[0] in candidates :
                        candidates.remove(myFact[0])
                        print("Your plant isn't a",
                              subjects[myFact[0]])
        nextQuestion = getFirstUnAsked(questions)

    if (len(candidates)>0) :
        userReply = yesNoQuestion(
            'Is your plant a(n) ' +
            subjects[candidates[0]] + '?> ')
        if (userReply) :
            print('Thanks for playing!')
            newSubject = candidates[0]
            updateFactTable(questions,newSubject,facts)
        else :
            print("Hmm... I don't know a plant like this...")
            newName = input('What is the name of your plant? ')
            newName = newName.strip()
            newName = newName.capitalize()
            # Check if this subject is in the database
            # Add it to the database if it is not
            if (newName in subjects) :
                newSubject = subjects.index(newName)
            else :
                newSubject = len(subjects)
                subjects.append(newName)
            # Insert code to learn new question
            newPredicate = input("What is a fact" +
                                " that's is true for " +
                                newName + " but false for " +
                                subjects[candidates[0]] + "? ")
            newPredicate = newPredicate.strip()
            if (newPredicate not in predicates) :
                predicateIndex = len(predicates)
                predicates.append(newPredicate)
            else :
                predicateIndex = predicates.index(newPredicate)
            # Insert False predicate for candidates[0]
            if isNotInFactTable(candidates[0],predicateIndex,facts) :
                newFact = list([candidates[0],predicateIndex,False])
                facts.append(newFact)
            if isNotInFactTable(newSubject,predicateIndex,facts) :
                newFact = list([newSubject,predicateIndex,True])
                facts.append(newFact)
            # Do regular writeback for questions
            updateFactTable(questions,newSubject,facts)
            print('Thanks for playing!')
    else :
        # Learning a new subject (plant)
        print("Hmm... I don't know a plant like this...")
        newName = input('What is the name of your plant? ')
        newName = newName.strip()
        newName = newName.capitalize()
        newSubject = len(subjects)
        subjects.append(newName)
        updateFactTable(questions,newSubject,facts)
        print('Thanks for playing!')

# ---------------------------------------------------------
''' MAIN PROGRAM '''
if __name__ == '__main__' :
    
    subjects = list()
    predicates = list()
    facts = list()
    header = list() #Is the top row of the file with subjects, predicates, facts

    # Loads the Data from file
    loadData(subjects,predicates,facts,header)

    # Play Plants
    play(subjects,predicates,facts)

    # Saves the Data from file
    saveData(subjects,predicates,facts,header)

        





    
    

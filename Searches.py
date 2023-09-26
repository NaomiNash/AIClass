#!/usr/bin/python3
''' Searches.py - Naomi Nash - April 22, 2022 - Saint Leo '''

# -----------------------------------------------------------
def printMap(mapToDisplay) :
    ''' printMap - Prints the Node Topology '''
    keyList = list(mapToDisplay.keys())
    print('Report of Node Topology')
    print(F"{'Node':<10} {'Neighbors':<30}")
    print('-'*10,'-'*30)
    for myKey in keyList :
        print(F"{myKey:<10} {str(mapToDisplay[myKey]):<30}")
    print('-'*10,'-'*30)
    print()

# -----------------------------------------------------------
def visitDFS(mapToTraverse, location, visited=[], path=[]) :
    ''' Enacts a Depth First Search to the Node Topology '''
    if location not in visited :
        print('Visiting ', location, ' after ', str(path))
        visited.append(location)
        path.append(location)
        for neighbor in mapToTraverse[location] :
            visitDFS(mapToTraverse, neighbor, visited, path)
        if location in path :
            path.remove(location)

# -----------------------------------------------------------
def reportDFS(mapToTraverse, location) :
    ''' Prints the Depth First Search results '''
    print('Report of Depth First Search')
    visitDFS(mapToTraverse, location)
    print('End of Report')
    print()

# -----------------------------------------------------------
def visitBFS(mapToTraverse, location, visited=[],
                frontier=[], hereFrom=[]) :
    ''' Enacts a Breadth First Search to the Node Topology '''
    if location not in visited :
        if (len(hereFrom)>0) :
            prevLocation = hereFrom.pop(0)
        else :
            prevLocation = None
        print('Visiting ', location, ' from ', prevLocation)
        visited.append(location)
        for neighbor in mapToTraverse[location] :
            if neighbor not in visited :
                if neighbor not in frontier :
                    frontier.append(neighbor)
                    hereFrom.append(location)
        if len(frontier) > 0 :
            nextToVisit = frontier.pop(0)
            visitBFS(mapToTraverse, nextToVisit, visited,
                frontier, hereFrom)        

# -----------------------------------------------------------
def reportBFS(mapToTraverse, location) :
    ''' Prints the Breadth First Search results '''
    print('Report of Breadth First Search')
    visitBFS(mapToTraverse, location)
    print('End of Report')
    print()

# -----------------------------------------------------------
    ''' MAIN PROGRAM '''
if __name__ == '__main__' :
    myMap = dict({
            1 : [2,3,4],
            2 : [1,3,5,6],
            3 : [1,2,7],
            4 : [1,7],
            5 : [2],
            6 : [2,7],
            7 : [3,4,6,8],
            8 : [7]

        })
    printMap(myMap)
    reportDFS(myMap, 5)
    reportBFS(myMap, 5)
    

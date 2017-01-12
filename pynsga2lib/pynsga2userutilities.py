
#-------------------------------------------------------------------------------
# Name:        NSGA-II
# Purpose:     Calculates objective functions for NSGA-II
#
# Author:      Mehmet B. Ercan (mehmetbercan@gmail.com)
#
# Created:     10/29/2014
# Edited:      01/11/2017
# Copyright:   (c) Mehmet B. Ercan 2014
# Licence:     MIT
#-------------------------------------------------------------------------------


import os
from pynsga2utilities import rankcon


def CalculateObjectiveFunctions(population,parname, generation,ModelDir):
    """
    This function must be modified by user. Fitness values in population dictionary has to be updated here.
    Objective function values are considered to be best once they get closer to zero and worst when they are closer to +1 (or +infinity)
    """
    os.chdir(ModelDir)
    #/*Initializing the max rank to zero*/
    population["maxrank"]=0
    popsize = len(population["ind"])
    nfunc = len(population["ind"][0]["fitness"])
    nchrom = len(population["ind"][0]["xbin"])

    ParameterValues=[]
    for i in xrange(popsize):
        ParameterValues.append(population["ind"][i]["xbin"]) #/* problem variables */
        

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#This part should be edited by the user based on the specific model to be calibrated.
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

    #Population Loop: Paralization can be  applied here
    for i in xrange(popsize): 
        print "\n"*5,"-"*45,"\nGeneration: ", generation, "  Simulation: ", i+1, "\n", "-"*45
        
#        #Edit model input parameters using ParameterValues[i]
#        parvals=ParameterValues[i]
#        for j in xrange(nchrom): #parameter loop
#            UpdateModelParameterwith=parvals[j]
        
#        #Run model and read outputs
#        os.system(ModelDir+'/modelrun.cmd')
        
        
        #Calculate Objective functions
        objectivefuncs = []
        for k in xrange(nfunc):
            #Calculate Objective functions (ObjFunc) based on model result
            ObjFunc=0.2 #This should be calculated (bellow functions may be used here)

            
            
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#The user should stop editing after this line.
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            #Append objective functions
            objectivefuncs.append(ObjFunc)  
        #Add objective functions to population
        population["ind"][i]['fitness'] = objectivefuncs
    #/*---------------------------* RANKING *------------------------------*/
    rankcon(population);
    return;

    
    
    

#-------------------------------------------------------------------------------

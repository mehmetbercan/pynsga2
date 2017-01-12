from pynsga2lib import pynsga2, pynsga2utilities, pynsga2userutilities


#---- Input ----(space on directory may cause problems during execution)
ModelDirectory = r"C:\Projects\nsga2\pynsga2\ExampleModel\Model"
#---------------

NSGAII=pynsga2.nsga2(ModelDirectory) 
NSGAII.CreateInitialPopulation()

#Loop through generations
TotalNumGenerations = NSGAII.ngener
i=0
while i < TotalNumGenerations:
    NSGAII.CreateChildPopulation() #Thorough selection, crossover and mutation child population created from old population
    
    pynsga2utilities.decode(NSGAII.new_pop_ptr, NSGAII.vlen, NSGAII.lim_b); #Turn binary calibration parameters into normal numbers.
    #new_pop_ptr=child population. vlen=the no.of bits assigned to the each calibration parameters. lim_b=range of calibration parameters.
    

    pynsga2userutilities.CalculateObjectiveFunctions(NSGAII.new_pop_ptr,NSGAII.parname,i+1,NSGAII.Modeldir);

    
    NSGAII.CreateParentPopulation(i+1) # Old and New populations goes throuth Elitism, crowding distances, nondominated sorting
    #and create the old population for next generation. Report is printed during this function process.
    i+=1


print "The NSGA-II execution finished. Look at the results in NSGA2.OUT folder.";


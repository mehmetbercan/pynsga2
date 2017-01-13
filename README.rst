###################################################
NSGA-II as Python Library for Calibration of Models
###################################################
pynsga2 1.0

Released: 11-January-2017


************
Introduction
************
*  **Non-Dominated Sorting Genetic Algorithm II (NSGA-II)** is a multi-objective optimization algorithm used as an automatic calibration tool in wide range of disciplines.
*  pynsga2 is adapted from `nsga2 for SWAT models <https://github.com/mehmetbercan/NSGA-II_Python_for_SWAT_model>`_. Thus, pynsga2 is tested on a `Hydrologic Model <http://www.sciencedirect.com/science/article/pii/S1364815216302547>`_.
*  pynsga2 can be used with any model in any dicipline.

************
Setup
************  
 
**Install the Python module:**

*  Python setuptools are required for installation
*  Open a command prompt and ``cd`` to *"./pynsga2"*, then type ``Python setup.py install``
*  If the bullet above does not work, try ``pip install <./pynsga2>``
 
**Setup the Model:** 

*  Use *"ExampleModel"* folder structure 
*  Setup Model directory in *"pynsga2Example.py"* file in the *"ExampleModel"* folder
*  Setup NSGA-II parameters in *"pynsga2.def"* file in *"NSGA2.IN"* folder
*  Setup calibration parameters for your model in *"pynsga2_par.def"* file in *"NSGA2.IN"* folder
*  Edit **"pynsga2userutilities.py"** under *C:\\YourPythonDirectory\\Lib\\site-packages\\pynsga2lib* file to determine how to calculate objective functions

**Run the Model:** 

*  Once setup done, run *"pynsga2Example.py"* to start the calibration

****************
pynsga2 Outputs
****************

In this section, the output files will be explained to make users familiar with them. 
The output files are not in the example model but they will be created once *"pynsga2Example.py"* runs sucessfully.

*  Output.out:

  * This file contains all results starting from first generation to last generation (Last generation is the final result that included in next output file, *"plot.out"*).
  * This ouput is in same format with Prof. Deb's C code output. 
  * The first columns represent the calibration parameter values sperated with single space. The calibration paramers are in same order defined in *"pynsga2_par.def"* file. The next columns represent fitness values as much as defined in *"pynsga2.def"* file. Next two columns are related with NSGA-II methods. *"|**|"* sign seperates previous population results from current population results. After *"|**|"* sign, the order of columns are same as before the sign. 


*  Plot.out:

  * This file contains fitness results from the population of last generation (pareto front).
  * Each line, displaying objective function values, is a member of the pareto front. The order defined in *"pynsga2userutilities.py"* file is applied. 



*  g_rank_record.out: 

  * This file contains only results related with NSGA-II records and does not have any data related with model outputs.

  

************
Final Notes
************  

*  Read papers bellow to understand the process behing the scripts
*  Visit `my website <http://mehmetbercan.com/research/researchCal.html>`_ for more information
*  If you encounter any problems or have suggestions for the future development, please contact **Mehmet B. Ercan** at mehmetbercan@gmail.com.


**Important:**

*  **"pynsga2userutilities.py"** is the most important file to addapt pynsga2 into your model. It will be edited to calculate objective functions for the model.

**Credit:** 

Please cite one of the bellow articles if you use this code:

Ercan, M. B. and J. L. Goodall(2016), Design and implementation of a general software library for using NSGA-II with SWAT for multi-objective model calibration., *Environmental Modelling & Software*, 84, 112-120. doi:`10.1016/j.envsoft.2016.06.017 <http://www.sciencedirect.com/science/article/pii/S1364815216302547>`_.

Ercan, M. B. and J. L. Goodall (2014), A Python tool for multi-gage calibration of SWAT models using the NSGA-II algorithm., In: Ames, D.P., Quinn, N.W.T., Rizzoli, A.E. (Eds.), 2014. *Proceedings of the 7th International Congress on Environmental Modelling and Software, June 15-19, San Diego, California, USA*. (4):2325-2331, 2014. doi:`10.13140/2.1.3865.4407 <http://www.iemss.org/sites/iemss2014/papers/iemss2014_submission_212.pdf>`_. 



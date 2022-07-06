# About Hospital_Virus_Spread

### Instructions:
1. compiled with Python 3.7.4
2. check and pip install required packages in requirements.txt
3. Run main.py and enter the required inputs.
4. Output is the minimum time taken for the virus to spread. 

### main.py
#### contains the main function that gives the minimum time taken for the virus to spread entirely in the hospital wards.

### traverse.py
#### contains the functions for the virus to traverse to different locations such as top, bottom, left and right of the current ward.

### model_virus.py
#### contains the functions that:
#### 1. model the interaction amongst infected wards, uninfected wards and empty wards.
#### 2. Model the virus spread and store the infection state of each ward per time unit.


### Logic of the code.
#### 1. The code tracks the total minimum units of time required for the entire ward to be uninfected.
#### 2.After an iteration of virus spread under single time unit is finished, the old state of the hospital ward is updated with the newest state.
#### 3. The above process repeats until all the wards are infected (returns minimum time taken) or all possible ways of virus spread are exhausted in the hospital ward yet uninfected wards remain (returns -1)

# longcompound.py
# Raunak Anand
# ECS 36A Winter 2019
# Calculation of atomic weight of chemical compounds entered by user
# along with names of elements


def makedictionary():
    global chem_names
    global dict_compound
    file = open("atomic_weights.txt","r") # open file 
    dict_compound = {} # dictionary 
    chem_names = {} # dictionary for element names
    for line in file:
        line = line.strip() # remove whitespace 
        code = line.split("\t") # split line at tab
        atomic_weight = code[0] # first column is atomic weight
        element= code[1] # second column is atomic weight 
        names = code[2] # third column is element names
        weight = float(atomic_weight) # atomic weights are converted to floats 
        dict_compound[element] = weight
        chem_names[element] = names
def chemistry(x):  # function to calculate atomic weight 
    global element_list
    compounds = makedictionary()
    i = -1
    wt = 0 
    lst = x # temporary list
    element_list = [] # list of element names
    done = True
    while i <= len(lst) + 1 :
        i = i + 1
        try:
            if lst[i] < "a" and lst[i] >= "A" and done: # checking if elements are capitalized 
                if lst[i+1] >= "a" and done: # checking if element if of two letters such as 'Sn'
                    if lst[i+2] < "A" and done: # checking if there is a number after the element
                                               # number of molecules 
                        wt += (dict_compound[lst[i:i+2]] * float(lst[i+2])) # obtaining final atomic weight
                        element_list.append(chem_names[lst[i:i+2]])
                    elif lst[i+2] < "a" and lst[i+2] >= "A" and done:
                        wt += dict_compound[lst[i:i+2]] # obtaining final atomic weight 
                        element_list.append(chem_names[lst[i:i+2]]) 
                elif lst[i+1] < "A" and done:
                    wt += dict_compound[lst[i]] * float(lst[i+1]) # obtaining final atomic weight 
                    element_list.append(chem_names[lst[i]])
                elif lst[i+1] < "a" and lst[i+1] >= "A" and done:
                    wt += dict_compound[lst[i]] # obtaining final atomic weight 
                    element_list.append(chem_names[lst[i]]) # adding element names to the list
        except IndexError: # to prevent 'i' from going out of range 
            done = False
            continue
    if lst[len(lst)-1] < "a" and lst[len(lst)-1] >= "A": # checking if elements are capitalized 
        wt += dict_compound[lst[len(lst)-1]] # obtaining final atomic weight  
        element_list.append(chem_names[lst[len(lst)-1]])
    elif  lst[len(lst)-1] >= "a" and lst[len(lst)-2] < "a" and lst[len(lst)-2] >= "A":# to check if next character is
            # different element, number, same element (for eg. Sn)
        
        wt += dict_compound[lst[len(lst)-2:len(lst)]] # obtaining final atomic weight
        element_list.append(chem_names[lst[len(lst)-2:len(lst)]])
    return wt
def main():
    while True:
        try:
            chem = input("Chemical Composition? ")
            print("The atomic weight of",chem,"is",chemistry(chem))
            b = list(dict.fromkeys(element_list))
            i = 0 
            c = 'The elements are ' + b[i]
            while i + 1 < len(b):
                i = i + 1
                if i + 1 < len(b):
                    c += ' , ' + b[i]
                else:
                    c += ' and '+str(b[len(b)-1]) 
            print(c)
        except EOFError: # program keeps running until user presses ctrl + D
            break
main()

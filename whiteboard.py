# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function


# input is a string, either T or F

# output should be a string, either Outage or Power

# constraints: if F >= 2, return Outage, anything below return Power.

# What about T?

ex_list = [ 'T', 'F', 'F', 'F' ]	

count_f = []

def power_outage(l_street):
    for light in l_street:
        if light == 'F':
            count_f.append(light)
        else:
            continue
    if count_f.count('F') >= 2:
        return "Outage"
    else:
        return "Power"
        
print(power_outage(ex_list))

light_list = [ 'T', 'F', 'F', 'F' ]

# dylan method
def determine_outage(light_list):
    return 'Outage' if light_list.count('F') >= 2 else 'Power'

def determine_outage_with_list_comp(light_list):
    return 'Outage' if len([True for light in light_list if light == 'F']) >= 2 else "Power"

def determine_outage_with_filter(light_list):
    return 'Outage' if len(list(filter(lambda light: light == 'F', light_list))) >= 2 else 'Power'
import json
import graphviz

# parse json file
def parse(j_file):
    fp = open(j_file) # opens json file into fp
    data = json.load(fp) # returns json file as dicttionary
    return data, fp

# required
def digraph(j_file):
    
    dot = graphviz.Digraph(comment='CSCI 2024 Template')
    
    # data[0]= comm-intensive requirements
    # data[1]= math core 
    # data[2]= humanities arts and social sciences
    # data[3]= depth requirement 
    # data[4]= cs major requirements (9)
    data_csci,fp = parse(j_file[0]) # parse csci bs data
    
    # major required
    # math/science core
    # hass elective --> chinese pathway
    # csci classes --> need course code
    
    # colors --> different for each concentration 
    # even out levels
    
    print(dot.source)
    
    dot.render(directory='doctest-output').replace('\\','/')
    dot.render(directory='doctest-output', view=True) 
    
    fp.close()


# required
def bipartite():
    # professors --> only cs
    # classes
    # start with 2023 fall - 2024 spring
    
    return 

# not required --> implement if time
def extra_credit():
    return
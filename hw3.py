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
    data_pre, fp1 = parse(j_file[1]) # parse prereq data
    
    # add nodes and edges
    node_num = [] # holds course number
    node_name = [] # holds course name
    edges = [] # holds all prereq data
    
    # add CS1
    dot.node('CSCI 1100','CSCI 1100 || Computer Science I')
    node_num.append('CSCI 1100')
    node_name.append('CSCI 1100 || Computer Science I')
    
    # major required
    for i in range(7):
        course = data_csci[4]['rules'][0]['rule_data']['rules'][i]['rule_data']['courses'][0]['dept'] + ' ' + data_csci[4]['rules'][0]['rule_data']['rules'][i]['rule_data']['courses'][0]['crse']
        dot.node(course,course + " || " + course,data_csci[4]['rules'][0]['rule_data']['rules'][i]['label'])
        node_num.append(course)
        node_name.append(course + " || " +data_csci[4]['rules'][0]['rule_data']['rules'][i]['label'])
    
    
    # math/science core
    # intro to bio/intro to bio lab
    dot.node('BIOL 1010','BIOL 1010 || Intro to Biology')
    node_num.append('BIOL 1010')
    node_name.append('BIOL 1010 || Intro to Biology')
    
    dot.node('BIOL 1015','BIOL 1015 || Intro to Biology Laboratory')
    node_num.append('BIOL 1015')
    node_name.append('BIOL 1015 || Intro to Biology Laboratory')
    
    edges.append(('BIOL 1015','BIOL 1010'))
    dot.edge('BIOL 1010','BIOL 1015')
    
    # physics 1
    dot.node('PHYS 1100','PHYS 1100 || Physics I')
    node_num.append('PHYS 1100')
    node_name.append('PHYS 1100 || Physics I')
    
    # science elective
    dot.node('SCIOP', 'SCIOP || Science Option')
    node_num.append('SCIOP')
    node_name.append('SCIOP || Science Option')
    
    # calc 1
    dot.node('MATH 1010','MATH 1010 || Calculus I')
    node_num.append('MATH 1010')
    node_name.append('MATH 1010 || Calculus I')
    
    # calc 2
    dot.node('MATH 1020','MATH 1020 || Calculus I')
    node_num.append('MATH 1020')
    node_name.append('MATH 1020 || Calculus I')
    
    # math elective 1
    dot.node('MATH 1', 'MATH 1 || Mathematics Options I')
    node_num.append('MATH 1')
    node_name.append('MATH 1 || Mathematics Options I')
    
    # math elective 2

    
    # hass elective --> chinese pathway
    # manually add all of chinese :)
    
    # csci classes --> need course code
    
    # colors --> different for each concentration 
    # even out levels
    
    # label: Code Name
    
    print(dot.source)
    
    dot.render(directory='doctest-output').replace('\\','/')
    dot.render(directory='doctest-output', view=True) 
    
    fp.close()


# required
def bipartite():
    # professors --> only cs
    # classes
    # start with 2023 fall - 2024 spring
    # colors: teachers == blue, classes == red
    
    return 

# not required --> implement if time
def extra_credit():
    return
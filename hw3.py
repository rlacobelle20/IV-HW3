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
    req_data = dict() # holds requirement data
    
    req_data['major_req'] = [] #contains a list of major required elemets
    
    # add CS1
    dot.node('CSCI 1100','Computer Science I')
    node_num.append('CSCI 1100')
    node_name.append('Computer Science I')
    req_data['major_req'].append('CSCI 1100')
    
    # major required
    
    for i in range(7):
        course = data_csci[4]['rules'][0]['rule_data']['rules'][i]['rule_data']['courses'][0]['dept'] + ' ' + data_csci[4]['rules'][0]['rule_data']['rules'][i]['rule_data']['courses'][0]['crse']
        dot.node(course,data_csci[4]['rules'][0]['rule_data']['rules'][i]['label'])
        node_num.append(course)
        node_name.append(data_csci[4]['rules'][0]['rule_data']['rules'][i]['label'])
        req_data['major_req'].append(course)

    # math/science core
    req_data['math_sci'] = []
    
    # intro to bio/intro to bio lab
    dot.node('BIOL 1010','Intro to Biology')
    node_num.append('BIOL 1010')
    node_name.append('Intro to Biology')
    req_data['math_sci'].append('BIOL 1010')
    
    dot.node('BIOL 1015','Intro to Biology Laboratory')
    node_num.append('BIOL 1015')
    node_name.append('Intro to Biology Laboratory')
    req_data['math_sci'].append('BIOL 1015')
    
    edges.append(('BIOL 1015','BIOL 1010'))
    dot.edge('BIOL 1010','BIOL 1015')
    
    # physics 1
    dot.node('PHYS 1100','Physics I')
    node_num.append('PHYS 1100')
    node_name.append('Physics I')
    req_data['math_sci'].append('PHYS 1100')
    
    # science elective
    dot.node('SCIOP', 'Science Option')
    node_num.append('SCIOP')
    node_name.append('Science Option')
    req_data['math_sci'].append('SCIOP')
    
    # calc 1
    dot.node('MATH 1010','Calculus I')
    node_num.append('MATH 1010')
    node_name.append('Calculus I')
    req_data['math_sci'].append('MATH 1010')
    
    # calc 2
    dot.node('MATH 1020','Calculus II')
    node_num.append('MATH 1020')
    node_name.append('Calculus II')
    req_data['math_sci'].append('MATH 1020')
    
    # math elective 1
    dot.node('MATH 1', 'Mathematics Options I')
    node_num.append('MATH 1')
    node_name.append('Mathematics Options I')
    req_data['major_req'].append('MATH 1')
    
    # math elective 2
    dot.node('MATH 2', 'Mathematics Options II')
    node_num.append('MATH 2')
    node_name.append('Mathematics Options II')
    req_data['major_req'].append('MATH 2')
    
    # hass elective --> full chinese pathway
    req_data['chinese'] = []
    
    # chinese 1
    dot.node('LANG 1410', 'CHINESE I')
    node_num.append('LANG 1410')
    node_name.append('CHINESE I')
    req_data['chinese'].append('LANG 1410')
    
    # chinese 2
    dot.node('LANG 2410', 'CHINESE II')
    node_num.append('LANG 2410')
    node_name.append('CHINESE II')
    req_data['chinese'].append('LANG 2410')
    
    # chinese 3
    dot.node('LANG 2420', 'CHINESE III')
    node_num.append('LANG 2420')
    node_name.append('CHINESE III')
    req_data['chinese'].append('LANG 2420')
    
    # chinese 4
    dot.node('LANG 4430', 'CHINESE IV')
    node_num.append('LANG 4430')
    node_name.append('CHINESE IV')
    req_data['chinese'].append('LANG 4430')
    
    # chinese 5
    dot.node('LANG 4470', 'CHINESE V')
    node_num.append('LANG 4470')
    node_name.append('CHINESE V')
    req_data['chinese'].append('LANG 4470')
    
    # chinese lang & culture in film
    dot.node('LANG 4961', 'Chinese Lang & Culture In Film')
    node_num.append('LANG 4961')
    node_name.append('Chinese Lang & Culture In Film')
    req_data['chinese'].append('LANG 4961')
    
    edges.append(('LANG 2420','LANG 4961'))
    dot.edge('LANG 2420','LANG 4961')
    
    # chinese calligraphy
    dot.node('LANG 4960', 'Chinese Calligraphy')
    node_num.append('LANG 4960')
    node_name.append('Chinese Calligraphy')
    req_data['chinese'].append('LANG 4960')
    
    edges.append(('LANG 2420','LANG 4960'))
    dot.edge('LANG 2420','LANG 4960')
    
    # csci classes --> need course code
    # don't do grad classes, no repeats
    # [key for key, value in keyValue.items() if value > 60]
    csci_pre = [k for k in data_pre.keys() if "CSCI" in k]
    
    req_data['csci'] = [] # holds all csci courses with prereqs
    prereqs = [] # prereqs --> check if course exists before adding edge
    for i in csci_pre:
        # do not use grad classes
        if i[5] != "6":
            prereqs = data_pre[i]['prereqs']
            
            if len(prereqs) > 0:
                # dont add if node already exists
                if i not in node_num:
                    node_num.append(i)
                    node_name.append(data_pre[i]['title'])

    # even out levels
    
    for num in node_num:
        if len(num) >= 9:
            prereqs = data_pre[num]['prereqs']
            # only adds node if prereq exists
            if len(prereqs) > 0:
                for i in prereqs:
                    if i in node_num and (i,num) not in edges:
                        dot.node(num,data_pre[num]['title'])
                        dot.edge(i,num)
                        edges.append((i,num))
        
    # label: Code Name
    
    #print(dot.source)
    # colors nodes
    for i in req_data['major_req']:
        dot.node(i, color= 'cornflowerblue', style='filled')
    for i in req_data['math_sci']:
        dot.node(i, color= 'green', style='filled')
    for i in req_data['chinese']:
        dot.node(i, color= 'orange', style='filled')
    
    dot.render(directory='doctest-output').replace('\\','/')
    dot.render(directory='doctest-output', view=True) 
    
    fp.close()
    fp1.close()


# required
def bipartite(j_file):
    # professors --> only cs
    # classes
    # start with 2023 fall - 2024 spring
    # colors: teachers == blue, classes == red

    data_202309, fp = parse(j_file[0])
    data_202401, fp1 = parse(j_file[1])

    #dictionary with course as key and professor as value
    # [course id \n course name] = [list of professors]
    course_dict = dict()
    for c in data_202309[14]['courses']:
      if c['id'][6]!='9' and c['id'][5]!='6':
        instructors = set()
        for i in range(0,len(c['sections'])):
          for timeslot in c['sections'][i]['timeslots']:
            split_list = (timeslot.get('instructor').split(', '))
            for prof in split_list:
              if(prof!="TBA" and prof!='Shianne M. Hulbert'):
                instructors.add(prof)
        course_dict[c['id'] + '\n' + c['title']]=instructors

    for c in data_202401[14]['courses']:
      if c['id'][6]!='9' and c['id'][5]!='6':
        instructors = set()
        for i in range(0,len(c['sections'])):
          for timeslot in c['sections'][i]['timeslots']:
            split_list = (timeslot.get('instructor').split(', '))
            for prof in split_list:
              if(prof!="TBA" and prof!='Shianne M. Hulbert'):
                if c['id'] + '\n' + c['title'] not in course_dict.keys():
                  instructors.add(prof)
                else:
                  course_dict[c['id'] + '\n' + c['title']].add(prof)
            if c['id'] + '\n' + c['title'] not in course_dict.keys():
                course_dict[c['id'] + '\n' + c['title']]=instructors
                
        
        #course_dict[c['id'] + '\n' + c['title']].add(instructors)

    print(course_dict)

    dot = graphviz.Graph(engine='circo', graph_attr={'scale': '0.5'})
    #dot.attr(layout='neato')
    for x in course_dict:
      dot.node(x, color= 'cornflowerblue', style='filled')
      for prof in course_dict[x]:
        dot.node(prof, color='pink', style='filled')
        dot.edge(x, prof)

    d=dot.unflatten(stagger=20)
    d.view()

    dot.render(directory='doctest-output').replace('\\','/')
    dot.render(directory='doctest-output', view=True)
    fp.close()
    fp1.close()


    return

# not required --> implement if time
def extra_credit():
    return

digraph(['2024-BS-CSCI.json','prereq_graph.json'])
bipartite(['courses.json', 'courses24.json'])

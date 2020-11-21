"""COMP1730/6730 assignment template.

Semester 1, 2019.

Co-authors: u6826541, u6833622, u6832190
"""

from visualise import *
import math


# Load data - do not change this function
def load_heightmap(path):
    """Loads a heightmap dataset.

    Parameters
    ----------
    path : str
        Path to the heightmap data.

    Returns
    -------
    List of lists
        A list of lists containing the heightmap. Each list is
        a row of the map.
        (0, 0) is the top left corner of the heightmap.
    """
    import numpy as np
    return [list(row) for row in np.loadtxt(path)]


# Question 1.
def cells_above_height(heightmap, height):
    '''This function takes a map and a height as input , and will return the cell
    s that is taller than the height'''
    n_cells = 0
    for row in heightmap:
        for cell in row:
            if cell > height:
                n_cells += 1
    #traverse the list and find the proper cell
    return n_cells

def area_above_water(heightmap, water_level):
    '''This function takes a map and water level as inputs, which will return the
    total areas that is higher than water level and will Change unit'''
    return (cells_above_height(heightmap, water_level) * 10 ** (-6))

# Question 2.
def highest_point(heightmap):
    ''' This function takes a heightmap and returns the highest point as a tuple of (x, y)
    coordinates'''
    max_point=(0,0)
    max_num = heightmap[0][0]
    #they are all the default setting,and start at (0,0)
    
    for y in range (len(heightmap)):
        for x in range (len(heightmap[y])):
            if max_num < heightmap[y][x]:
                max_point = (x,y)
                max_num = heightmap [y][x]
                #to check whether it is the highest point, if so max point will
                #become to the new max point
    return max_point

# Question 3.
def findhor_ver(heightmap,x,y):
    '''This function takes two inputs to caculate horizontal and vertical gradient
        according to the cell's position.
        (Edge-cases)With the assumption that if the cell needed is unexisted, we could use the ratio of the existed and the aimed element 
        to produce the gradient needed'''
    if x == 0: # if the cell is on the boundary, we do produce the undefined cell according to the ratio of the nearest existed one and the aimed one
        if y == 0:
            # left up case
            hor = 2*(heightmap[y][x+1]-heightmap[y][x])
            ver = 2*(heightmap[y+1][x]-heightmap[y][x])
        elif y == len(heightmap)-1:
            # left down case
            hor = 2*(heightmap[y][x+1]-heightmap[y][x])
            ver = 2*(heightmap[y][x]-heightmap[y-1][x])
        else:
            # left line case (corner excepted)
            hor = 2*(heightmap[y][x+1]-heightmap[y][x])
            ver = (heightmap[y+1][x]-heightmap[y-1][x])
            # rightmost line case
    elif x == (len(heightmap[0])-1):
        if y == 0:
            hor = 2*(heightmap[y][x]-heightmap[y][x-1])
            ver = 2*(heightmap[y+1][x]-heightmap[y][x])
        elif y == len(heightmap)-1: 
            hor = 2*(heightmap[y][x]-heightmap[y][x-1])
            ver = 2*(heightmap[y][x]-heightmap[y-1][x])
        else:
            hor = 2*(heightmap[y][x]-heightmap[y][x-1])
            ver = 2*(heightmap[y+1][x]-heightmap[y-1][x])
    elif y == 0:
        hor = (heightmap[y][x+1] - heightmap[y][x-1])
        ver = 2*(heightmap[y+1][x] - heightmap[y][x])
    elif y == len(heightmap)-1:
        hor = (heightmap[y][x+1] - heightmap[y][x-1])
        ver = 2*(heightmap[y][x] - heightmap[y-1][x])
        # normal situation use the calculation method provided
    else:   
        hor = (heightmap[y][x+1] - heightmap[y][x-1])    
        ver = (heightmap[y+1][x] - heightmap[y-1][x])
        
    return (hor,ver)   
        
def slope(heightmap, x, y):
    '''This function takes a heightmap and(x,y) and will return the slope of a position (x,y)
    (Edge-cases)With the assumption that if the cell needed is unexisted, we could use the ratio of the existed and the aimed element 
    to produce the gradient needed'''
    (hor,ver)=findhor_ver(heightmap,x,y)
    return (ver**2+hor**2)**(1/2)


def aspect(heightmap, x, y):
    '''This function takes a heightmap and(x,y) and will return the aspect of a position (x,y)
    (Edge-cases)With the assumption that if the cell needed is unexisted, we could use the ratio of the existed and the aimed element 
    to produce the gradient needed'''
    (hor,ver)=findhor_ver(heightmap,x,y)
    return math.atan2(ver,hor)


# Question 4.         

def find_adjacent(x ,y ,heightmap):
    '''which takes a coordinate and a heightmap and will return the cells which is
    adjacent(8 cells) to the coordinate and will return in a list and it will return the height of (x,y).'''
    index = [] 
    if y - 1 < 0:
        if x - 1 < 0:
        # which means the (x,y) is in top left of the map
            index = [(x+1,y),(x,y+1),(x+1,y+1)]
        elif x == len(heightmap[y]) - 1:
        # in the top right of the map
            index = [(x-1,y),(x-1,y+1),(x,y+1)]
        else:
        #(x,y) on the first row            
            index = [(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    elif x - 1 < 0:
        if y == len(heightmap) - 1:
        # on the bottom left of the map           
            index = [(x,y-1),(x+1,y-1),(x+1,y)]
        else:
        # on the first column of the map            
            index = [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1)]
    elif y == len(heightmap) - 1:
        if x == len(heightmap[0]) - 1:
        # on the bottom right of the map
            index = [(x-1,y-1),(x,y-1),(x-1,y)]
        else:
        # on the last row of the map            
            index = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y)]
    elif x == len(heightmap[0]) - 1:
        # on the last column of the map        
        index = [(x-1,y-1),(x,y-1),(x-1,y),(x-1,y+1),(x,y+1)]
    else:
        # the normal case,which is not in the edges        
        index = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    return (index,heightmap[y][x])

def find_mini(heightmap,coordinate_and_point):
    '''This function takes a map and a sequence of the coordinates of all adjacent
    points and and the central value.
       This function will return a tuple,which means it has just one minimum so just return the minimum value and its
    coordinate ,else it means that it will have more than one minimum so it will 
    return all the coordinates of the minimum value in a list'''
    coordinate_list = coordinate_and_point[0]
    height = [] #This is a list of all the adjacent height
    for index in coordinate_list:   # This will add all the value into the list
        (x,y) = index
        height.append(heightmap[y][x])      
    minimum = min(height) 
    min_index = height.index(minimum) #index of minimum
    if minimum >= coordinate_and_point[1]: #whether the minimum will bigger than central value or not
        return (minimum, coordinate_list[min_index])
    else:
        if height.count(minimum) > 1: #whether it will have more than one minimum            
            min_indexs = []
            for i in range(len(height)):    #if so add all the coordinates to the list
                if height[i] == minimum:
                    min_indexs.append(coordinate_list[i])
            return (minimum,min_indexs)
        else:   #This means that just has one minimum
            return (minimum, coordinate_list[min_index])

def find_path(heightmap, x, y, water_level=557):
    '''This function takes a map and the original position,water level,as well and will find
    the optimum path as a list of coordinates to win, which means that if you reach the lowest height position but not lower than
    water level,so you will win
       Besides,if you reach the water level you will stop and when you encounter the minimum which is lower
    than the water level, it will stop and not returning that point because it is under water'''
    path = [(x,y)]
    while True:    
       (min_value,next_point) = find_mini(heightmap,find_adjacent(x,y,heightmap))    #initialse the minimum and the minimum coordinate
       if isinstance(next_point,list):
       #If it is a list ,then it means that it has more than one minimum     
           tem_paths =[]    #Paths that each the minimums will lead to
           height1 = []     #Heights of the each path destination height 
           for point in next_point: 
               (x_n,y_n) = point
               part_path = find_path(heightmap,x_n,y_n,water_level) #create a partial path for each minimum
               tem_paths.append(part_path)              
               (x_1,y_1) = part_path[-1] 
               height1.append(heightmap[y_1][x_1])  #append each height of last position to the list
           index = height1.index(min(height1))  #get the index of best path
           path.extend(tem_paths[index])    #merge all the paths
           return path                     
       else:
       #which means that it just has one minimum
           if min_value >= heightmap[y][x]:
           #wherther the minimum is bigger than central value or not
               return path 
           elif water_level >= min_value :
           #whether it reaches the water level or not
               if min_value == water_level:
                   path.append(next_point)
               return path       
           else:
               path.append(next_point)
           #just a normal case, append the point to path and keep going from this point
       (x,y) = next_point
   


# Question 5.
def find_buildings(buildings_heightmap):
    '''This function takes a buildings heightmap and will return the coordinates of
    all the buildings in the map(if two cell are next tp each other, 
    then they are part of the same building)'''
    coordinates = []
    script = buildings_heightmap[:]
    deep_copy_heightmap = []
    for row in script:
        copy_row = row[:]
        deep_copy_heightmap.append(copy_row)        
    # first copy the heightmap to do some operations on it without changing any thing in oringnal one
    for y in range(len(deep_copy_heightmap)):
        for x in range(len(deep_copy_heightmap[y])): 
    #To check every points in map wherther they are building or not
            if deep_copy_heightmap[y][x] != 0:
                coordinates.append(judge_building(x,y,deep_copy_heightmap))             
            #If it is a building, it will continue to find wherther it has some more points or not               
        y += 1
    return coordinates 

def judge_building(x ,y , buildings_heightmap):
    '''This function takes the (x,y) coordinate and will check whether there are some
    points which is adjacent to the(x,y). If so it will keep looking based on the adjacent points
    until there are no more points adjacent to the whole points'''
    points = [(x,y)]    #This is the start point
    adjacent = near_four(x,y,buildings_heightmap)   #Use this function to find adjacent 4 points
    for (new_x,new_y) in adjacent:
    # check all the point in the adjacent points wherther it has more members or not    
        if buildings_heightmap[new_y][new_x] != 0 :
            buildings_heightmap[y][x] = 0   #It is a building, so it will be erased for not causing infinite loop 
            points.extend(judge_building(new_x,new_y,buildings_heightmap))  #And it will start at the erased point to keep looking points,
            buildings_heightmap[new_y][new_x] = 0                           #and extend it together with the total points
            #After finishing seaching, the adjacent cell will be erased to 0 for not causing infinite loop.
    return set(points)


def near_four(x ,y ,buildings_heightmap):
    '''This function takes a coordinate and a heightmap,which will find all the points
    that is adjacent to (x,y) according to "crossed grid" '''
    near = []
    if y - 1 < 0:   
        if x - 1 < 0:   #which means the (x,y) is in top left of the map  
            near = [(x+1,y),(x,y+1)]
        elif x == len(buildings_heightmap[y])-1:    #on the top right of the map
            near = [(x-1,y),(x,y+1)]
        else:  #(x,y) on the first row 
            near = [(x-1,y),(x,y+1),(x+1,y)]
    elif x - 1 < 0:     
        if y == len(buildings_heightmap)-1: # on the bottom left of the map
            near = [(x,y-1),(x+1,y)]
        else:   # on the first column of the map
            near = [(x,y-1),(x+1,y),(x,y+1)]
    elif y == len(buildings_heightmap)-1:
        if x == len(buildings_heightmap[y])-1:  # on the bottom right of the map
            near = [(x,y-1),(x-1,y)]
        else:   # on the last row of the map
            near = [(x-1,y),(x,y-1),(x+1,y)]
    elif x == len(buildings_heightmap[y])-1:    # on the last column of the map
        near =[(x,y-1),(x-1,y),(x,y+1)] 
    else:   # the normal case,which is not in the edges
        near = [(x,y-1),(x-1,y),(x,y+1),(x+1,y)]
    return near              
    
# Question 6.
def create_map(ground_heightmap, building_heightmap):
    '''This function takes two maps and add each corresponding cell of two maps
    together to get a new map'''
    actual_map = []
    index = 0
    for row_g in ground_heightmap:
        new_row = list(map(lambda x, y: x + y, row_g ,building_heightmap[index]))
        #Every row is a list so add each height together
        actual_map.append(new_row)
        index += 1
    return actual_map   

def judge_position(x1,y1,x2,y2,actual_map):
    '''This funcion takes two positions as (x1,y1,x2,y2) and will return two points which is the points that will generate a diagonal
    after so many steps.So apply this this function over and over again it will return the points
    of the diagonal between two position(with some approximation)'''
    if (x1,y1) in find_adjacent(x2,y2,actual_map)[0]:
        return ()
    #If two positions are next to each other,then it will no height between them
    if x1 - x2 == 0 or abs(x1 - x2) == 1:  #To check wherther it is a vertical line or the situaton of (2xn)
        if y1 > y2:
            return (x1,y1-1,x2,y2+1)
        elif y1 < y2:
            return (x1,y1+1,x2,y2-1)  
        else:   # Which means that y1=y2,so two positions are overlapped
            return ()
    elif y1 - y2 == 0 or abs(y1 - y2) == 1: #To check wherther it is a horizontal linen or the situaton of (2xn)
        if x1 > x2:
            return (x1-1,y1,x2+1,y2)
        else:
            return (x1+1,y1,x2-1,y2)                            
    elif (y1 - y2)/(x1 - x2) < 0:   #The two positions line slope is negative
        if y1 > y2:
            return (x1+1,y1-1,x2-1,y2+1)
        else:
            return (x1-1,y1+1,x2+1,y2-1) 
    else:     #The two positions line slope is positive
        if y1 > y2:
            return (x1-1,y1-1,x2+1,y2+1)
        else:
            return (x1+1,y1+1,x2-1,y2-1)
                      
def line_of_sight(ground_heightmap, building_heightmap, x1, y1, x2, y2):
    '''This function takes two maps and two positions and will return all the coordinates
    between two positions based on some approximation'''
    actual_map = create_map(ground_heightmap , building_heightmap) # first, add building heights and ground heights to create actual map
    height_sight1 = []  #This height list value will start at x1 to x2
    height_sight2 = []  #This height list value will start at x2 to x1
    if judge_position(x1,y1,x2,y2,actual_map) == ():    #If it is a (),which mean too close or they are overlapped,then will return [].
        return height_sight1
    else:
        (x1_new,y1_new,x2_new,y2_new) = judge_position(x1,y1,x2,y2,actual_map) #Initialise the coordinates, and move forward to create a diagonal
    while True:
        if (x1_new , y1_new) == (x2_new , y2_new):  #When you try to move forward,but you find that they are the same point such as (3x3)
            height_sight1.append(actual_map[y1_new][x1_new])
            #So add just one of it and break
            break
        if abs(x1_new - x2_new) == 1 and abs(y1_new - y2_new) == 1: #When you come across a situation like 2x2, if move forward will swap two points
            height_sight1.append(actual_map[y1_new][x1_new])
            height_sight2.append(actual_map[y2_new][x2_new])
            #So stop and append two points to proper list
            break
        if (x1_new,y1_new) in near_four(x2_new,y2_new,actual_map): #When moving forward to this situation that is two points are adjacent
            height_sight1.append(actual_map[y1_new][x1_new])
            height_sight2.append(actual_map[y2_new][x2_new])
            #So stop and append two points to proper list
            break
        height_sight1.append(actual_map[y1_new][x1_new])
        height_sight2.append(actual_map[y2_new][x2_new])
        (x1_new,y1_new,x2_new,y2_new) = judge_position(x1_new,y1_new,x2_new,y2_new,actual_map) 
        # If it is not come across situation above,then just keep going and append it to list
    return height_sight1+height_sight2[::-1]
        

def is_hiaf_visible(ground_heightmap, building_heightmap, x, y, hiaf_x=423, hiaf_y=337):
    '''This function takes two maps and two positions to check whether you standing at first position
    will see the second position or not,if so return true,else false.
       This function assumes that the second point is the highest point,which is higher than first point'''
    actual_map = create_map(ground_heightmap,building_heightmap)    #first create the actual map by two maps
    list_of_height = line_of_sight(ground_heightmap,building_heightmap,x,y,hiaf_x,hiaf_y)   #find all the heights between two positions
    
    self_height = actual_map[y][x] #This is the height of the first coordinate
    height_hiaf = actual_map[hiaf_y][hiaf_x] - self_height#This value is the second height minus first height,which will be use to similar triangle
    
    interval_diagonal = 1  #each interval value on the diagonal
    total_diagonal = len(list_of_height) + 1   #The length of the diagonal      
    if list_of_height == []:
    #It is empty mean they are too close,so it must can be visible
        return True
    for height in list_of_height:
        if ((height - self_height)/(height_hiaf)) > (interval_diagonal/total_diagonal):
        # If this is true means that one height of the diagonal is too high and it is not visible
            return False        
        interval_diagonal += 1  #calculate the next proper interval which will be used to compute the similar triangle       
    return True # None of the height will cause invisible.
        
       

if __name__ == "__main__":
    # If you want to run any of the functions in this assignment, do so from here.

    # For example, if you uncomment the following lines they will load and visualise a heightmap
    # that should look similar to the one in the assignment specification.
     
     heightmap = load_heightmap("height_rspe.txt")
     buildings = load_heightmap("buildings_rspe.txt")
#     find_buildings(buildings)
#     visualise_path(heightmap, find_path, 60, 40, full_map=False) 
#     visualise_path(heightmap, find_path, 60, 40, full_map=True) 
     
#     visualise_line_of_sight(heightmap, buildings, 0, 200, 337, 423, line_of_sight)
     combined_heightmap = [[heightmap[y][x] + buildings[y][x] for x in range(len(buildings[0]))] for y in range(len(buildings))]
#     visualise_heightmap(combined_heightmap)
     pass

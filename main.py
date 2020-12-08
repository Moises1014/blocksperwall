

walls = input('Please enter a how many walls there are: ')
blocks_for_walls = []

def Solid_wall():
  #length of wall
  length_solid_wall = input('\nEnter the legnth of the Wall(in feet,ft): ')
  #width of wall
  height_solid_wall = input('\nEnter the height of the Wall(in feet,ft): ')
  #area of wall
  wall_area = int(length_solid_wall)*int(height_solid_wall)
  #length of block
  length_block = input('\nEnter the legnth of the blocks(in inches, in): ')
  #width of block
  height_block = input('\nEnter the height of the blocks(in inches, in): ')
  #Area of block
  block_area = (int(length_block)* int(height_block))/144
  # Total blocks used in this wall
  blocks = wall_area / block_area
  print('\nTotal Blocks for this wall '+str(blocks))
  return blocks

def Other_wall():
  #gets how many doors windows exc in wall
  num_of_holes = input('\nPlease enter the number of doors, windows, holes,.. exc in walls: ')
  holes_area = []
  # gets areas of holes windows exc in wall
  for x in range(0, int(num_of_holes)):
    length_of_holes = input('\nPlease enter the length of doors, windows, hole,.. exc of hole'+str(x+1)+' (in feet,ft): ')
    height_of_holes = input('\nPlease enter the height of doors, windows, hole,.. exc of hole'+str(x+1)+' (in feet,ft): ')
    hole_area = int(length_of_holes)*int(height_of_holes)
    holes_area.append(hole_area)
  #length of wall
  length_solid_wall = input('\nEnter the legnth of the Wall(in feet,ft): ')
  #width of wall
  height_solid_wall = input('\nEnter the height of the Wall(in feet,ft): ')
  #area of wall
  wall_area = int(length_solid_wall)*int(height_solid_wall)
  #length of block
  length_block = input('\nEnter the legnth of the blocks(in inches, in): ')
  #width of block
  height_block = input('\nEnter the height of the blocks(in inches, in): ')
  #area  of block
  block_area = (int(length_block)* int(height_block))/144
  #number of blocks in this wall
  blocks = (wall_area - sum(holes_area) )/ block_area
  print('\nTotal Blocks for this wall '+str(blocks))
  return blocks


for i in range(0,int(walls)):
  print("\nWall #" + str(i+1))
  solid_wall = input('\nIs it a solid wall without any windows, door, hole,...: (yes or no)')
  if(solid_wall == 'yes'):
    blocks = Solid_wall()    
    blocks_for_walls.append(blocks)
  else:
    blocks = Other_wall()    
    blocks_for_walls.append(blocks)
  
    
# adds up total number of blocks used in every wall
totalblocks = sum(blocks_for_walls)
print("\nTotal blocks needed in all walls is: \n"+str(totalblocks))

import csv
import pandas as pd


blocks_for_walls = []
walls_items = []

walls = input('Please enter a how many walls there are: ')

def create_row(length_wall,height_wall,holes,area_holes,wall_area,length_block,height_block,blocks):
  walls_item ={
    'Length_of_Wall' : length_wall,
    'Height_of_the_Wall' : height_wall,
    'Number_of_Doors_windows_holes':holes,
    'Combined_Areas_of_all_Doors_windows_holes':area_holes,
    'Area_of_Wall' : wall_area,
    'Legnth_of_the_blocks' : length_block,
    'Heigth_of_the_blocks' : height_block,
    'Blocks_needed_for_Wall' : blocks,
    }
  walls_items.append(walls_item)

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
  create_row(length_solid_wall, height_solid_wall,'none','none',wall_area,length_block,height_block,blocks)
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
  create_row(length_solid_wall, height_solid_wall,num_of_holes,sum(holes_area),wall_area,length_block,height_block,blocks)
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

#create csv file
df = pd.DataFrame(walls_items)
df.to_csv('EstimationofWalls.csv')
''''
df = pd.read_csv('EstimationofWalls.csv')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Length_of_Wall, df.Height_of_the_Wall, df.Number_of_Doors_windows_holes, df.Combined_Areas_of_all_Doors_windows_holes, df.Area_of_Wall, df.Legnth_of_the_blocks,df.Heigth_of_the_blocks,df.Blocks_needed_for_Wall],
               fill_color='lavender',
               align='left'))
])



fig.show()
'''
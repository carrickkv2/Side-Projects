#Program which renames files for the Perfect Storm Mod.


import os
cwd = os .getcwd()

#old files names to change
old_file_name = 'stagesel.gfx'
old_file_name1 = 'stagesel_image.gfx'
old_file_name2 = 'charicon_s.gfx'

#new file names to change
new_file_name = 'ostagesel.gfx'
new_file_name1 = 'ostagesel_image.gfx'
new_file_name2 = 'ocharicon_s.gfx'

#loop through all the files in the directory and change all old files names to new file names
for root,  _,  files in os .walk( cwd ):
   for file in files:
      if file == old_file_name:
          old = os .path .join( root, old_file_name )
          new = os .path .join( root, new_file_name )
          os .rename( old, new )
      elif file == old_file_name1:
          old = os .path .join( root, old_file_name1 )
          new = os .path .join( root, new_file_name1 )
          os .rename( old, new )
      elif file == old_file_name2:
          old = os .path .join( root, old_file_name2 )
          new = os .path .join( root, new_file_name2 )
          os .rename( old, new )

# Author:  Anna Pronczak
# Date: 7 September 2017
# Purpose:  List feature classes in Newark geodatabase


# Import ArcPy
import arcpy
import os 

# Set the workspace
arcpy.env.workspace = "C:\\Users\\aip10\\Desktop\\Fall_2017\\606_Programming\\Week2\\Assignment2\\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
fcList = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for fc in fcList:
    print fc

# Print "Complete"
print "Complete"


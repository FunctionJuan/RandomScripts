#import(s)
import os
import shutil
#Set a directory
directory = r"C:\\this\\would\\be your working\\directory"
writingPath=r"C:\\this\\would\\be your destination\\directory"
def groupName():
    i=0
    for name in os.listdir(directory):
        #OpenFile:
        with open(os.path.join(directory, name)) as f:
            fullSongName = (f'{name}')
            groupName = (f'{name.split(' -')[0]}')
            if not os.path.exists(writingPath+"\\"+groupName):
                os.makedirs(writingPath+"\\"+groupName)
                print("The full song name is: ",fullSongName)
                print("The Path is : ", writingPath+"\\"+groupName)
            #if (groupName == writingPath+"\\"+)
            if(groupName == os.path.basename(writingPath+"\\"+groupName)):
                shutil.copy(directory+"\\"+fullSongName,writingPath+"\\"+groupName)
              #  print("This group name is : ",groupName, i,"and will go into: ", os.path.basename(writingPath+"\\"+groupName))
                i = i +1
            #print("This is the recently wrote path",os.path.basename(writingPath+"\\"+groupName))    
          
            #print(type(groupName), i)
            
           
        
        
        

groupName()
# def loopingSongs():
#     i = 0
#     l = 100
#     while i < 100:
#         print("This is Your Value :" , i)
#         i = i + 1

# loopingSongs()

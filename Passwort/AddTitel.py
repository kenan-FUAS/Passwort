import os


class AddTitel:
   def AddTitel(self):
       name= input("Neuer Titel:\t")
       path = os.getcwd()
       if path.endswith("PManager")==False:
        newPath = os.chdir(path+"/PManager")
       newTitel = open(name+".txt","w+")


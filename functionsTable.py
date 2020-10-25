class Funtable:
    #Declaration of atributes
    def __init__(self):
         self.__functionTable = []
    
    #Function to store new functions in the Function Table
    def addNewFunction(self, name, funtype, numberOfparams, typesOfParams, varTable):
        #Dictionary defined to store function data such as the nume, return type, number of parameters defined,
        #the type of the params, and a varTable to store our local variables with their type and value.
        functionToAdd = {
            'name' : name, 
            'type' : funtype, 
            'params' : numberOfparams, 
            'typesOfParams' : typesOfParams, 
            'varTable': varTable 
            }
        self.__functionTable.append[functionToAdd]
            
     #Function to search for a function in the table.
    def searchFunction(self, name):
        for function in self.table:
            if function['name'] == name:
                return function
        return False
    
    #Function to verify if the function has already been declared in the Function Table
    def checkFunctionExists(self, name):
        for function in self.table:
            if function['name'] == name:
                return True
        return True        
   
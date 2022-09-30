class employee:
    def __init__(self, name, IDNum, department, jobtitle, salary):
        self.__name= name
        self.__IDNum= IDNum
        self.__department= department
        self.__jobtitle= jobtitle
        self.__salary= salary


    def getname(self):
        return self.__name

    def getID(self):
        return self.__IDNum
    
    def getdepartment(self):
        return self.__department

    def getjob(self):
        return self.__jobtitle

    def getsal(self):
        return self.__salary
    
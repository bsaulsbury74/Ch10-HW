class PayrollDeduction:

    def __init__(self,description,date,amount,eID):

        self.__description= description
        self.__date=date
        self.__amount= amount
        self.__eID= eID

    def getdescription(self):
        return self.__description

    def getdate(self):
        return self.__date

    def getamount(self):
        return self.__amount

    def getID(self):
        return self.__eID
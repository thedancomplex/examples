class RobotClass:
    the_var = None
    the_global = None
    the_self = None

    def __init__(self, var):

        # Changes instance of the_var, viewable by rest of class
        self.the_var = var

        # local version of the_var not seen by the rest of class
        the_var = var * 2

        return

    def setGlobal(self, var):
        global the_global
        the_global = var
        return

    def setSelf(self, var):
        self.the_self = var
        return

    def getGlobal(self):

        # The statement below does NOT work as the_global is not defined
        # print(the_global)

        # This statement does work as it is an instance of classes "the_global"
        print(self.the_global)
        return

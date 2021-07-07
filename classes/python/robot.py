from RobotClass import RobotClass as RC

rc1 = RC(42)
rc2 = RC(57)


# We can easially initialize instance specific init values"
print("We can easially initialize instance specific init values")
print(rc1.the_var)
print(rc2.the_var)
print()

# Global changes are not viewable from outside the class
print("Global changes are not viewable from outside the class")
rc1.setGlobal(123)
rc2.setGlobal(-123)
print(rc1.the_global)
print(rc2.the_global)
print(rc1.the_global)
print()

# We can set global values manually
print("We can set global values manually")
rc1.the_global=123
rc2.the_global=-123
print(rc1.the_global)
print(rc2.the_global)
print()

# changes are not sent across classes
print("changes are not sent across classes")
print(rc1.the_global)
print(rc2.the_global)
print()

# These global values are perceitant
print("These global values are perceitant")
rc1.getGlobal()
rc2.getGlobal()
print()

# we can check the instance of the value and the within class verions of the vlaue
print("we can check the instance of the value and the within class verions of the vlaue")
print("instance 1")
rc1.checkGlobal()
print("instance 2")
rc2.checkGlobal()
print()

print("if we change the global in one class it will change in another class, thus changes to globals are percistant across classes instances but the instance version has not been changedchanged")
rc1.setGlobal(666)
rc2.checkGlobal()
print()

# Self changes are viewable outside the class
print("Self changes are viewable outside the class")
rc1.setSelf(3.14)
rc2.setSelf(-3.14)
print("instance 1")
print(rc1.the_self)
print("instance 2")
print(rc2.the_self)
print("instance 1 again")
print(rc1.the_self)
print()

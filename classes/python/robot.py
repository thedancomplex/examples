from RobotClass import RobotClass as RC

rc1 = RC(42)
rc2 = RC(57)

print(rc1.the_var)
print(rc2.the_var)

print()

# Global changes are not viewable from outside the class
rc1.setGlobal(123)
rc2.setGlobal(-123)
print(rc1.the_global)
print(rc2.the_global)
print(rc1.the_global)
print()

# We can set global values manually
rc1.the_global=123
rc2.the_global=-123
print(rc1.the_global)
print(rc2.the_global)
print(rc1.the_global)
rc1.getGlobal()
rc2.getGlobal()
print()


# Self changes are viewable outside the class
rc1.setSelf(3.14)
rc2.setSelf(-3.14)
print(rc1.the_self)
print(rc2.the_self)
print(rc1.the_self)
print()

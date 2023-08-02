#!/usr/bin/python3
BaseGeometry = __import__('3-base_geometry').BaseGeometry

def __dir__(cls):
        # get list of all attributes for this classand exclude_init_subclass
        attributes = super().__dir__()
        return [attributes for attributes in attributes if attributes != '__init_subclass__']
bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

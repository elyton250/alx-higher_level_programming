#!/usr/bin/python3


def add_attribute(obj, attribute_name, value):
    """Add a new attribute to an object if possible."""
    :wq

    if not hasattr(obj, "__dict__"):
        # Check if the object supports attribute assignment
        raise TypeError("can't add new attribute")
    # Use setattr to add the attribute with the specified name and value
    setattr(obj, attribute_name, value)

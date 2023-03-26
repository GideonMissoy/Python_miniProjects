class Subject:
    def __init__(self, name, category, clearance_level):
        self.name = name
        self.category = category
        self.clearance_level = clearance_level

class Object:
    def __init__(self, name, security_level):
        self.name = name
        self.security_level = security_level

class SecurityLevel:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class AccessMode:
    def __init__(self, name, level):
        self.name = name
        self.level = level

# Define the subjects
alice = Subject("Alice", "A", SecurityLevel("Low", 1))
bob = Subject("Bob", "B", SecurityLevel("Low", 1))
charlie = Subject("Charlie", "C", SecurityLevel("High", 2))

# Define the objects
doc1 = Object("Document 1", SecurityLevel("Low", 1))
doc2 = Object("Document 2", SecurityLevel("High", 2))
doc3 = Object("Document 3", SecurityLevel("High", 2))

# Define the security categories
category_a = ["A"]
category_b = ["B"]
category_c = ["C"]

# Define the access modes
read_access = AccessMode("Read", "read")
write_access = AccessMode("Write", "write")

# Define the access control logic
def read(subject, obj):
    if obj.name == "Document 1" and subject.category in category_a+category_b and subject.clearance_level.level >= obj.security_level.level:
        return True
    elif obj.name == "Document 2" and subject.category in category_c and subject.clearance_level.level >= obj.security_level.level:
        return True
    elif obj.name == "Document 3" and subject.category in category_b and subject.clearance_level.level >= obj.security_level.level:
        return True
    else:
        return False

def write(subject, obj):
    if obj.name == "Document 1" and subject.category in category_a+category_b and subject.clearance_level.level <= obj.security_level.level:
        return True
    elif obj.name == "Document 2" and subject.category in category_c and subject.clearance_level.level <= obj.security_level.level:
        return True
    elif obj.name == "Document 3" and subject.category in category_b and subject.clearance_level.level <= obj.security_level.level:
        return True
    else:
        return False

# Define the Bell-LaPadula model properties
def no_read_up(subject, obj):
    if subject.clearance_level.level >= obj.security_level.level:
        return True
    else:
        return False

def no_write_down(subject, obj):
    if subject.clearance_level.level <= obj.security_level.level:
        return True
    else:
        return False

def confinement(subject, obj):
    if subject.category in obj.name:
        return True
    else:
        return False

# Define a function to validate the Bell-LaPadula model properties for a given configuration
def validate_config(subjects, objects):
    for subject in subjects:
        for obj in objects:
            if not no_read_up(subject, obj) or not no_write_down(subject, obj) or not confinement(subject, obj):
                return False
    return True

# Define functions to check the Bell-LaPadula model properties
def check_SSC(subject, obj):
    if subject.clearance_level


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

def satisfies_ssc(subjects, objects):
    for obj in objects:
        max_clearance = SecurityLevel("Low", 0)
        for subject in subjects:
            if confinement(subject, obj) and subject.clearance_level.level > max_clearance.level:
                max_clearance = subject.clearance_level
        if obj.security_level.level > max_clearance.level:
            return False
    return True

def satisfies_star(subjects, objects):
    for obj in objects:
        min_clearance = SecurityLevel


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

def satisfies_ssc(subjects, objects):
    for obj in objects:
        max_clearance = SecurityLevel("Low", 0)
        for subject in subjects:
            if confinement(subject, obj) and subject.clearance_level.level > max_clearance.level:
                max_clearance = subject.clearance_level
        if obj.security_level.level > max_clearance.level:
            return False
    return True

# Check for the Star property
star_property = True
for obj in [doc1, doc2, doc3]:
    if obj.security_level.level == 1:
        for subject in [alice, bob, charlie]:
            if not read(subject, obj):
                star_property = False
                break
            if not write(subject, obj):
                star_property = False
                break

def check_discretionary_security():
    for subj in [alice, bob, charlie]:
        for obj in [doc1, doc2, doc3]:
            read_permitted = read(subj, obj)
            write_permitted = write(subj, obj)
            if read_permitted or write_permitted:
                print(f"{subj.name} has access to {obj.name}")
            else:
                print(f"{subj.name} does not have access to {obj.name}")

check_discretionary_security()

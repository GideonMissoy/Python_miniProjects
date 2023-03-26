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
        print(f"{subject.name} can read {obj.name}")
        return True
    elif obj.name == "Document 2" and subject.category in category_c and subject.clearance_level.level >= obj.security_level.level:
        print(f"{subject.name} can read {obj.name}")
        return True
    elif obj.name == "Document 3" and subject.category in category_b and subject.clearance_level.level >= obj.security_level.level:
        print(f"{subject.name} can read {obj.name}")
        return True
    else:
        print(f"{subject.name} cannot read {obj.name}")
        return False

def write(subject, obj):
    if obj.name == "Document 1" and subject.category in category_a+category_b and subject.clearance_level.level <= obj.security_level.level:
        print(f"{subject.name} can write to {obj.name}")
        return True
    elif obj.name == "Document 2" and subject.category in category_c and subject.clearance_level.level <= obj.security_level.level:
        print(f"{subject.name} can write to {obj.name}")
        return True
    elif obj.name == "Document 3" and subject.category in category_b and subject.clearance_level.level <= obj.security_level.level:
        print(f"{subject.name} can write to {obj.name}")
        return True
    else:
        print(f"{subject.name} cannot write to {obj.name}")
        return False

# Check the simple security condition
def check_simple_security():
    for obj in [doc1, doc2, doc3]:
        for subject in [alice, bob, charlie]:
            if not read(subject, obj):
                return False
    return True

# Test the access control logic and simple security condition
print("Access control test:")
read(alice, doc1)  # Output: Alice can read Document 1
read(bob, doc2)    # Output: Charlie can read Document 2
write(bob, doc1)   # Output


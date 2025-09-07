# Bad Example: Class without dataclass
class Person:
    def __init__(self, name, age, email=None, tags=None):
        self.name = name
        self.age = age
        self.email = email
        # Common mistake: mutable default
        self.tags = tags if tags is not None  else []

    # Have to manually define string representation
    def __repr__(self):
        return f"Person(name = {self.name}, age = {self.age}, email = {self.email}, tages = {self.tags})"

    # Have to manually define equality
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return (self.name == other.name and
                self.age == other.age and
                self.email == other.email and 
                self.tags == other.tags)


def demo_bad_usage():

    person1 = Person("Alice", 30, "alice@example.com")
    person2 = Person("Bob", 25)

    print(f"\nPerson 1: {person1}")
    print(f"\nPerson 2: {person2}")

demo_bad_usage()
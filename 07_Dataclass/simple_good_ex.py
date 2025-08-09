from dataclasses import dataclass, field

# Simple dataclass with type hints
@dataclass
class Person:
    name : str
    age : int
    email : str | None = None

    # Using field() with default factory for mutable default values
    tags: list[str] = field(default_factory=list)

    def is_adult(self) -> bool:
        return self.age >= 18


# Usage Example
def demo_good_usage():

    # Creating Instances
    person1 = Person(
        name = "Alice",
        age = 30,
        email = "alice@example.com"
    )

    person2 = Person(
        name = "Bob",
        age = 25
    )

    person3 = Person(
        name = "Charlie",
        age = 17,
        tags = ["student", "part-time"]
    )

    # Adding to a mutable field
    person1.tags.append("developer")

    # Using the built-in string represenation
    print(f"\nPerson 1: {person1}")
    print(f"\nPerson 2: {person2}")
    print(f"\nPerson 3: {person3}")

    # Using the instance method
    print(f"\nIs {person1.name} an adult? {person1.is_adult()}")
    print(f"\nIs {person3.name} an adult? {person3.is_adult()}")

demo_good_usage()
class Developer:
    def __init__(self):
        self.problem_solving = False
        self.collaboration = False
        self.adaptability = False
        self.logic = False
        self.mathematics = False
        self.planning = False

    def describe(self):
        traits = []
        if self.problem_solving:
            traits.append("Problem Solving")
        if self.collaboration:
            traits.append("Collaboration")
        if self.adaptability:
            traits.append("Adaptability")
        if self.logic:
            traits.append("Logic")
        if self.mathematics:
            traits.append("Mathematics")
        if self.planning:
            traits.append("Planning")
        print("This developer has the following personality traits:")
        for idx, trait in enumerate(traits, start=1):
            print(f"{idx}. {trait}")
        print(f"Total traits: {len(traits)}")


class DeveloperBuilder:
    def __init__(self):
        self.developer = Developer()

    def with_problem_solving(self):
        self.developer.problem_solving = True
        return self

    def with_collaboration(self):
        self.developer.collaboration = True
        return self

    def with_adaptability(self):
        self.developer.adaptability = True
        return self

    def with_logic(self):
        self.developer.logic = True
        return self

    def with_mathematics(self):
        self.developer.mathematics = True
        return self

    def with_planning(self):
        self.developer.planning = True
        return self

    def build(self):
        return self.developer


# Building a Developer instance with all traits
builder = DeveloperBuilder()
developer = (builder
             .with_problem_solving()
             .with_collaboration()
             .with_adaptability()
             .with_logic()
             .with_mathematics()
             .with_planning()
             .build())

# Output the result
developer.describe()

# Important steps in the program
print("\nImportant Steps in Program:")
steps = [
    "1. Define the Developer class with default traits set to False.",
    "2. Create a DeveloperBuilder class to set desired traits.",
    "3. Use the builder methods to enable specific traits.",
    "4. Build the developer object.",
    "5. Print out the traits and total number of traits."
]
for step in steps:
    print(step)
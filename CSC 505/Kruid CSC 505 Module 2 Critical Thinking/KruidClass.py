class KruidModel:
    def __init__(self):
        self.phases = []
        self.feedback_loops = []

    def input_phase(self, phase):
        phases_input = input("Enter the phases of your Waterfall model, separated by commas:\n")
        self.phases = [phase.strip() for phase in phases_input.split(",")]

    def input_feedback_loops(self):
        print("Enter feedback loops in format 'FromPhase -> ToPhase'. Type 'done' when finished.")
        while True:
            loop = input("Feedback loop: ")
            if loop.lower() == 'done':
                break
            if '->' in loop:
                self.feedback_loops.append(loop.strip())
            else:
                print("Invalid format. Please use 'FromPhase -> ToPhase' format.")

    def display_model(self):
        print("\nKruid Model Summary")
        print("------------------------------")
        print("Phases:")
        for idx, phase in enumerate (self.phases,1):
            print(f"{idx}- {phase}")

        if self.feedback_loops:
            print("\nFeedback Loops:")
            for loop in self.feedback_loops:
                print(f"- {loop}")
        else:
            print("No feedback loops defined.")

if __name__ == "__main__":
    model = KruidModel()
    model.input_phase("Requirements, Design, Implementation, Testing, Maintenance")
    model.input_feedback_loops()
    model.display_model()

    
def print_actors_and_use_cases():
    actors = {
        "Citizen": "Logs pothole reports and damage claims",
        "CityCrew": "Repair crew updates work orders and statuses",
        "Supervisor": "Oversees assignments and priorities"
    }
    use_cases = {
        "Submit Pothole Report": "Citizen logs a pothole with details (address, severity, size, location)",
        "Report Pothole Damage": "Citizen reports damage caused by a pothole (type, estimated cost)",
        "Assign Repair Crew": "Supervisor creates and assigns a work order for pothole repair",
        "Update Work Order": "CityCrew updates repair details (crew ID, time, equipment, status, filler material, cost)",
        "Calculate Repair Cost": "System calculates cost based on crew/time/material usage",
        "Manage Pothole Data": "System stores and prioritizes pothole records"
    }
    print("Actors:")
    for actor, desc in actors.items():
        print(f"- {actor}: {desc}")
    print("\nUse Cases:")
    for i, (name, desc) in enumerate(use_cases.items(), 1):
        print(f"{i}. {name}: {desc}")

if __name__ == "__main__":
    print_actors_and_use_cases()

# Unit - 3
# Constraint Satisfaction Problem (CSP)
# Subject Timetable using Backtracking

subjects = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

# Constraints:
# Maths and Python cannot be at the same time
# DBMS and AI cannot be at the same time

def is_valid(subject, slot, assignment):
    # Check Maths and Python constraint
    if subject == "Maths" and assignment.get("Python") == slot:
        return False

    if subject == "Python" and assignment.get("Maths") == slot:
        return False

    # Check DBMS and AI constraint
    if subject == "DBMS" and assignment.get("AI") == slot:
        return False

    if subject == "AI" and assignment.get("DBMS") == slot:
        return False

    return True


def backtracking(assignment):
    # All subjects are assigned
    if len(assignment) == len(subjects):
        return assignment

    # Select an unassigned subject
    for subject in subjects:
        if subject not in assignment:
            variable = subject
            break

    # Try each time slot
    for slot in time_slots:
        print("Trying:", variable, "=", slot)

        # Check constraints
        if is_valid(variable, slot, assignment):
            assignment[variable] = slot

            result = backtracking(assignment)

            if result is not None:
                return result

            # Backtrack
            del assignment[variable]

    return None


# Start CSP
solution = backtracking({})

# Display final timetable
print("\n----- FINAL TIMETABLE -----")

if solution:
    for subject in subjects:
        print(subject, "->", solution[subject])
else:
    print("No solution found.")
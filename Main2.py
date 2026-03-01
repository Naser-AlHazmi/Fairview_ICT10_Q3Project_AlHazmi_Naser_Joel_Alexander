from pyscript import display, document

def sign(e):

    # Get radio checked state and input values
    
    access_1 = document.getElementById("student1_access").checked  # Check if registered online
    
    access_2 = document.getElementById("student2_access").checked  # Check if has medical clearance
    
    grade_selection = document.getElementById("grade").value  # Get selected grade
    
    section = document.getElementById("section").value  # Get selected section

    
    if not grade_selection or not section: # Check if grade or section is not selected
    
        document.getElementById("output1").innerHTML = "Please fill in all fields."
    
        e.preventDefault()
    
        return
    
    digits = ''.join(ch for ch in grade_selection if ch.isdigit()) # Extract digits from grade selection
    
    grade_number = int(digits) if digits else 0 # Convert to integer, default to 0 if no digits found
    
    if not access_1: # Check if registered online
    
        document.getElementById("output1").innerHTML = "You need to register online first."
    
        e.preventDefault()
    
        return
    
    if not access_2: # Check if has medical clearance
    
        document.getElementById("output1").innerHTML = "You need to secure a medical clearance."
    
        e.preventDefault()
    
        return
    
    if grade_number < 7 or grade_number > 10: # Check if grade is between 7 and 10
    
        document.getElementById("output1").innerHTML = "Only students in grades 7-10 are eligible."
    
        e.preventDefault()
    
        return
    
    teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"] # List of teams
    
    Num = document.getElementById("section") # Get section element

    team_index = int(Num.value) - 1 # Get team index based on section value

    assigned_team = teams[team_index] # Get assigned team based on index
    
    message = ( 
    
        "Congratulations! You are eligible to join the Intramurals.<br>"
    
        f"Your team is: <strong>{assigned_team}</strong><br>"
    
        f"Welcome, {grade_selection} - {section}."
    
    ) 
    
    document.getElementById("output1").innerHTML = message
    
    e.preventDefault()
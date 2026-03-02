from pyscript import display, document; import webbrowser

def Signup(e):

    # get input values

    name = document.getElementById("name").value #input value

    password = document.getElementById("password").value #input value

    # check if name and password are not empty

    if not name or not password: #if either is empty

        document.getElementById("output").innerHTML = "Please enter both username and password." #display error message

        e.preventDefault()

    elif name == "alexander" and password == "alexander123": #Secret

        document.location.href = "image2.gif"

        e.preventDefault()

    elif name == "naser" and password == "naser123": #Secret

        document.location.href = "image3.gif"

        e.preventDefault()

    elif name == "Dela Cruz" and password == "Dela Cruz123":

        document.location.href = "team.html"

        e.preventDefault()

    elif name == "Juan Miguel" and password == "Juan Miguel123":

        document.location.href = "team.html"

        e.preventDefault()

    elif name == "cortisolspike" and password == "cortisolspike123": #Secret

        webbrowser.open("https://youtube.com/shorts/4djt69C-Dfw?si=UC_luv1dXEEh1WvZ")

        e.preventDefault()

    elif len(password) >= 10 and len(name) >= 7: #if password and name is valid

        if not password.isalpha(): #if password contains only letters
    
            if not password.isdigit(): #if password contains only digits

                document.location.href = "team.html" #moves to team.html

                e.preventDefault()

        else: #if password is invalid
            
            document.getElementById("output").innerHTML = "Invalid password! Password must be at least 10 characters long and contain both letters and numbers." #display error message

            e.preventDefault()

    else:

        document.getElementById("output").innerHTML = "Invalid password! Username must contain 10 letters, and Password must be at least 10 characters long and contain both letters and numbers." #display error message

        e.preventDefault()

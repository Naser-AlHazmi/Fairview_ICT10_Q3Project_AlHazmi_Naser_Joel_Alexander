from pyscript import display, document; import webbrowser

def Signup(e):

    # get input values

    name = document.getElementById("name").value #input value

    username = document.getElementById("username").value #input value

    password = document.getElementById("password").value #input value

    # check if name and password are not empty

    if not username or not password: #if either is empty

        document.getElementById("output").innerHTML = "Please enter both username and password." #display error message

        e.preventDefault()

    elif name == "alexander" and password == "alexander123": #Secret

        document.location.href = "image2.gif"

        e.preventDefault()

    elif name == "naser" and password == "naser123": #Secret

        document.location.href = "image3.gif"

        e.preventDefault()

    elif name == "cortisolspike" and password == "cortisolspike123": #Secret

        webbrowser.open("https://youtube.com/shorts/4djt69C-Dfw?si=UC_luv1dXEEh1WvZ")

        e.preventDefault()

    elif name == "Dela Cruz" and len(username) >= 7 and password == "Dela Cruz123": #if name is "Dela Cruz" and username is valid and password is valid

        document.location.href = "team.html" 

        e.preventDefault()

    elif name == "Juan Miguel" and len(username) >= 7 and password == "Juan Miguel123": #if name is "Juan Miguel" and username is valid and password is valid

        document.location.href = "team.html"

        e.preventDefault()

    elif len(password) >= 10 and len(username) >= 7: #if password and username is valid

        if not password.isalpha(): #if password contains only letters
    
            if not password.isdigit(): #if password contains only digits

                document.location.href = "team.html" 

                e.preventDefault()

        else: #if password is invalid
            
            document.getElementById("output").innerHTML = "Invalid password! Password must be at least 10 characters long and contain both letters and numbers." #display error message

            e.preventDefault()

    else:

        document.getElementById("output").innerHTML = "Invalid username/password! Username must contain 7 letters, and Password must be at least 10 characters long and contain both letters and numbers." #display error message

        e.preventDefault()

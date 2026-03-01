from pyscript import display, document

def generateList(e):
    
    players = ["Aguido", "Al Hazmi", "Reyes", "Gavina", "Cruz", "Janayan", "Buo", "Singh", "Manuel", "Del Prado", "Haberia", "Tan", "Banaag", "Zaldivar", "Castro", "Lubo", "Fransisco", "Vargas", "Brion", "Barcelona", "Entrada", "Mariposque", "Pagtalunan", "Guevarra", "Subaan", "Goyenechea" ]  # List of teams

    list_html = "<ul>"  # Start of unordered list

    for player in players:
        list_html += f"<li>{player}</li>"  # Add each player as a list item

    list_html += "</ul>"  # End of unordered list

    document.getElementById("playersList").innerHTML = list_html  # Display the generated list in the output element
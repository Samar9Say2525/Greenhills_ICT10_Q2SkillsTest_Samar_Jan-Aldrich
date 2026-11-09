from pyscript import display,document


def element_checker(e):
    document.getElementById('result').innerHTML = ' '
    user_input = document.getElementById('input_symbol').value.capitalize().strip()

    Elements ={
    'H':{'Name':"Hydrogen",'Mass':1.088,'Number':1},
    'C':{'Name':"Carbon",'Mass':12.011,'Number':6},
    'N':{'Name':"Nitrogen",'Mass':14.007,'Number':7},
    'O':{'Name':"Oxygen",'Mass':15.999,'Number':8},
    'P':{'Name':"Phosphorus",'Mass':30.974,'Number':15},
    'S':{'Name':"Sulfur",'Mass':32.06,'Number':16},
    'Se':{'Name':"Selenium",'Mass':78.971,'Number':34},
    'F':{'Name':"Fluorine",'Mass':18.998,'Number':9},
    'Cl':{'Name':"Chlorine",'Mass':35.45,'Number':17},
    'Br':{'Name':"Bromine",'Mass':79.904,'Number':35},
    'I':{'Name':"Iodine",'Mass':126.904,'Number':53},
    'At':{'Name':"Astatine",'Mass':210,'Number':85},
    'Ts':{'Name':"Tennessine",'Mass':294,'Number':117},
    'He':{'Name':"Helium",'Mass':4.0026,'Number':2},
    'Ne':{'Name':"Neon",'Mass':20.180,'Number':10},
    'Ar':{'Name':"Argon",'Mass':39.948,'Number':18},
    'Kr':{'Name':"Krypton",'Mass':83.798,'Number':36},
    'Xe':{'Name':"Xenon",'Mass':131.293,'Number':54},
    'Rn':{'Name':"Radon",'Mass':222,'Number':86},
    'Og':{'Name':"Oganesson",'Mass':294,'Number':118}
    }

    attributes = Elements.get(user_input, {
        'Name': 'Not Found in the list or not a non-metallic element',
        'Number': 'N/A',
        'Mass': 'N/A'
    })

    display(f"Symbol: {user_input}", target="result")
    
    display(f"Element: {attributes['Name']}", target="result")

    display(f"Atomic Number: {attributes['Number']}", target="result")

    display(f"Atomic Mass: {attributes['Mass']}", target="result")



# Student Information Sheet Output 
from pyscript import display, document 

def student_information(e):
    document.getElementById('output').innerHTML = ""
    data1 = document.getElementById('input1').value
    data2 = document.getElementById('input2').value
    data3 = document.getElementById('input3').value

    message= f"""Student Information
    Name: {data1} \"
    Age: {data2} \"
    School: {data3} \"

    Notes: \n
    \"{data1} is a student who is {data2} and is studying at {data3}"

    """
    display(message, target="output")
    display(f'Name:{data1}')
    display(f'Age:{data2}')
    display(f'School:{data3}')
    
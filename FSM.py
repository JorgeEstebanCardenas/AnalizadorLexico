

letras = [i for i in range(65, 91)] + [i for i in range(97, 123)]
numeros = [i for i in range(48, 58)]
espacio = [32]
vacios = [10, 32]
igual = [61]
operaciones = [43, 45, 42, 47]
L = [ord("l")]
E = [ord("e")]
T = [ord("t")]
punto = [ord(".")]
puntoycoma = [ord(";")]


estados = {
    "q0": [(L, "q1")],
    "q1": [(E, "q2")],
    "q2": [(T, "q3")],
    "q3": [(vacios, "q4")],
    "q4": [(vacios, "q4"), (letras, "q5")],
    "q5": [(letras + numeros, "q5"), (vacios, "q6"), (igual, "q7")],
    "q6": [(vacios, "q6"), (igual, "q7")],
    "q7": [(vacios, "q8"), (numeros, "q9")],
    "q8": [(vacios, "q8"), (numeros, "q9")],
    "q9": [(numeros, "q9"), (punto, "q10"), (vacios, "q12"), (operaciones, "q13"), (puntoycoma, "q15")],
    "q10": [(numeros, "q11")],
    "q11": [(numeros, "q11"), (vacios, "q12"), (operaciones, "q13"), (puntoycoma, "q15")],
    "q12": [(vacios, "q12"), (operaciones, "q13")],
    "q13": [(vacios, "q14"), (numeros, "q9")],
    "q14": [(vacios, "q14"), (numeros, "q9")],
    "q15": [(vacios, "q16"), (L, "q1")],
    "q16": [(vacios, "q16"), (L, "q1")],
}

def step(char, state):

    connections = estados.get(state, None)

    try:
        for connection in connections:
            if ord(char) in connection[0]:
                #print(state + " input: " + char + " -> " + connection[1])
                return connection[1]
    except:
        return "error"

    #print(state + " input: " + char + " -> " + "error")
    return "error"


def readfile():
    file_path = "input.txt"

    with open(file_path, "r") as f:
        content = ""
        line = f.readline()

        while line:
            content += line
            line = f.readline()

    #print(content)
    return content


if __name__ == "__main__":
    input = readfile()

    current = "q0"

    error_found = False

    for l in input:
        current = step(l, current)

        if current == "error":
            error_found = True
            break


    if error_found:
        print("Error")
    else:
        if current == "q15" or current == "q16":
            print("Aceptado")
        else:
            print("No aceptado")


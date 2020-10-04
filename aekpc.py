import optparse

alphanum = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789 "
payload = ""
simbolos = {
    "!": 33,
    "[": 34,
    "#": 35,
    "$": 36,
    "%": 37,
    "/": 38,
    "{": 39,
    ")": 40,
    "=": 41,
    "(": 42,
    "¡": 43,
    ",": 44,
    "'": 45,
    ".": 46,
    "-": 47,
    "Ñ": 58,
    "ñ": 59,
    ";": 60,
    "¿": 61,
    ":": 62,
    "_": 63,
    "\"": 64,
    "´": 91,
    "}": 92,
    "+": 93,
    "&": 94,
    "?": 95,
    "|": 96,
    "¨": 123,
    "]": 124,
    "*": 125,
    "°": 126
}
posicionact = 0
posicionaini = 0

def aggSimbolo(sim):
    return 'Keyboard.write('+str(sim)+');'

def aggTexto(txt):
    return 'Keyboard.print(\"'+txt+'\");'

if __name__ == '__main__':
    parser = optparse.OptionParser('usage %prog -P <Payload>')
    parser.add_option('-P','--Payload', dest='Payload', type='string', help='Inserte el payload a convertir')
    (options, args) = parser.parse_args()
    payload = options.Payload
    print("Codificando payload: "+payload+"\n")
    for x in payload:
        if x not in alphanum:
            print(aggTexto(payload[posicionaini:posicionact]))
            posicionaini = (posicionact + 1)
            if x in simbolos:
                print(aggSimbolo(simbolos[x]))

        posicionact += 1
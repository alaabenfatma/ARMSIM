'''
	AUTHOR: ALAA BEN FATMA
	YEAR: 2019
'''
import sys
import re

'''
    Declarations
'''

# MOTS CLEFS
COMMENT = '@'
MOV = 'MOV'
ADD = 'ADD'
SUB = 'SUB'
CMP = 'CMP'
LDR = 'LDR'
STR = 'STR'
LSL = 'LSL'
LSR = 'LSR'
BAL = 'BAL'
BEQ = 'BEQ'
BNE = 'BNE'
ETIQ = 'ETIQ'
PUSH = 'PUSH'
POP  = 'POP'


class Lexeme:
    def __init__(self, type, valeur):
        if(type == 'MOV'):
            self.type = MOV
        elif type == 'ADD':
            self.type = ADD
        elif type == 'SUB':
            self.type = SUB
        elif type == 'CMP':
            self.type = CMP
        elif type == 'LDR':
            self.type = LDR
        elif type == 'STR':
            self.type = STR
        elif type == 'LSL':
            self.type = LSL
        elif type == 'LSR':
            self.type = LSR
        elif type == 'BAL':
            self.type = BAL
        elif type == 'BEQ':
            self.type = BEQ
        elif type == 'BNE':
            self.type = BNE
        elif type == 'PUSH':
            self.type = PUSH
            valeur = valeur.replace('{','').replace('}','')
        elif type == 'POP':
            self.type = POP
            valeur = valeur.replace('{','').replace('}','')
        elif ':' in type:
            self.type = ETIQ
            etq = re.search(regex_etiquette, type).group(0)
            valeur = etq[:-1]
        else:
            self.type = COMMENT
        valeur = valeur.replace('\n', '')
        self.valeur = (valeur).replace(' ', '')

    def afficher(self):
        print("[NATURE = ", self.type, ", VALEUR = ", self.valeur, "]")


POSITION = 0
CODE = []
INSTRUCTIONS = []

REGISTRES = {
    'r0': 0,
    'r1': 0,
    'r2': 0,
    'r3': 0,
    'r4': 0,
    'r5': 0,
    'r6': 0,
    'r7': 0,
    'r8': 0,
    'r9': 0,
    'r10': 0,
    'r11': 0,
    'r12': 0,
    'r13': 0,
    'r14': 0,
    'r15': 0,
}

FLAGS = {
    'Z': 0,
    'C': 0,
}
FakeMemory = []

'''
REGULAR EXPRESSIONS
'''
# Commentaires
regex_comment = r'@.*'
# Les etiquettes
regex_etiquette = r'.*\:'
# Les piles
regex_stack = r'\{.*?\}'

'''
    Analyse Lexical
'''


def LireFichier(path):
    global CODE
    with open(path, 'r') as f:
        for line in f.readlines():
            line = re.sub(regex_comment, r'', line)
            line= line.lstrip()
            if(':' in line):
                twoLines = line.split(':')
                CODE.append(twoLines[0]+':')
                CODE.append(twoLines[1][1:])
                continue
            CODE.append(line)


def afficher_lexemes(lexemes):
    for l in lexemes:
        l.afficher()

# Convert #xyz > int(xyz)


def toNum(x):
    return int(x[1:])


def Analyse_Lex():
    lexemes = []
    LireFichier(sys.argv[1])

    for mot in CODE:
        parts = mot.partition(' ')
        keyword = parts[0]
        argument = parts[2]
        L = Lexeme(keyword.upper(), argument)
        lexemes.append(L)
    return lexemes


'''
    Analyse Syntaxique
'''


def checkNum(x):
    if('#' in x):
        return (x[1:])
    else:
        return x


def Generate_Instructions(lexemes):
    global INSTRUCTIONS
    for l in lexemes:
        cmd = l.type
        val = l.valeur.split(',')
        INSTRUCTIONS.append([cmd, val])


def indexOfEtiq(id):
    c = 0
    id = id[0].upper()
    for i in INSTRUCTIONS:
        if(i[0] == 'ETIQ'):
            if(id == i[1][0]):
                break
        c += 1
    return c


def eval(x, y, z, op):
    if('#' in z):
        z = toNum(z)
    else:
        z = REGISTRES[z]
    if('#' in y):
        y = toNum(y)
    else:
        y = REGISTRES[y]
    if(op == '+'):
        REGISTRES.update({x: int(y)+int(z)})
    elif op == '-':
        REGISTRES.update({x: int(y)-int(z)})
    elif op == '*':
        REGISTRES.update({x: int(y)*int(z)})
    elif op == 'LSL':
        REGISTRES.update({x: int(y)*(2 ^ int(z))})
    elif op == 'LSR':
        REGISTRES.update({x: int(y)/(2 ^ int(z))})


def mov(inst):
    global REGISTRES
    r = inst[1]
    if('#' in r):
        REGISTRES.update({inst[0]: int(checkNum(inst[1]))})
    else:
        REGISTRES.update({inst[0]: REGISTRES[r]})


def cmp(x, y):
    global FLAGS
    if('#' in y):
        y = toNum(y)
        FLAGS.update({'C': int(REGISTRES[x] - y)})
    else:
        FLAGS.update({'C': REGISTRES[x] - REGISTRES[y]})


def beq():
    if(FLAGS['C'] == 0):
        return True
    return False


def bal(index):
    Execute(index)


def Execute(startFrom=0):
    global REGISTRES
    for inst in INSTRUCTIONS[startFrom:]:
        print("Executing : ", inst)
        if(inst[0] == 'MOV'):
            mov(inst[1])
        elif(inst[0] == 'ADD'):
            eval(inst[1][0], inst[1][1], inst[1][2], '+')
        elif(inst[0] == 'SUB'):
            eval(inst[1][0], inst[1][1], inst[1][2], '-')
        elif(inst[0] == 'MULT'):
            eval(inst[1][0], inst[1][1], inst[1][2], '*')
        elif(inst[0] == 'LSL'):
            eval(inst[1][0], inst[1][1], inst[1][2], 'LSL')
        elif(inst[0] == 'LSR'):
            eval(inst[1][0], inst[1][1], inst[1][2], 'LSR')
        elif(inst[0] == 'PUSH'):
            FakeMemory.append(REGISTRES[inst[1][0]])
        elif(inst[0] == 'POP'):
            x = FakeMemory.pop()
            print(x)
            REGISTRES[inst[1][0]] = x
        elif(inst[0] == 'BAL'):
            index = indexOfEtiq(inst[1])
            Execute(index)
            break
        elif(inst[0] == 'CMP'):
            cmp(inst[1][0], inst[1][1])
        elif(inst[0] == 'BEQ'):
            if((beq())):
                index = indexOfEtiq(inst[1])
                Execute(index)
                return
            else:
                continue
        elif(inst[0] == 'BNE'):
            if(not(beq())):
                index = indexOfEtiq(inst[1])
                Execute(index)
                return
            else:
                continue
        else:
            continue


def main():
    global REGISTRES
    lexemes = Analyse_Lex()
    Generate_Instructions(lexemes)
    Execute()
    for r in REGISTRES:
        print(r, '=', REGISTRES[r])


if __name__ == "__main__":
    main()

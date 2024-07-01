import pandas as pd

pd.set_option('display.width', 1600)
pd.set_option('display.max_columns', 100)
def norte():
    while True:
        print("1.Porto (1863 - 2018)")
        print("2.bragancanca (1863 - 2018)")
        print("3.Montalegre (1863 - 2018)")
        print("4.Penhas Douradas (1863 - 2018)")
        print("5.Voltar...")
        op = input("Escolha a regiao central: (1-7) ")
        if op == '1':
            porto()
        elif op == '2':
            braganca()
        elif op == '3':
            montalegre()
        elif op == '4':
            penhasDouradas()
        elif op == '5':
            print("5. A Voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-8)!")
def centro():
    while True:
        print("1.Castelo Branco (1863 - 2018)")
        print("2.Coimbra (1863 - 2018)")
        print("3.Evora (1863 - 2018)")
        print("4.Lisboa (1863 - 2018)")
        print("5.Portalegre (1863 - 2018)")
        print("6.Setubal (1863 - 2018)")
        print("7.Santarem (1863 - 2018)")
        print("8.Voltar...")
        op = input("Escolha a regiao central: (1-7) ")
        if op == '1':
            casteloBranco()
        elif op == '2':
            coimbra()
        elif op == '3':
            evora()
        elif op == '4':
            lisboa()
        elif op == '5':
            portalegre()
        elif op == '6':
            setubal()
        elif op == '7':
            santarem()
        elif op == '8':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-8)!")
def sul():
    while True:
        print("1.Beja (1863 - 2018)")
        print("2.Faro (1863 - 2018)")
        print("3.Voltar...")
        op = input("Escolha a regiao central: (1-3) ")
        if op == '1':
            beja()
        elif op == '2':
            faro()
        elif op == '3':
            print("3. A Voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-8)!")
def ilhas():
    while True:
        print("1.Terceira (1863 - 2018)")
        print("2.Funchal (1863 - 2018)")
        print("3.Ponta Delgada (1863 - 2018)")
        print("4.Voltar...")
        op = input("Escolha a regiao central: (1-4) ")
        if op == '1':
            terceira()
        elif op == '2':
            funchal()
        elif op == '3':
            pontaDelgada()
        elif op == '4':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-8)!")
def terceira():

    terceira = "porto.xlsx"
    terceira_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(terceira, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def faro():
    faro = "porto.xlsx"
    faro_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(faro, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def funchal():
    funchal = "porto.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(funchal, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def pontaDelgada():
    pontaDelgada = "porto.xlsx"
    pontaDelgada_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(pontaDelgada, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def porto():
    porto = "porto.xlsx"
    porto_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(porto, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def penhasDouradas():

    penhasDouradas = "porto.xlsx"
    penhasDouradas_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(penhasDouradas, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def montalegre():

    montalegre = "montalegre.xlsx"
    montalegre_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(montalegre, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def beja():
    beja = "beja.xlsx"
    beja_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(beja, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def casteloBranco():
    casteloBranco = "casteloBranco.xlsx"
    casteloBranco_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(casteloBranco, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def coimbra():
    coimbra = "coimbra.xlsx"
    coimbra_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(coimbra, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def braganca():
    braganca = "braganca.xlsx"
    braganca_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(braganca, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def evora():
    evora = "evora.xlsx"
    evora_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(evora, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def lisboa():
    lisboa = "evora.xlsx"
    lisboa_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(lisboa, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def portalegre():
    portalegre = "evora.xlsx"
    portalegre_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(portalegre, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def setubal():
    setubal = "evora.xlsx"
    setubal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(setubal, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())
def santarem():
    santarem = "evora.xlsx"
    santarem_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(santarem, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    meta = dfs['meta']
    print(meta.to_string())

    tmin = dfs['tmin']
    print(tmin.to_string())

    tmax = dfs['tmax']
    print(tmax.to_string())

    prec = dfs['prec']
    print(prec.to_string())


def main():
    while True:
        print("1.Norte")
        print("2.Centro")
        print("3.Sul")
        print("4.Ilhas")
        print("5.Sair.")
        op = input("Escolha a regiao que pretende: (1-5) ")
        if op == '1':
            norte()
        elif op == '2':
            centro()
        elif op == '3':
            sul()
        elif op == '4':
            ilhas()
        elif op == '5':
            print("Exiting...")
            break
        else:
            print("Escolha uma opcao valida (1-5)!")

if __name__ == "__main__":
    main()

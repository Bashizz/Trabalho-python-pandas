import pandas as pd

pd.set_option('display.width', 1600)
pd.set_option('display.max_columns', 13)
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
    terceira = "terceira.xlsx"
    terceira_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(terceira, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

    while True:
        print("1.Informacao de dados::")
        print("2.Precepitacao minima:")
        print("3.Precepitacao maxima:")
        print("4.Precepitacao:")
        print("5.Voltar:")
        op = input("Escolha a Informacao que deseja ver: (1-5) ")

        if op == '1':
            meta = dfs['meta']
            print(meta.to_string())
        elif op == '2':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(terceira, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(terceira, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(terceira, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(terceira, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(terceira, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(terceira, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")

def faro():
    faro = "faro.xlsx"
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
    funchal = "funchal.xlsx"
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
    pontaDelgada = "pontaDelgada.xlsx"
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

    penhasDouradas = "penhasDouradas.xlsx"
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
    lisboa = "lisboa.xlsx"
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
    portalegre = "portalegre.xlsx"
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
    setubal = "setubal.xlsx"
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
    santarem = "santarem.xlsx"
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

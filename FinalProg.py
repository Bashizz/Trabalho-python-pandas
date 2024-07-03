import pandas as pd

pd.set_option('display.width', 1600)
pd.set_option('display.max_columns', 1000)
def norte():
    while True:
        print("1.Porto (1863 - 2018)")
        print("2.bragancanca (1863 - 2018)")
        print("3.Montalegre (1863 - 2018)")
        print("4.Penhas Douradas (1863 - 2018)")
        print("5. Ver todos os dados")
        print("6. Voltar...")
        op = input("Escolha a regiao: (1-6) ")
        if op == '1':
            porto()
        elif op == '2':
            braganca()
        elif op == '3':
            montalegre()
        elif op == '4':
            penhasDouradas()
        elif op == '5':
            norte_ver_todos_os_dados()
        elif op == '6':
            print("6. A Voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-6)!")

def sul():
    while True:
        print("1.Beja (1863 - 2018)")
        print("2.Faro (1863 - 2018)")
        print("3.Ver todos os dados.")
        print("4.Voltar...")
        op = input("Escolha a regiao: (1-3) ")
        if op == '1':
            beja()
        elif op == '2':
            faro()
        elif op == '3':
            sul_ver_todos_os_dados()
        elif op == '4':
            print("4. A Voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-8)!")
def ilhas():
    while True:
        print("1. Terceira (1863 - 2018)")
        print("2. Funchal (1863 - 2018)")
        print("3. Ponta Delgada (1863 - 2018)")
        print("4. Ver todos os dados")
        print("5. Voltar...")
        op = input("Escolha a regiao: (1-5) ")
        if op == '1':
            terceira()
        elif op == '2':
            funchal()
        elif op == '3':
            pontaDelgada()
        elif op == '4':
            ilhas_ver_todos_os_dados()
        elif op == '5':
            print("A voltar...")
            break
        else:
            print("Escolha uma opcao valida (1-5)!")
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
            print('4.Escolher mes e ano')
            print('5.Voltar')
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
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(terceira, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
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
                df = pd.read_excel(terceira, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
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
            elif op == '4':
                df = pd.read_excel(terceira, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def ilhas_ver_todos_os_dados():
    # Define a dictionary for sheet name descriptions
    sheet_descriptions = {
        'tmin': 'Precipitação Minima',
        'tmax': 'Precipitação Máxima',
        'prec': 'Precipitação'
    }

    # Load the three Excel files, excluding the metadata sheet if identified
    terceira_sheets = pd.read_excel('terceira.xlsx', sheet_name=None)
    funchal_sheets = pd.read_excel('funchal.xlsx', sheet_name=None)
    ponta_delgada_sheets = pd.read_excel('pontaDelgada.xlsx', sheet_name=None)

    # Initialize empty dictionaries to collect dataframes with descriptions
    terceira_data = {}
    funchal_data = {}
    ponta_delgada_data = {}

    # Process Terceira sheets

    for sheet_name, df in terceira_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            terceira_data[description] = df

    for sheet_name, df in funchal_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            funchal_data[description] = df


    for sheet_name, df in ponta_delgada_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            ponta_delgada_data[description] = df

    # Create a new Excel writer object
    with pd.ExcelWriter('IlhasMerged.xlsx') as writer:
        # Write Terceira data to a sheet
        for description, df in terceira_data.items():
            df.to_excel(writer, sheet_name=f'Terceira - {description}', index=False)

        # Write Funchal data to a sheet
        for description, df in funchal_data.items():
            df.to_excel(writer, sheet_name=f'Funchal - {description}', index=False)

        # Write Ponta Delgada data to a sheet
        for description, df in ponta_delgada_data.items():
            df.to_excel(writer, sheet_name=f'Ponta Delgada - {description}', index=False)

    print("Ficheiros mergidos num so com o nome IlhasMerged.xlsx")
def norte_ver_todos_os_dados():
    # Define a dictionary for sheet name descriptions
    sheet_descriptions = {
        'tmin': 'Precipitação Minima',
        'tmax': 'Precipitação Máxima',
        'prec': 'Precipitação'
    }

    # Load the three Excel files, excluding the metadata sheet if identified
    porto_sheets = pd.read_excel('porto.xlsx', sheet_name=None)
    bragancanca_sheets = pd.read_excel('braganca.xlsx', sheet_name=None)
    Montalegre_sheets = pd.read_excel('Montalegre.xlsx', sheet_name=None)
    penhas_Douradas_sheets = pd.read_excel('penhasDouradas.xlsx', sheet_name=None)

    # Initialize empty dictionaries to collect dataframes with descriptions
    bragancanca_data = {}
    montalegre_data = {}
    porto_data = {}
    penhas_Douradas_data = {}
    # Process Terceira sheets

    for sheet_name, df in bragancanca_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            bragancanca_data[description] = df

    for sheet_name, df in Montalegre_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            montalegre_data[description] = df

    for sheet_name, df in porto_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            porto_data[description] = df

    for sheet_name, df in penhas_Douradas_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            penhas_Douradas_data[description] = df

    # Create a new Excel writer object
    with pd.ExcelWriter('NorteMerged.xlsx') as writer:

        for description, df in bragancanca_data.items():
            df.to_excel(writer, sheet_name=f'bragancanca - {description}', index=False)

        for description, df in montalegre_data.items():
            df.to_excel(writer, sheet_name=f'Montalegre - {description}', index=False)

        for description, df in porto_data.items():
            df.to_excel(writer, sheet_name=f'Porto - {description}', index=False)

        for description, df in penhas_Douradas_data.items():
            df.to_excel(writer, sheet_name=f'Penhas Douradas - {description}', index=False)

    print("Ficheiros mergidos num so com o nome NorteMerged.xlsx")
def centro():
    while True:
        print("1.Castelo Branco (1863 - 2018)")
        print("2.Coimbra (1863 - 2018)")
        print("3.Evora (1863 - 2018)")
        print("4.Lisboa (1863 - 2018)")
        print("5.Portalegre (1863 - 2018)")
        print("6.Setubal (1863 - 2018)")
        print("7.Santarem (1863 - 2018)")
        print("8.Ver todos os dados")
        print("9.Voltar...")
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
            centro_ver_todos_os_dados()
        elif op == '9':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-8)!")
def centro_ver_todos_os_dados():

    # Define a dictionary for sheet name descriptions
    sheet_descriptions = {
        'tmin': 'Precipitação Minima',
        'tmax': 'Precipitação Máxima',
        'prec': 'Precipitação'
    }

    # Load the three Excel files, excluding the metadata sheet if identified
    coimbra_sheets = pd.read_excel('coimbra.xlsx', sheet_name=None)
    evora_sheets = pd.read_excel('evora.xlsx', sheet_name=None)
    lisboa_sheets = pd.read_excel('lisboa.xlsx', sheet_name=None)
    portalegre_sheets = pd.read_excel('portalegre.xlsx', sheet_name=None)
    setubal_sheets = pd.read_excel('setubal.xlsx', sheet_name=None)
    santarem_sheets = pd.read_excel('santarem.xlsx', sheet_name=None)
    castelo_Branco_sheets = pd.read_excel('CasteloBranco.xlsx', sheet_name=None)

    # Initialize empty dictionaries to collect dataframes with descriptions
    coimbra_data = {}
    evora_data = {}
    lisboa_data = {}
    portalegre_data = {}
    setubal_data = {}
    santarem_data = {}
    castelo_Branco_data = {}

    for sheet_name, df in coimbra_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            coimbra_data[description] = df

    for sheet_name, df in evora_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            evora_data[description] = df

    for sheet_name, df in lisboa_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            lisboa_data[description] = df

    for sheet_name, df in portalegre_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            portalegre_data[description] = df

    for sheet_name, df in setubal_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            setubal_data[description] = df

    for sheet_name, df in santarem_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            santarem_data[description] = df

    for sheet_name, df in castelo_Branco_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            castelo_Branco_data[description] = df


    # Create a new Excel writer object
    with pd.ExcelWriter('CentroMerged.xlsx') as writer:

        for description, df in coimbra_data.items():
            df.to_excel(writer, sheet_name=f'coimbra - {description}', index=False)

        for description, df in evora_data.items():
            df.to_excel(writer, sheet_name=f'evora - {description}', index=False)

        for description, df in lisboa_data.items():
            df.to_excel(writer, sheet_name=f'lisboa - {description}', index=False)

        for description, df in portalegre_data.items():
            df.to_excel(writer, sheet_name=f'portalegre - {description}', index=False)

        for description, df in setubal_data.items():
            df.to_excel(writer, sheet_name=f'setubal - {description}', index=False)

        for description, df in santarem_data.items():
            df.to_excel(writer, sheet_name=f'santarem - {description}', index=False)

        for description, df in castelo_Branco_data.items():
            df.to_excel(writer, sheet_name=f'Castelo Branco - {description}', index=False)

    print("Ficheiros mergidos num so com o nome CentroMerged.xlsx")
def sul_ver_todos_os_dados():

    # Define a dictionary for sheet name descriptions
    sheet_descriptions = {
        'tmin': 'Precipitação Minima',
        'tmax': 'Precipitação Máxima',
        'prec': 'Precipitação'
    }


    beja_sheets = pd.read_excel('beja.xlsx', sheet_name=None)
    faro_sheets = pd.read_excel('faro.xlsx', sheet_name=None)

    beja_data = {}
    faro_data = {}

    for sheet_name, df in beja_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            beja_data[description] = df

    for sheet_name, df in faro_sheets.items():
        if 'meta' not in sheet_name.lower():
            description = sheet_descriptions.get(sheet_name, sheet_name)
            print(f"  - {description} (Sheet: {sheet_name})")
            faro_data[description] = df

    with pd.ExcelWriter('SulMerged.xlsx') as writer:
        for description, df in beja_data.items():
            df.to_excel(writer, sheet_name=f'beja - {description}', index=False)

        for description, df in faro_data.items():
            df.to_excel(writer, sheet_name=f'faro - {description}', index=False)

    print("Ficheiros mergidos num so com o nome SulMerged.xlsx")

def faro():
    faro = "faro.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(faro, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(faro, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(faro, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(faro, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(faro, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(faro, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(faro, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(faro, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(faro, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(faro, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def funchal():
    funchal = "funchal.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(funchal, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(funchal, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(funchal, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(funchal, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(funchal, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(funchal, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(funchal, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(funchal, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(funchal, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(funchal, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def pontaDelgada():
    pontaDelgada = "pontaDelgada.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(pontaDelgada, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(pontaDelgada, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(pontaDelgada, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(pontaDelgada, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(pontaDelgada, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(pontaDelgada, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(pontaDelgada, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(pontaDelgada, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(pontaDelgada, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(pontaDelgada, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def porto():
    porto = "porto.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(porto, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(porto, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(porto, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(porto, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(porto, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(porto, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(porto, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(porto, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(porto, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(porto, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def penhasDouradas():
    penhasDouradas = "penhasDouradas.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(penhasDouradas, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(penhasDouradas, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(penhasDouradas, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(penhasDouradas, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(penhasDouradas, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(penhasDouradas, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(penhasDouradas, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(penhasDouradas, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(penhasDouradas, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(penhasDouradas, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def montalegre():
    montalegre = "montalegre.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(montalegre, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(montalegre, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(montalegre, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(montalegre, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(montalegre, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(montalegre, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(montalegre, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(montalegre, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(montalegre, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(montalegre, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def beja():
    beja = "beja.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(beja, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(beja, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(beja, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(beja, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(beja, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(beja, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(beja, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(beja, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(beja, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(beja, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def casteloBranco():
    casteloBranco = "casteloBranco.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(casteloBranco, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(casteloBranco, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(casteloBranco, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(casteloBranco, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(casteloBranco, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(casteloBranco, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(casteloBranco, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(casteloBranco, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(casteloBranco, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(casteloBranco, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def coimbra():
    coimbra = "coimbra.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(coimbra, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(coimbra, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(coimbra, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(coimbra, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(coimbra, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(coimbra, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(coimbra, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(coimbra, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(coimbra, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(coimbra, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def braganca():
    braganca = "braganca.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(braganca, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(braganca, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(braganca, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(braganca, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(braganca, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(braganca, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(braganca, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(braganca, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(braganca, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(braganca, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def evora():
    evora = "evora.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(evora, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(evora, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(evora, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(evora, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(evora, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(evora, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(evora, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(evora, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(evora, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(evora, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def lisboa():
    lisboa = "lisboa.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(lisboa, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(lisboa, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(lisboa, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(lisboa, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(lisboa, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(lisboa, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(lisboa, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(lisboa, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(lisboa, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(lisboa, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def portalegre():
    portalegre = "portalegre.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(portalegre, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(portalegre, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(portalegre, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(portalegre, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(portalegre, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(portalegre, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(portalegre, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(portalegre, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(portalegre, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(portalegre, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def setubal():
    setubal = "setubal.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(setubal, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(setubal, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(setubal, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(setubal, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(setubal, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(setubal, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(setubal, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(setubal, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(setubal, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(setubal, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")
def santarem():
    santarem = "santarem.xlsx"
    funchal_sheets = ['meta', 'tmin', 'tmax', 'prec']
    dfs = pd.read_excel(santarem, sheet_name=['meta', 'tmin', 'tmax', 'prec'])

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
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmin = dfs['tmin']
                print(tmin.to_string())
            elif op == '2':
                df = pd.read_excel(santarem, sheet_name='tmin')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(santarem, sheet_name='tmin')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(santarem, sheet_name='tmin')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '3':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                tmax = dfs['tmax']
                print(tmax.to_string())
            elif op == '2':
                df = pd.read_excel(santarem, sheet_name='tmax')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(santarem, sheet_name='tmax')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(santarem, sheet_name='tmax')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '4':
            print('1.Ver tudo')
            print('2.Escolher ano')
            print('3.Escolher mes')
            print('4.Escolher mes e ano')
            print('5.Voltar')
            op = input()
            if op == '1':
                prec = dfs['prec']
                print(prec.to_string())
            elif op == '2':
                df = pd.read_excel(santarem, sheet_name='prec')
                ano = int(input('Indique o ano (1863 - 2018): '))
                filtered_df = df[df['year'] == ano]
                print(filtered_df.to_string())
            elif op == '3':
                df = pd.read_excel(santarem, sheet_name='prec')
                mes = input('Indique o mes (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dez): ')
                if mes in df.columns:
                    month_data = df[['year', mes]]
                    print(month_data.to_string())
                else:
                    print("Mes nao existe!")
            elif op == '4':
                df = pd.read_excel(santarem, sheet_name='prec')
                print(df.columns)
                ano = int(input('Indique o ano (1863 - 2018): '))
                mes = input('Indique o mês (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ')
                if 'year' in df.columns and mes in df.columns:
                    filtered_df = df[df['year'] == ano]
                    month_data = filtered_df[['year', mes]]
                    print(month_data)
                else:
                    print("Ano ou mes nao existem!")
            elif op == '5':
                print("A voltar...")
                break;
        elif op == '5':
            print("A voltar...")
            break;
        else:
            print("Escolha uma opcao valida (1-5)!")

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
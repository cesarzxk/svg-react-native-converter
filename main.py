import time
print('''
-----------------------------------------------------------------------
Project available in the cesarzxk/svg-react-native-converter repository
-----------------------------------------------------------------------
''')

looping = True;


while(looping):
    filename = input('Entre com o nome do arquivo svg: ').strip() + '.svg'
    destiny = input('Entre com o nome do arquivo de saida com extensão (ex: arquivo.js): ')

    imports = []

    try:
            
        with open(filename, 'r') as svg:
            for i in svg:
                try:
                    index  = i.index(' ')
                    newi = i[1:index].capitalize()
                    imports.append(newi)

                except:
                    try:
                        index  = i.index('/')
                    except:
                        newi = i[1:len(i)-2].capitalize()
                        imports.append(newi)
                        
            
            if imports[0]=='Svg':
                imports.pop(0)

            svg.seek(0)

            newimports = ''

            imports = list(set(imports))

            for i in imports:
                if (i == imports[len(imports)-1]):
                    newimports = newimports + i
                else:
                    newimports = newimports + i + ','


            with open(destiny, 'w') as destiny:
                destiny.write("import React from 'react';\n")
                destiny.write("import Svg,{"+newimports+"}from 'react-native-svg';\n")
                
                for i in svg:
                    if(i[1] == "/"):
                        newi = i[2:].capitalize()
                        destiny.write('</'+newi)

                    else:
                        newi = i[1:].capitalize()
                        destiny.write('<'+newi)

        print('''
------------------------Sucesso------------------------
<>----------arquivo convertido com sucesso----------</>
-------------------------------------------------------
        ''')
        restart = True

        while(restart):

            response = input('Deseja continuar convertendo?(n/s): ').lower()

            if(response == 'n'):
                print('''
|------------------------------------------------------|
|-----------------Thanks for using!:D------------------|
|------------------------------------------------------|
                ''')

                time.sleep(3)
                restart = False
                looping = False
                

            elif(response == 's'):
                restart = False
    except:
        print('''
-------------------------Erro!-------------------------
<>--------------arquivo não encontrado--------------</>
-------------------------------------------------------
        ''')

        




def contador(file_name):  
    try:
        with open (file_name) as arquivo:
            leitor = arquivo.read()  

    except FileNotFoundError:
        print("O arquivo '{}'não existe!".format(file_name))
    
    else:
        print("O numero de palavras no arquivo '{}' é {}!".format(file_name, len(leitor.split())))

contador("teste.txt")
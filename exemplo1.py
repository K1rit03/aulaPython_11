while True:
    try:
        a = int(input('Digite um numero: '))
        b = int(input('Digite um numero: '))
        if a < 0 or b < 0:
            raise TypeError              # gera uma exceção
        c = a/b
        print(f'Resultado: {c}')
    except TypeError:
        print('Error: o numero deve ser positivo')
    except ValueError:
        print("ERRO: O valor informado deve ser inteiro")
    except ZeroDivisionError:
        print("ERRO: Ocorreu uma divisão por zero")
    except Exception as msg:
        print("ERRO inesperado? {msg2}")
    else:
        print("operação executada com sucesso")
        break
   
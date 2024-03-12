class Calculadora:
    
    def __init__(self, valor=0.00):
        self.__registrador = valor
        self.__registrador_anterior = []
        
    def __salvar_registrador_anterior(self):
        self.__registrador_anterior.append(self.__registrador)
        
    def adicionar(self, somado):
        self.__salvar_registrador_anterior()
        self.__registrador += somado
        
    def subtrair(self, subtraido):
        self.__salvar_registrador_anterior()
        self.__registrador -= subtraido
    
    def dividir(self, dividido):
        if dividido != 0:
            self.__salvar_registrador_anterior()
            self.__registrador /= dividido
        else:
            print("Erro: divisão por zero.")
    
    def multiplicar(self, multiplicado):
        self.__salvar_registrador_anterior()
        self.__registrador *= multiplicado
        
    def get_registrador(self):
        return self.__registrador
        
    def reset(self):
        self.__registrador = 0.00
        
    def undo(self):
        if self.__registrador_anterior:
            self.__registrador = self.__registrador_anterior.pop()
        else:
            print('Não tem mais nada para desfazer')

    def exibir(self):
        print(f'O registrador é {self.__registrador}')
        
    def __str__(self):
        return f'A calculadora foi criada com o valor {self.__registrador} no registrador'
    
class InterfaceUsuario:
    def __init__(self):
        self.__calculadora = Calculadora()
        
    def exibir_menu(self):
        while True:
            print(f"""+--------------+
| {self.__calculadora.get_registrador():.2f} |
+--------------+
(+) somar
(-) subtrair
(/) dividir
(*) multiplicar
(r) resetar
(d) desfazer
(s) Sair da calculadora
---------------""")
            operacao = input('Operação: ')
            if operacao != 'r' and operacao != 'd' and operacao != 's':
                try:
                    valor = float(input('Valor: '))                  
                    if operacao == '+':
                        self.__calculadora.adicionar(valor)
                    elif operacao == '-':
                        self.__calculadora.subtrair(valor)
                    elif operacao == '/':
                        self.__calculadora.dividir(valor)
                    elif operacao == '*':
                        self.__calculadora.multiplicar(valor)
                    elif operacao == 'r':
                        self.__calculadora.reset()
                    elif operacao == 'd':
                        self.__calculadora.undo()
                    elif operacao == 's':
                        break
                    else:
                        print('Operação inválida!')
                except ValueError:
                    print('Digite um valor válido')                    
            
if __name__ == '__main__':
    interface = InterfaceUsuario()
    interface.exibir_menu()
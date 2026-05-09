import json
import tkinter as tk
from brazilcep import get_address_from_cep
from tkinter import filedialog

#back
historico = []      #cria a lista de historico
historico_cep = []
def buscar():
    cep = entrada.get()     #pega o input do usuario

    try:                                        #tenta acessar os dados do input do usuario
        dados = get_address_from_cep(cep)       #pega os dados do banco de dados
        historico.append(dados)                 #adiciona os dados no historico
        historico_cep.append(dados.get('cep'))
        texto = f"""
Cep: {dados.get('cep', 'n/a')}
Cidade: {dados.get('city', 'n/a')}
Estado: {dados.get('uf', 'n/a')}
Bairro: {dados.get('district', 'n/a')}
Rua: {dados.get('street', 'n/a')} 
"""
        resultado.config(text=texto)

    except:
        resultado.config(text='Cep invalido')

def salvar_json():
    caminho = filedialog.asksaveasfilename(         #retorna o caminho escolhido pelo usuario
        defaultextension=".json",                   #define o tipo de arquivo
        filetypes=[("Arquivo JSON", "*.json")],
        )

    if caminho:
        with open(caminho, "w", encoding="utf-8") as f: #abrindo o arquivo de forma segura usando o "with"
            json.dump(historico, f) #descarrega todo conteudo no arquivo
        resultado.config(text="Arquivo salvo com sucesso")

def mostrar_historico():
    texto = ""
    
    for i in range(len(historico_cep)):     #adiciona cada elemento da lista historico na variavel texto
        texto += f"{historico_cep[i]}\n"
        
    resultado.config(text=f"Historico de ceps pesquisados:\n{texto}")

def limpar_historico():
    historico.clear()                           #limpa toda a lista de historico
    historico_cep.clear()
    resultado.config(text="Historico Limpo")

#front

janela = tk.Tk()                #cria a janela
janela.title("Buscar Cep")      #titulo da janela
janela.geometry("500x500")      #resoluçao da janela
janela.config(bg="#5C5E74")   #configuraçao de cor da janela

titulo = tk.Label(              #cria um texto dentro da janela
    janela,
    text="Buscar Cep",
    font=("Arial", 18, "bold"),
    bg="#5C5E74"
)
titulo.pack(pady=15)

entrada = tk.Entry(             #cria o input do usuario
    janela,
    font=("Arial", 14),
    justify="center"
)
entrada.pack(pady=10, ipadx=20, ipady=5)

botao_buscar = tk.Button(      #cria um botao
    janela,text="Buscar",
    width=20,
    command=buscar
)
botao_buscar.pack(pady=5)

botao_salvar = tk.Button(
    janela,
    text="Salvar Json",
    width=20,
    command=salvar_json
)
botao_salvar.pack(pady=5)

botao_mostrar = tk.Button(
    janela,
    text="Mostrar Histórico",
    width=20,
    command=mostrar_historico
)
botao_mostrar.pack(pady=5)

botao_limpar = tk.Button(
    janela,
    text="Limpar Histórico",
    width=20,
    command=limpar_historico
)
botao_limpar.pack(pady=5)

resultado = tk.Label(       #cria um output do programa
    janela,
    text="",
    bg="white",
    width=20,
    height=10,
    anchor="center",
    padx=20,
    pady=10
)
resultado.pack(pady=15)

janela.mainloop()           #deixa a janela aberta
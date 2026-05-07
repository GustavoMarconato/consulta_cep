import json
import tkinter as tk
from brazilcep import get_address_from_cep
from tkinter import filedialog

#back
historico = []
historico_cep = []
def buscar():
    cep = entrada.get()

    try:
        dados = get_address_from_cep(cep)
        historico.append(dados)
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
    caminho = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("Arquivo JSON", "*.json")],
        )

    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(historico, f)
        resultado.config(text="Arquivo salvo com sucesso")

def mostrar_historico():
    texto = ""
    
    for i in range(len(historico_cep)):
        texto += f"{historico_cep[i]}\n"
        
    resultado.config(text=f"Historico de ceps pesquisados:\n{texto}")

def limpar_historico():
    historico.clear()
    historico_cep.clear()
    resultado.config(text="Historico Limpo")

#front

janela = tk.Tk()
janela.title("Buscar Cep")
janela.geometry("500x500")
janela.config(bg="#5C5E74")

titulo = tk.Label(
    janela,

    text="Buscar Cep",
    font=("Arial", 18, "bold"),
    bg="#5C5E74"
)
titulo.pack(pady=15)

entrada = tk.Entry(
    janela,
    font=("Arial", 14),
    justify="center"
)
entrada.pack(pady=10, ipadx=20, ipady=5)

botao_buscar = tk.Button(
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

resultado = tk.Label(
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

janela.mainloop()
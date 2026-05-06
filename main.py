
import json
import tkinter as tk
from brazilcep import get_address_from_cep
from tkinter import filedialog
historico = []

def limpar_historico():
    historico.clear()
    with open("ceps.json", "w", encoding="utf-8") as f:
        json.dump([], f)
    resultado.config(text='Historico limpo!')


def salvar_json():
    caminho = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("Arquivo Json", "*.json")],
        title="salvar arquivo JSON"
    )

    if caminho:
        with open(caminho, "w", encoding="utf=8") as f:
            json.dump(historico, f, ensure_ascii=False, indent=4)
        resultado.config(text="Arquivo salvo com sucesso")


def buscar():
    cep = entrada.get()
    try:
        dados = get_address_from_cep(cep)
        historico.append(dados)
        texto = f"""
CEP: {dados.get('cep', 'N/A')}
Cidade: {dados.get('city', 'N/A')}
Estado: {dados.get('uf', 'N/A')}
Bairro: {dados.get('district', 'N/A')}
Rua: {dados.get('street', 'N/A')}
"""
        resultado.config(text=texto)
    except Exception as e:
        resultado.config(text="CEP inválido")
        print(e)


janela = tk.Tk()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Buscar", command=buscar)
botao.pack()

botao_salvar = tk.Button(janela, text="Salvar Json", command=salvar_json)
botao_salvar.pack()

botao_limpar = tk.Button(janela, text="Limpar historico", command=limpar_historico)
botao_limpar.pack()

resultado = tk.Label(janela, text="")
resultado.pack()



janela.mainloop()



#
# FILE MANAGER
# Instalação: sudo apt-get install python3-tk
#

from tkinter import *
from tkinter import filedialog
from shutil import copyfile

# Tela do File Manager
def browseFile():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Selecione um Arquivo",filetypes=[("Tipo de Arquivo","*.txt")])
    # Alterar o conteudo
    label_file.configure(text = "Arquivo Aberto: " + filename)
    copyfile(filename,"./file.txt")

# Criando uma Tela Inicial
window = Tk()

# Definindo o título da tela
window.title("Gerenciador de Arquivos")

# Definindo tamanho da tela
window.geometry("800x500")

# Definindo a cor de fundo da tela
window.config(background = "white")

# Label interno da tela
label_file = Label(window,text = "Abrindo Arquivo para envio",width = 100, height = 4,fg = "green")

# Botão de encontrar o Arquivo
button_explore = Button(window,text = "Encontrar Arquivo",command = browseFile)

# Botão de fechar
button_exit = Button(window,text = "Sair",command = exit)

# Colocar as informações na tela
label_file.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1, row = 3)

# Esperando uma resposta
window.mainloop()
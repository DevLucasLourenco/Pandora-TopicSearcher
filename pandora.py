import tkinter as tk
from PIL import ImageTk, Image


class Pandora():
    
    def __init__(self):
        self.root = None

        self.pandora_view()

    
    
    def pandora_view(self):
        self.root = tk.Tk()
        self.root.title('Pandora - Busca Web')
        self.root.geometry('800x600+500+100')
        self.root.resizable(False, False)
        

        imagem_fundo = 'utilidades/'

        image_frame = tk.Label(self.root, image=imagem_fundo)
        image_frame.place(x=0, y=0, relwidth=1, relheight=1)

        # Crie o frame central
        frame_central = tk.Frame(self.root,height=500, width=600, bd=0, highlightthickness=0, bg='black')
        frame_central.place(relx=0.5, rely=0.5, anchor="center")
        
        
        frame_label_pandora_texto = tk.Frame(frame_central,height=0, width=20, bd=0, highlightthickness=0, bg='black')
        frame_label_pandora_texto.place(relx=0.5, rely=0.05, anchor='n')
        
        
        label_pandora = tk.Label(frame_label_pandora_texto, text='Pandora\nBusca Web', anchor='center', font= 'bold',  bg='purple', fg='white', borderwidth=2, relief='solid')
        label_pandora.grid(row=0, column=0, padx=20, pady=20, columnspan=3, sticky='ew')
        
        
        
        
        
        self.root.mainloop()     






if __name__ == '__main__':
    instancia = Pandora()
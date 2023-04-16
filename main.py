from tkinter import *
from customtkinter import *

root = Tk()
root.geometry("800x600")
root.title("Gobrosko")
root.iconbitmap("icon.ico")
root.resizable(False, False)

# Arka plan rengi
root.configure(bg='white')

# Oyun başlık etiketi
label_title = Label(root, text="Gobrosko", font=("Helvetica", 48), fg='black', bg='white')
label_title.pack(pady=50)

# Oyun açıklama etiketi
label_description = Label(root, text="Sinir bozan bir yılan oyunu.\nOyunun adı Gobrosko ve tabikide yılanın adı da Gobrosko...\n\nYıllar yıllar önce bir yılan yaşarmış. Tek amacı elmaları yemek olan\nbu yılan yıllardır elma yiyor, ama artık sıkılmış durumda.\nHaydi onun işini hızlandıralım.\n\nGobrosko...", font=("Helvetica", 15), fg='#777', bg='white')
label_description.pack(pady=20)

def start():
    import game

# Başla düğmesi
btn_start = CTkButton(root, text="Başla", font=CTkFont("Helvetica", 24), text_color='white', fg_color='#E74C3C', bg_color="white", hover_color="#151515", corner_radius=10, height=40, command=start)
btn_start.pack(pady=75)

root.mainloop()

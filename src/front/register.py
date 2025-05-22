from tkinter import Button, Entry, Label, Tk, messagebox
from src.domain.dtos import UserDTO
from src.services import UserService
from .activies import ListActivies
from src.common.base import TkinterBase

class Register(TkinterBase):
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("Tela de Cadastro")
        self.master.geometry("300x200")
        self.master.resizable(True, True)

        # Usuário
        self.label_username = Label(master, text="Usuário:")
        self.label_username.pack(pady=(20, 5))
        self.entry_username = Entry(master)
        self.entry_username.pack()

        # Email
        self.label_email = Label(master, text="Email:")
        self.label_email.pack(pady=(20, 5))
        self.entry_email = Entry(master)
        self.entry_email.pack()

        # Senha
        self.label_password = Label(master, text="Senha:")
        self.label_password.pack(pady=(10, 5))
        self.entry_password = Entry(master, show="*")
        self.entry_password.pack()

        # Botão de login
        self.button_register = Button(master, text="Entrar", command=self.register)
        self.button_register.pack(pady=20)

    def register(self):
        data = UserDTO.create(
            self.entry_username.get(), self.entry_email.get(), self.entry_password.get()
        )

        try:
            data.validate()
            service = UserService()
            service.create_user(data)
            messagebox.showinfo("Cadastro bem-sucedido", "Bem-vindo, admin!")
            self.master.destroy()
            self.open_window(ListActivies, destroy=True)
        except ValueError as e:
            messagebox.showerror("Cadastro falhou", f"{e}")

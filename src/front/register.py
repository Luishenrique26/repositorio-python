from tkinter import Button, Entry, Label, Tk, messagebox

from src.domain.dtos.user_dto import UserDTO
from src.services.user_service import UserService
from .activies import ListarActivies


class Register:
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

        # Senha
        self.label_password = Label(master, text="Senha:")
        self.label_password.pack(pady=(10, 5))
        self.entry_password = Entry(master, show="*")
        self.entry_password.pack()

        # Botão de login
        self.button_register = Button(master, text="Entrar", command=self.register)
        self.button_register.pack(pady=20)

    def register(self):
        data = UserDTO.create(self.entry_username.get(), self.entry_password.get())

        try:
            data.validate()
            service = UserService()
            service.create_user(data)
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo, admin!")
            self.master.destroy()
            self.open_window(ListarActivies)
        except ValueError as e:
            messagebox.showerror("Cadastro falhou", f"{e}")

    def open_window(self, window):
        new_window = Tk()
        window(new_window)
        return

from tkinter import Button, Entry, Label, Tk, messagebox
from src.domain.dtos.user_dto import UserDTO
from .activies import ListarActivies
from .register import Register
class Login:
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("Tela de Login")
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
        self.button_login = Button(master, text="Entrar", command=self.login)
        self.button_login.pack(pady=20)

        # Botão de cadastro
        self.button_register = Button(master, text="Cadastrar", command=self.register)
        self.button_register.pack(pady=20)

    def login(self):
        data = UserDTO.create(self.entry_username.get(), self.entry_password.get())

        try:
            data.validate()
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo, admin!")
            self.master.destroy()
            self.open_window()
        except ValueError as e:
            messagebox.showerror("Login falhou", f"{e}")

    def open_window(self):
        new_window = Tk()
        app = ListarActivies(new_window)
        return

    def register(self):
        self.master.destroy()
        new_window = Tk()
        register = Register(new_window)
        return

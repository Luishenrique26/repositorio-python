import re
from tkinter import Tk, Label, Button, messagebox, Entry
from src.domain.dtos import ActiviesDTO
from src.services import ActiviesService
from src.common.base import TkinterBase
# Dados simulados

class AddActivitie(TkinterBase):
    def __init__(self, master: Tk):
        self.master = master

        self.master.title("Adicionar atividade")
        self.master.geometry("900x400")
        self.master.resizable(False, False)

        self.label_name = Label(self.master, text="Nome da Atividade:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_start_date = Label(self.master, text="Data de inicio:")
        self.label_start_date.grid(row=1, column=0, padx=5, pady=5)

        self.entry_start_date = Entry(self.master)
        self.entry_start_date.grid(row=1, column=1, padx=5, pady=5)
        # self.entry_start_date.insert(0, "DD/MM/AAAA")
        # self.entry_start_date.config(
        #     validate = "key",
        #     validatecommand = (
        #         self.master.register(
        #             lambda date: f"{re.sub(r'^(\d{0,2})(\d{0,2})(\d{0,4})$', lambda m: f'{m.group(1)}/{m.group(2) if m.group(2) else ""}/{m.group(3) if m.group(3) else ""}', date)}"
        #         ),
        #         "%P",
        #     ),
        # )

        self.label_end_date = Label(self.master, text="Data de fim:")
        self.label_end_date.grid(row=2, column=0, padx=5, pady=5)

        self.entry_end_date = Entry(self.master)
        self.entry_end_date.grid(row=2, column=1, padx=5, pady=5)
        # self.entry_end_date.insert(0, "DD/MM/AAAA")
        # self.entry_end_date.config(
        #     validate="key",
        #     validatecommand=(
        #         self.master.register(lambda date: f"{date[:2]}/{date[2:4]}/{date[4:]}"),
        #         "%P",
        #     ),
        # )

        self.button_add = Button(self.master, text="Adicionar", command=self.add_activitie)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


    def add_activitie(self):
        name = self.entry_name.get()
        start_date = self.entry_start_date.get()
        end_date = self.entry_end_date.get()

        dto = ActiviesDTO.create(name=name, start_date=start_date, end_date=end_date)
        try:
            dto.validate()
            service = ActiviesService()
            service.create_activie(dto)
            messagebox.showinfo("Cadastro bem-sucedido", "Atividade cadastrada com sucesso!")
            self.master.destroy()
            self.open_window(ListActivies, destroy=True)
        except ValueError as e:
            messagebox.showerror("Cadastro falhou", f"{e}") 

class ListActivies(TkinterBase):
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("Lista de atividades")
        self.master.geometry("900x400")
        self.master.resizable(False, False)

        self.rows = []

        self.btn_add = Button(self.master, text="Adicionar", command=lambda: self.open_window(AddActivitie))
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.render_header()
        self.render_data()

    def render_header(self):
        headers = ["ID", "Nome", "Início", "Fim", "Criado em", "Atualizado em", "", ""]
        for col, text in enumerate(headers):
            Label(self.master, text=text, font=("Arial", 10, "bold")).grid(
                row=0, column=col, padx=5, pady=5
            )

    def render_data(self):
        service = ActiviesService()
        data = service.get_activies()
        if not data:
            return 
        for idx, item in enumerate(data):
            self.add_row(item, idx + 1)

    def add_row(self, item, row_idx):
        labels = []
        values = [
            item["activitie_id"],
            item["name"],
            item["start_date"],
            item["end_date"],
            item["created_at"],
            item["updated_at"],
        ]
        for col, val in enumerate(values):
            lbl = Label(self.master, text=val)
            lbl.grid(row=row_idx, column=col, padx=5, pady=5)
            labels.append(lbl)

        btn_update = Button(
            self.master, text="Update", command=lambda i=item: self.update_item(i)
        )
        btn_update.grid(row=row_idx, column=6, padx=5)

        btn_delete = Button(
            self.master, text="Delete", command=lambda r=row_idx: self.delete_row(r)
        )
        btn_delete.grid(row=row_idx, column=7, padx=5)

        self.rows.append((labels, btn_update, btn_delete))

    def update_item(self, item):
        print(f"Atualizar item: {item['activitie_id']}")

    def delete_row(self, row_idx):
        row = self.rows[row_idx - 1]  # -1 porque a primeira linha é o cabeçalho

        keys = [
            "activitie_id",
            "name",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]
        values = {k: lbl.cget("text") for k, lbl in dict(zip(keys, row[0])).items()}

        print(f"rows: {values}")

        response = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o item {row[0][0].cget('text')}?",
        )
        if response is False:
            return

        for widget in row[0]:  # labels
            service = ActiviesService()
            service.delete_activie(values["activitie_id"])
            widget.destroy()
        row[1].destroy()  # botão update
        row[2].destroy()  # botão delete
        self.rows[row_idx - 1] = None

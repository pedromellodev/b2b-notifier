import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import threading
import time
from PIL import Image, ImageTk
import os
import sys

pasta_base = os.path.dirname(sys.executable)
caminho_logo = os.path.join(pasta_base, "logo.png")
caminho_reservas = os.path.join(pasta_base, "reservas.json")

def salvar_reserva():
    pj = entry_pj.get()
    razao_social = entry_razao_social.get()
    horario = entry_horario.get()

    try:
        horario_dt = datetime.strptime(horario, "%d/%m/%Y %H:%M")
        reserva = {
            "pj": pj,
            "razao_social": razao_social,
            "horario": horario
        }

        with open(caminho_reservas, "a") as f:
            f.write(json.dumps(reserva) + "\n")

        messagebox.showinfo("Sucesso", "Reserva salva com sucesso!")
        entry_pj.delete(0, tk.END)
        entry_razao_social.delete(0, tk.END)
        entry_horario.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Formato de data/hora inválido. Use dd/mm/aaaa hh:mm")

def verificar_reservas():
    while True:
        try:
            try:
                with open(caminho_reservas, "r") as f:
                    linhas = f.readlines()
            except FileNotFoundError:
                # Se o arquivo não existir na primeira vez, crie-o vazio
                open(caminho_reservas, "w").close()
                linhas = []

            agora = datetime.now().strftime("%d/%m/%Y %H:%M")
            print(f"[DEBUG] Verificando reserva às {agora}...")

            for linha in linhas:
                if not linha.strip():
                    continue
                reserva = json.loads(linha)
                print(f"[DEBUG] Comparando com reserva: {reserva['horario']}")

                if reserva["horario"] == agora:
                    mensagem = f"A reserva B2B {reserva['razao_social']}:\n{reserva['pj']} caiu."
                    messagebox.showinfo("Notificação de Reserva", mensagem)

        except Exception as e:
            print(f"[ERRO] {e}")

        time.sleep(30)

# Comando para iniciar a Thread
threading.Thread(target=verificar_reservas, daemon=True).start()

root = tk.Tk()
try:
    root.iconbitmap("logo.ico")
except tk.TclError:
    print("Aviso: Arquivo 'logo.ico' não encontrado.")
root.title("Ph B2B Notifier")
root.configure(bg="#1f1f1f")

largura_janela = 400
altura_janela = 400
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
root.resizable(False, False)

fonte_padrao = ("Helvetica", 12)
cor_texto = "white"
cor_campo = "#2c2c2c"
cor_botao = "#4CAF50"

try:
    logo_image = Image.open(caminho_logo)
    logo_image = logo_image.resize((70, 70))
    logo_tk = ImageTk.PhotoImage(logo_image)
    label_logo = tk.Label(root, image=logo_tk, bg="#1e1e1e")
    label_logo.pack(pady=10)
except FileNotFoundError:
    print(f"Erro: Arquivo '{caminho_logo}' não encontrado.")
    label_logo = tk.Label(root, text="B2B Notifier", font=fonte_padrao, bg="#1e1e1e", fg="white")
    label_logo.pack(pady=10)


def criar_entry():
    entry = tk.Entry(root, font=fonte_padrao, width=40, bg=cor_campo, fg=cor_texto, insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#555")
    return entry

tk.Label(root, text="CNPJ", font=fonte_padrao, bg="#1f1f1f", fg=cor_texto).pack(pady=(20,5))
entry_pj = criar_entry()
entry_pj.pack(pady=5)

tk.Label(root, text="Razão Social", font=fonte_padrao, bg="#1f1f1f", fg=cor_texto).pack(pady=(10,5))
entry_razao_social = criar_entry()
entry_razao_social.pack(pady=5)

tk.Label(root, text="Horário da Reserva (dd/mm/aaaa hh:mm)", font=fonte_padrao, bg="#1f1f1f", fg=cor_texto).pack(pady=(10,5))
entry_horario = criar_entry()
entry_horario.pack(pady=5)

btn_salvar = tk.Button(root, text="Salvar Reserva", font=fonte_padrao, bg=cor_botao, fg="white", width=20, height=2, bd=0, activebackground="#45a049", cursor="hand2", relief="flat", command=salvar_reserva)
btn_salvar.pack(pady=20)

root.mainloop()
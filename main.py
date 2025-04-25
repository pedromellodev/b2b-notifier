import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import threading
import time

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

        with open("reservas.json", "a") as f:
            f.write(json.dumps(reserva) + "\n")

        messagebox.showinfo("Salvo", "Reserva salva com sucesso!")
        entry_pj.delete(0, tk.END)
        entry_razao_social.delete(0, tk.END)
        entry_horario.delete(0, tk.END)

    except ValueError:
         messagebox.showerror("Erro", "Formato de data/hora inválido. Use dd/mm/aaaa hh:mm")

root = tk.Tk()
root.title("Ph B2B Notifier")

tk.Label(root, text = "CNPJ").pack()
entry_pj = tk.Entry(root, width=50)
entry_pj.pack()

tk.Label(root, text="Razão Social").pack()
entry_razao_social = tk.Entry(root, width=50)
entry_razao_social.pack()

tk.Label(root, text="Horário da Reserva (dd/mm/aaaa hh:mm)").pack()
entry_horario = tk.Entry(root, width=50)
entry_horario.pack()

tk.Button(root, text="Salvar Reserva", command=salvar_reserva).pack(pady=10)

root.mainloop()

def verificar_reservas():
    while True:
        try:
            with open("reservas.json", "r") as f:
                linhas = f.readlines()

            agora = datetime.now().strftime("%d/%m/%Y %H:%M")
            print(f"[DEBUG] Verificando reserva às {agora}...")

            for linha in linhas:
                if not linha.strip():
                    continue
                reserva = json.loads(linha)
                print(f"[DEBUG] Comparando com reserva:{reserva['horario']}")
                
                if reserva["horario"] == agora:
                    mensagem = f"Reserva B2B para {reserva['razao_social']}:\n{reserva['pj']}"
                    messagebox.showinfo("Notificação de Reserva", mensagem)
                horario_reserva = datetime.strptime(reserva["horario"], "%d/%m/%Y %H:%M")
                
        except Exception as e:
            print(f"ERRO {e}")

        time.sleep(30)

threading.Thread(target=verificar_reservas, daemon=True).start()
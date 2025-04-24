# B2B Notifier

**B2B Notifier** é uma aplicação simples desenvolvida em Python com o objetivo de auxiliar empresas que realizam **reservas B2B**. A ferramenta permite o cadastro de reservas com uma descrição, razão social e horário agendado — e exibe uma notificação pop-up no momento em que a reserva acontece.

## Funcionalidades

- Interface gráfica com campos para:
  - Descrição da reserva
  - Razão social
  - Data e hora da reserva
- Armazenamento das reservas em arquivo `.json`
- Notificações automáticas quando chega o horário agendado
- Simples, leve e pode ser transformado em `.exe` para uso em qualquer PC

## Tecnologias utilizadas

- Python 3.x
- Tkinter (interface gráfica)
- JSON (para persistência dos dados)
- PyInstaller (para empacotar como executável)

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/b2b-notifier.git
cd b2b-notifier

2. Instale as dependências:

pip install pyinstaller

3. Execute o programa:

python b2b_notifier.py


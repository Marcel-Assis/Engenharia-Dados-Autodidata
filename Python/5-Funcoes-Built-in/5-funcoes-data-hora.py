# Funções para manipulação de datas e horas:


# Obter a data e hora atual:
from datetime import datetime, timedelta, timedelta


agora = datetime.now()
print(agora)  # 2026-02-24 04:26:35.789012

# Obter apenas a data atual:
hoje = datetime.today().date()
print(hoje)  # 2026-02-24

# Criar uma data específica:
data_especifica = datetime(2024, 6, 15).date()
print(data_especifica)  # 2024-06-15

# Criar um horário específico:
horario_especifico = datetime(2024, 6, 15, 14, 30, 0).time()
print(horario_especifico)  # 14:30:00

# Criar um datetime específico:
datetime_especifico = datetime(2024, 6, 15, 14, 30, 0)
print(datetime_especifico)  # 2024-06-15 14:30:00

# Formatar datas e horas:
print(agora.strftime("%d/%m/%Y %H:%M:%S"))  # 24/02/2026 04:26:35

# Parse de strings para datas:
# %d dia
# %m mês
# %Y ano
# %H hora
# %M minuto
# %S segundo
data_str = "24/02/2026"
data_parse = datetime.strptime(data_str, "%d/%m/%Y")
print(data_parse)  # 2026-02-24 00:00:00

# Operações com datas:
amanha = hoje + timedelta(days=1)
print(amanha)  # 2026-02-25

ontem = hoje - timedelta(days=1)
print(ontem)  # 2026-02-23

# Operações com horários:
horario_futuro = agora + timedelta(hours=2)
print(horario_futuro)  # 2026-02-24 06:26:35.789012

# Operações com timedelta:
delta = timedelta(days=2, hours=3, minutes=30)
print(delta)  # 2 days, 3:30:00

# %A dia da semana
# %a dia da semana abreviado
# %B mês
# %b mês abreviado
# %Y ano com século
# %y ano sem século
# %I hora (12 horas)
# %H hora (24 horas)
# %M minuto
# %S segundo
# %p AM/PM
# %Z fuso horário
# %j dia do ano
# %U semana do ano (domingo como primeiro dia da semana)
# %W semana do ano (segunda-feira como primeiro dia da semana)
# %c data e hora local completa
# %x data local
# %X hora local
# %G ano ISO
# %u dia da semana ISO (1 = segunda-feira, 7 = domingo)
# %V semana do ano ISO
# %w dia da semana (0 = domingo, 6 = sábado)
# %z deslocamento do fuso horário em relação ao UTC
print(agora.strftime("%A, %d de %B de %Y %H:%M:%S %Z%z")) # Exemplo: terça-feira, 24 de fevereiro de 2026 04:26:35 UTC+0000
print(agora.strftime("%c")) # Exemplo: Tue Feb 24 04:26:35 2026
print(agora.strftime("%x")) # Exemplo: 02/24/26
print(agora.strftime("%X")) # Exemplo: 04:26:35
print(agora.strftime("%G")) # Exemplo: 2026
print(agora.strftime("%u")) # Exemplo: 2
print(agora.strftime("%V")) # Exemplo: 08
print(agora.strftime("%w")) # Exemplo: 2
print(agora.strftime("%z")) # Exemplo: +0000
print(agora.strftime("%Z")) # Exemplo: UTC
print(agora.strftime("%j")) # Exemplo: 55
print(agora.strftime("%s")) # Exemplo: 1708760795
print(agora.strftime("%f")) # Exemplo: 789012
print(agora.strftime("%p")) # Exemplo: AM
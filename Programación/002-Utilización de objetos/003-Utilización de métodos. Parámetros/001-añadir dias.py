import datetime

ahora = datetime.datetime.now()

masuno = ahora + datetime.timedelta(days=1)
print("Fecha actual:", ahora)
print("Fecha más uno:", masuno)
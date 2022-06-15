
""" Proyecto Sistema de citas médicas  en python + mysql
1.- Abrir asistente
2.- Login y registro
3.- si elegimos registro creara un usuario en la bd
4.- si elegimos login identificara al usario (en este caso el usuario es un doctor[a])
5.- crear, editar, mostrar eliminar las citas que se agendaran
 """

from usuarios import acciones

print("""
####### BIENVENIDO #######
Acciones desponibles
  -registro
  -login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?:")

if accion == "registro":
  hazEl.registro()

elif accion == "login":
  hazEl.login()

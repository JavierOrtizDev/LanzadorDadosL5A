from def_roll_dice import roll_dice
from def_control_error import error_control
d_ring = ["Vacío", "🌀", "☠️", "🌀☠️", "✅☠️", "🎯☠️"]
d_skill = ["Vacío", "Vacío", "🌀", "🌀 ", "☠️", "☠️ ", "🌀☠️", "✅ ", "✅ ", "🎯", "🎯", "🎯🌀"]

mensaje_ring ='Introduce el numero de dados de anillo que vas a lanzar: '
mensaje_skill = 'Introduce el numero de dados de habilidad que vas a lanzar: '

#control de errores 
num_ring = error_control(mensaje_ring)
num_skill = error_control(mensaje_skill)

#lanzar dados
print(roll_dice(d_ring, num_ring))
print(roll_dice(d_skill, num_skill))


print("Cantidad de dados de anillo guardados:", num_ring)
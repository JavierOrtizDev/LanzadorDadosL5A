import def_roll_dice
import def_control_error
d_ring = ["Vacío", "🌀", "☠️", "🌀☠️", "✅☠️", "🎯☠️"]
mensaje_ring ='Introduce el numero de dados de anillo que vas a lanzar: '

d_skill = ["Vacío", "Vacío", "🌀", "🌀 ", "☠️", "☠️ ", "🌀☠️", "✅ ", "✅ ", "🎯", "🎯", "🎯🌀"]
mensaje_skill = 'Introduce el numero de dados de habilidad que vas a lanzar: '

#control de errores 
num_ring = def_control_error.error_control(mensaje_ring)
num_skill = def_control_error.error_control(mensaje_skill)

#lanzar dados
def_roll_dice.roll_dice(d_ring, num_ring)
def_roll_dice.roll_dice(d_skill, num_skill)


print("Cantidad de dados de anillo guardados:", num_ring)
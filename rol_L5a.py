from def_roll_dice import roll_dice

from def_control_error import error_control

d_ring = ["Vacío", "🌀", "☠️", "🌀☠️", "✅☠️", "🎯☠️"]
d_skill = ["Vacío", "Vacío", "🌀", "🌀", "☠️", "☠️", "🌀☠️", "✅", "✅ ", "🎯", "🎯", "🎯🌀"]

mensaje_ring ='Introduce el numero de dados de anillo que vas a lanzar: '
mensaje_skill = 'Introduce el numero de dados de habilidad que vas a lanzar: '

#control de errores 
num_ring = error_control(mensaje_ring)


num_skill = error_control(mensaje_skill)

#lanzar dados
resultado_anillo = roll_dice(d_ring, num_ring)


resultado_habilidad = roll_dice(d_skill, num_skill)
def combinar():
    resultado_combinado = {}

# Procesamos el primer array (Anillos)
    for i, valor in enumerate(resultado_anillo):
     resultado_combinado [("anillo", i)] = [valor]

# Procesamos el segundo array (Habilidades)
    for i, valor in enumerate(resultado_habilidad):
     resultado_combinado [("habilidad", i)] = [valor]
    
    return resultado_combinado
resultado_combinado = combinar()
print(resultado_combinado)

print("Cantidad de dados de anillo guardados:", num_ring)
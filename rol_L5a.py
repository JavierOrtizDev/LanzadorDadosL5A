from def_roll_dice import roll_dice

from def_control_error import error_control

from def_dados_guardados import elegir_dados_guardados
import random

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


def combinar(resultado_anillo, resultado_habilidad):
    resultado_combinado = []

    for face in resultado_anillo:
     resultado_combinado.append({"type" : "Anillo","face": face})

    for face in resultado_habilidad:
     resultado_combinado.append({"type" : "Habilidad","face": face})
    
    return resultado_combinado


resultado_combinado = combinar(resultado_anillo, resultado_habilidad)
print("\nResultados de la Tirada:")
for i, dado in enumerate(resultado_combinado, start = 1):
  print(f"[{i}] ({dado['type']} {dado['face']})")

dados_guardados = elegir_dados_guardados(resultado_combinado, num_ring)

def dados_relanzados(dados_guardados, d_ring, d_skill):
    i = 0
    # Usamos while porque la lista crecerá si hay más éxitos
    while i < len(dados_guardados):
        dado_actual = dados_guardados[i]
        cara = dado_actual["face"]
        
        # Verificamos si el símbolo 🎯 está contenido en la cara
        if "🎯" in cara:
            # Seleccionamos el pool según el tipo
            pool = d_ring if dado_actual["type"] == "Anillo" else d_skill
            
            # Lanzamos el nuevo dado
            nueva_cara = random.choice(pool)
            nuevo_dado = {
                "type": dado_actual["type"], 
                "face": nueva_cara
            }
            
            # Lo añadimos al final de la lista para que sea procesado más adelante
            dados_guardados.append(nuevo_dado)
            
            # Opcional: imprimir el proceso para el jugador
            print(f"--> ¡Explosión en {dado_actual['type']}! ({cara}) -> Nuevo dado: {nueva_cara}")
        
        i += 1  
    
    return dados_guardados
                

dado_guadados_totales = dados_relanzados(dados_guardados, d_ring, d_skill)
print("\nDados que has guardado:", end=" ")
for dado in dado_guadados_totales:
  print(dado["face"]," ", end=" ")

print()

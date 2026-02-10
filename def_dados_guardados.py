def elegir_dados_guardados(dados, max_guardar):

    print(f"\nPuedes guardar hasta {max_guardar} dados.")
    print("Introduce los números de los dados separados por espacios (ej: 1 3 5)")
    print("O pulsa ENTER para no guardar ninguno.")

    while True:
        entrada = input("> ").strip()

        if entrada == "":
            return []

        try:
            indices = [int(x) for x in entrada.split()]

            if len(indices) > max_guardar:
                raise ValueError("Has seleccionado más dados de los permitidos.")

            if len(set(indices)) != len(indices):
                raise ValueError("No puedes repetir el mismo dado.")

            if any(i < 1 or i > len(dados) for i in indices):
                raise ValueError("Algún índice está fuera de rango.")

            dados_guardados = [dados[i - 1] for i in indices]

           
            return dados_guardados

        except ValueError as e:
            print(f"❌ Error: {e}")

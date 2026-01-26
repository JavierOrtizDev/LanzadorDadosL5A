def error_control( mensaje):
  while True:
    try:
      num = int(input(mensaje))
      if num > 0 and num < 10:
        return num
      raise ValueError
    except:
      print("❌ Error: introduce un numero entre 1 - 9")
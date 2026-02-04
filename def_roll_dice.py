import random
#lanza los dados de anillo
def roll_dice(dice, num_dice):
    result = []
    for i in  range(num_dice):
      face = random.choice(dice)
      result.append(face)
    return result
""" #lanza los dados extras
      while "🎯" in face:
        face = random.choice(dice)
        result.append(face) """
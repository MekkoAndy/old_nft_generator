import random


def mess_func(lori, name, rarity_list):
   head_layer_chance = random.randint(0, 9)
   head_layer_chance_bool = False if head_layer_chance == 0 else True

   glasses_layer_chance = random.randint(0, 99)
   glasses_layer_chance_bool = True if glasses_layer_chance in range(7) else False


   # eye picker for common
   lori[2] = random.choice([2, 6, 7, 8, 10, 12, 13, 16, 19, 20, 22, 24, 27, 28])

   # mouth picker for common
   lori[3] = random.choice([1, 5, 6, 7, 9, 12, 13, 15, 16, 18, 21, 22, 24, 25])

   # rare cases
   if rarity_list[name] == 1:
      # eye picker for rare
      lori[2] = random.choice([1, 3, 4, 5, 9, 11, 14, 15, 17, 18, 21, 23, 25, 26, 29, 30, 31])

      # mouth picker for rare
      lori[3] = random.choice([2, 3, 4, 8, 10, 11, 14, 17, 19, 20, 23, 26, 27, 28])
   
   # outfit chooser
   lori[4] = random.choice(range(4, 56))

   # legendary cases
   if rarity_list[name] == 2:
      lori[4] = random.choice([1, 2, 3])

   # glasses layer
   lori[5] = lori[5] if glasses_layer_chance_bool else 0

   # head layer
   lori[6] = lori[6] if head_layer_chance_bool else 0


   return lori

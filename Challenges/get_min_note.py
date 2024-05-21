def get_min_note(note_a, note_b, min = 3):
   calc = -((note_a * .35) + (note_b * .35) - min) / .3
   rounded = round(calc, 1)
   return  rounded if rounded > calc else round(calc + 0.1, 1)

data_mining = get_min_note(note_a=4, note_b=4)
interconectivity = get_min_note(note_a=2.6, note_b=4.3)
invertion_analisys = get_min_note(note_a=1.3, note_b=4.5)

print(data_mining)
print(interconectivity)
print(invertion_analisys)

# 1. Declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)
nums = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# 2. Afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
asc_nums = sorted(nums)
print(asc_nums)
print(nums)

# 3. Afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
desc_nums = sorted(nums, reverse=True)
print(desc_nums)
print(nums)

# 4. Afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(asc_nums[1::2])

# 5. Afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(asc_nums[::2])

# 6. Afișarea elementelor multipli ai lui 3
print([x for x in asc_nums if not x % 3])

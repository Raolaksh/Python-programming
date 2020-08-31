is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you neither male nor tall")

is_female = True
is_short = False

if is_female or is_short:
    print("you are a short female")
else:
    print("you are either not female or not short or both")

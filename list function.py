lucky_numbers = [4, 8, 15, 16, 23, 42]
naruto_characters = ["naruto","sasuke","sasuke","sakura","itachi","kakashi"]
naruto_characters.extend(lucky_numbers)
naruto_characters.append("baruto")
print(naruto_characters)
naruto_characters.insert(1,"sarada")
print(naruto_characters)
naruto_characters.remove("sarada")
print(naruto_characters)
naruto_characters.pop()
print(naruto_characters)
print(naruto_characters.index("itachi"))
print(naruto_characters.count("sasuke"))


NAMES_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Beige": "#f5f5dc", "Black": "#000000",
                "Blue": "#0000ff", "Coral": "#ff7f50", "Green": "#006400", "Purple": "#68228b", "Red": "#8b1a1a"}


name = input("what colour do you want? ")

while name != "":
    if name in NAMES_TO_HEX:
        print(name, 'is', NAMES_TO_HEX[name])
    else:
        print('no')
    name = input("what colour do you want? ")

# Why doesnt this work
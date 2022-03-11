from PIL import Image

img = Image.open('C:/Users/CadeWeiskopf/Desktop/smiley.png', 'r')
img = img.resize((50, 50))
pixels = list(img.getdata())

height = img.height
width = img.width
brightnessCharacters = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
brightnessCharactersBackwards = ''
j = len(brightnessCharacters) - 1
while j >= 0:
    brightnessCharactersBackwards += brightnessCharacters[j]
    j -= 1

#brightnessCharacters = brightnessCharactersBackwards

print('height=' + str(height) + ' width=' + str(width))
print('length of pixels=' + str(len(pixels)))
widthIndex = 1
asciiText = '\n'
for i in range(0, len(pixels)):
    avg = pixels[i][0] + pixels[i][1] + pixels[i][2]
    avg /= 3
    if avg != 0:
        brightnessIndex = 255 / int(avg)
        brightnessIndex = len(brightnessCharacters) / brightnessIndex
        brightnessIndex -= 1
    else:
        brightnessIndex = 0
    asciiText += brightnessCharacters[int(brightnessIndex)]
    if widthIndex == width:
        asciiText += '\n'
        widthIndex = 1
    else:
        widthIndex += 1

print(asciiText)

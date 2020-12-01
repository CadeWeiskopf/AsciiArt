
import numpy;
import cv2;

image = cv2.imread("C:/Users/weisk/Downloads/smiley.jpg")

# pixels is array of [r,g,b] 
pixels = numpy.asarray(image)

brightness = []

for x in pixels:
    for y in x:
        pixel = y
        # use average for brightness
        bright = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3
        brightness.append(bright)


bChars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
output = ""
for b in brightness:
    if b != 0:
        scalar = 255 / b;
        index = len(bChars) / scalar
        index -= 1
    else:
        scalar = 0
        index = 0
    bChar = bChars[int(index)]
    output += bChar
    #print(bChar)

print(output)
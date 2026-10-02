from PIL import Image

matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

mask = mask.resize(matrix.size)
mask.putalpha(100)

matrix.paste(mask, (0, 0), mask)
matrix.show()
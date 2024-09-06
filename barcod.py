import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display
barcode_format = barcode.get_barcode_class('ean13')
barcode_number = '0001-05'
barcode_image = barcode_format(barcode_number, writer=ImageWriter())
barcode_filname = 'barcode_image'
barcode_image.save(barcode_filname)
display(Image(filename=f'{barcode_filname}.png'))
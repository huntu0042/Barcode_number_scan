from PIL import Image
from pyzbar.pyzbar import decode


def scan_barcode(img_name):
	decdata = decode(Image.open(img_name))
	barcode_num = decdata[0].data
	print(decdata[0].data)
	return barcode_num

def scan_many_barcode(img_list):
	num_list = []
	for img_name in img_list:
		decdata = decode(Image.open(img_name))
		barcode_num = decdata[0].data
		print(barcode_num)

		num_list.append(barcode_num)
	return num_list


img_name = "3.png"
scan_barcode(img_name)
talents = int(input('nhap tanlents:'))
pounds  = int(input('nhap pounds:'))
lots    = float(input('nhap lots:'))

tổng_lots = talents * 20 * 32 + pounds * 32 + lots
tổng_grams = tổng_lots * 13.3 
kilograms = int(tổng_grams / 1000)
grams = tổng_grams % 1000

print('Granms:' , grams )
print('Kilograms:' , kilograms )
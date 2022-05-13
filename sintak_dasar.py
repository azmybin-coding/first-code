"""
All basic syntac programming language :
1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah malompat jika kondisi terpenuhi
3. Pengulangan: Langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

#Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu karung beras, dan jika ada beli telor 6 butir"')
print('Maka budi pergi ke toko')
print('dan Budi mulai berbelanja')

#Percabangan
milk_bottle_count = 180
egg_count = 1555
print(f"Milk bottle count {milk_bottle_count} btl")
print(f"Egg count {egg_count} btr")

if milk_bottle_count > 20:
    print("Budi melihat harganya, dan ternyata uangnya cukup")
    if egg_count == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu")
        print("Budi membeli 6 butir telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada Ibu")

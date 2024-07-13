meme_dict = {
    "key": "value",
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "ROFL": "Tanggapan terhadap lelucon",
    "SHEESH": "Sedikit ketidaksetujuan",
    "CREEP": "Menakutkan, tidak menyenangkan",
    "AGGRO": "Untuk menjadi agresif/marah",   
}

for i in range(len(meme_dict)):
    meme = input('masukkan key:')
    print(meme_dict[meme])

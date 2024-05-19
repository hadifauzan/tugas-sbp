# Definisikan kode menu, kategori, dan aturan sebagai array atau dictionary
penyakit_codes = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
gejala_codes = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14", "G15", "G15", "G16", "G17", "G18", "G19", "G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27"]

# Aturan direpresentasikan dalam format yang sama seperti sebelumnya, dengan tambahan data pakar
rules = {
    "P1" : ["G1", "G2", "G3", "G4", "G5", "G6", "G15"], 
    "P2" : ["G2", "G7", "G8", "G9"], 
    "P3" : ["G10", "G11", "G12"], 
    "P4" : ["G2", "G3", "G13", "G14", "G18"], 
    "P5" : ["G2", "G4", "G18", "G22"], 
    "P6" : ["G10", "G11", "G20", "G26", "G22"], 
    "P7" : ["G11", "G21", "G24", "G26"], 
    "P8" : ["G2", "G8", "G20", "G27"], 
}

# Definisi Term CF
term_cf = {
    "Tidak": 0,
    "Mungkin": 0.4,
    "Kemungkinan Besar": 0.6,
    "Hampir Pasti": 0.8,
    "Pasti": 1
}


# Definisikan kategori dan nilai MB-nya sebagai dictionary
user_input = {
    "G1": ["Mulut terasa gatal", "Mungkin", 0.4],
    "G2": ["Kulit terasa gatal", "Kemungkinan Besar", 0.6],
    "G3": ["Ada pembengkakan di bibir", "Tidak", 0],
    "G4": ["Pusing", "Hampir Pasti", 0.8],
    "G5": ["Mual", "Tidak", 0],
    "G6": ["Muntah", "Tidak", 0],
    "G7": ["Ada pembengkakan di Kulit", "Tidak", 0],
    "G8": ["Kulit memerah", "Tidak", 0],
    "G9": ["Muncul ruam di kulit", "Mungkin", 0.4],
    "G10": ["Bersin yang berulang", "Kemungkinan Besar", 0.6],
    "G11": ["Hidung berair", "Hampir Pasti", 0.8],
    "G12": ["Hidung, Langit-langit mulut, atau tenggorokan terasa gatal", "Hampir Pasti", 0.4],
    "G13": ["Telah meminum antibiotik", "Pasti", 1],
    "G14": ["Telah meminum obat tertentu", "Kemungkinan Besar", 0.6],
    "G15": ["Telah mengonsumsi produk yang mengandung susu/telur", "Mungkin", 0.4],
    "G16": ["Pembengkakan ringan di sekitar gigitan", "Tidak", 0],
    "G17": ["Pingsan", "Tidak", 0],
    "G18": ["Sakit perut", "Mungkin", 0.4],
    "G19": ["Demam", "Kemungkinan Besar", 0.6],
    "G20": ["Gatal pada hidung, mata dan atau tenggorokan", "Tidak", 0],
    "G21": ["Telah memakan jamur makanan", "Tidak", 0],
    "G22": ["Sesak napas", "Kemungkinan Besar", 0.6],
    "G23": ["Mata berair dan merah", "Kemungkinan Besar", 0.6],
    "G24": ["Pembekakan di sekitar mata", "Tidak", 0],
    "G25": ["Pembekakan di wajah", "Tidak", 0],
    "G26": ["Hidung tersumbat", "Tidak", 0],
    "G27": ["Telah beraktivitas di tempat yang memiliki rumput", "Tidak", 0]
}

# Input pakar berupa dictionary dengan kode menu sebagai kunci dan kategori serta nilai MD sebagai nilai
pakar_input = {
    "P1": [("G1", "Mulut terasa gatal", 0.3), ("G2", "Kulit terasa gatal", 0.6), ("G3", "Ada pembengkakan di bibir", 0.4), ("G4", "Pusing", 0.4), ("G5", "Mual", 0.6), ("G6", "Muntah", 0.1), ("G15", "Telah mengonsumsi produk yang mengandung susu/telur", 0)],
    "P2": [("G2", "Kulit terasa gatal", 0.4), ("G7", "Ada pembengkakan di kulit", 0.3), ("G8", "Kulit memerah", 0.5), ("G9", "Muncul ruam di kulit", 0.3)],
    "P3": [("G10", "Bersin yang berulang", 0.4), ("G11", "Hidung berair", 0.4), ("G12", "Hidung, Langit-langit mulut, atau tenggorokan terasa gatal", 0)],
    "P4": [("G2", "Kulit terasa gatal", 0), ("G3", "Ada pembengkakan di bibir", 0.4), ("G13", "Telah meminum antibiotik", 0.6), ("G14", "Telah meminum obat tertentu", 0.4), ("G18", "Sakit perut", 0.4)],
    "P5": [("G2", "Kulit terasa gatal", 0.2), ("G4", "Pusing", 0.8), ("G18", "Sakit perut", 0.4), ("G22", "Sesak napas", 0.6)],
    "P6": [("G10", "Bersin yang berulang", 0.7), ("G11", "Hidung berair", 0.8), ("G20", "Gatal pada hidung, mata dan atau tenggorokan", 0.1), ("G26", "Hidung tersumbat", 0.1), ("G22", "Sesak napas", 0.2)],
    "P7": [("G11", "Hidung berair", 0.4), ("G23", "Mata berair dan merah", 0.5), ("G24", "Pembengkakan di sekitar mata", 0.6), ("G26", "Hidung tersumbat", 0.7)],
    "P8": [("G2", "Kulit terasa gatal", 0.3), ("G8", "Kulit memerah", 0.2), ("G20", "Gatal pada hidung, mata dan atau tenggorokan", 0.5), ("G27", "Telah beraktivitas di tempat yang memiliki rumput", 0.4)]
}


# Input pakar berupa dictionary dengan kode menu sebagai kunci dan kategori serta nilai MD sebagai nilai
hitung_cf = {
    "P1": [
        ("G1", "Mulut terasa gatal", 0.4, 0.3),
        ("G2", "Kulit terasa gatal", 0.6, 0.6),
        ("G3", "Ada pembengkakan di bibir", 0, 0.4),
        ("G4", "Pusing", 0.8, 0.4),
        ("G5", "Mual", 0, 0.6),
        ("G6", "Muntah", 0, 0.1),
        ("G15", "Telah mengonsumsi produk yang mengandung susu/telur", 0.4, 0)
    ],
    "P2": [
        ("G2", "Kulit terasa gatal", 0.6, 0.4),
        ("G7", "Ada pembengkakan di kulit", 0, 0.3),
        ("G8", "Kulit memerah", 0, 0.5),
        ("G9", "Muncul ruam di kulit", 0.4, 0.3)
    ],
    "P3": [
        ("G10", "Bersin yang berulang", 0.6, 0.4),
        ("G11", "Hidung berair", 0.8, 0.4),
        ("G12", "Hidung, Langit-langit mulut, atau tenggorokan terasa gatal", 0.4, 0)
    ],
    "P4": [
        ("G2", "Kulit terasa gatal", 0.6, 0),
        ("G3", "Ada pembengkakan di bibir", 0, 0.4),
        ("G13", "Telah meminum antibiotik", 1, 0.6),
        ("G14", "Telah meminum obat tertentu", 0.6, 0.4),
        ("G18", "Sakit perut", 0.4, 0.4)
    ],
    "P5": [
        ("G2", "Kulit terasa gatal", 0.6, 0.2),
        ("G4", "Pusing", 0.8, 0.8),
        ("G18", "Sakit perut", 0.4, 0.4),
        ("G22", "Sesak napas", 0.6, 0.6)
    ],
    "P6": [
        ("G10", "Bersin yang berulang", 0.6, 0.7),
        ("G11", "Hidung berair", 0.8, 0.8),
        ("G20", "Gatal pada hidung, mata dan atau tenggorokan", 0, 0.1),
        ("G26", "Hidung tersumbat", 0, 0.1),
        ("G22", "Sesak napas", 0.6, 0.2)
    ],
    "P7": [
        ("G11", "Hidung berair", 0.8, 0.4),
        ("G23", "Mata berair dan merah", 0.6, 0.5),
        ("G24", "Pembengkakan di sekitar mata", 0, 0.6),
        ("G26", "Hidung tersumbat", 0, 0.7)
    ],
    "P8": [
        ("G2", "Kulit terasa gatal", 0.6, 0.3),
        ("G8", "Kulit memerah", 0, 0.2),
        ("G20", "Gatal pada hidung, mata dan atau tenggorokan", 0, 0.5),
        ("G27", "Telah beraktivitas di tempat yang memiliki rumput", 0, 0.4)
    ]
}


def calculate_combination_cf(penyakit):
    cf_combination = 1
    for gejala in user_input.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combination *= data[2] * data[3]
                break
    return cf_combination

def calculate_aggregated_cf(penyakit):
    cf_combinations = []
    for gejala in user_input.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combinations.append(data[2] * data[3])
                break

    cf_aggregated = cf_combinations[0]
    for cf in cf_combinations[1:]:
        cf_aggregated = cf_aggregated + cf - (cf_aggregated * cf)

    return cf_aggregated

def calculate_percentage(cf_combination, cf_aggregated):
    return cf_aggregated * 100

def calculate_cf(penyakit):
    cf_combination = calculate_combination_cf(penyakit)
    cf_aggregated = calculate_aggregated_cf(penyakit)
    percentage = calculate_percentage(cf_combination, cf_aggregated)
    
    return percentage

print("\nCertainty Factor Gabungan:")
print("Kode Penyakit   |       CF Gabungan")
print("-----------------------------------")
for penyakit in rules.keys():
    i = penyakit_codes.index(penyakit)
    cf_percentage = calculate_cf(penyakit)
    print(f"{penyakit}\t\t|\t{cf_percentage:.2f}%")

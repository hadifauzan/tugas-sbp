import numpy as np

# Data input dari user dan pakar
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

# Step 1: Calculate the average value for each gejala from user input
gejala_values = {gejala: user_input[gejala][2] for gejala in user_input}
average_gejala = np.mean(list(gejala_values.values()))

# Step 2: Calculate PDA and NDA for each penyakit based on input pakar and user
def calculate_pda_nda(penyakit, user_input, pakar_input, average_gejala):
    pda, nda = 0, 0
    for gejala, _, pakar_value in pakar_input[penyakit]:
        user_value = user_input.get(gejala, [None, None, 0])[2]
        pda += max(0, user_value - average_gejala)
        nda += max(0, average_gejala - user_value)
    return pda, nda

pda_nda_values = {penyakit: calculate_pda_nda(penyakit, user_input, pakar_input, average_gejala) for penyakit in pakar_input}

# Step 3: Calculate the EDAS score for each penyakit
def calculate_edas_score(pda, nda):
    return pda - nda

edas_scores = {penyakit: calculate_edas_score(*values) for penyakit, values in pda_nda_values.items()}

# Display EDAS scores
print("\nEDAS Scores:")
print("Kode Penyakit   |   EDAS Score")
print("-------------------------------")
for penyakit, score in edas_scores.items():
    print(f"{penyakit}\t\t|\t{score:.2f}")


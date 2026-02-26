import matplotlib.pyplot as plt

x = [
    # ===== JOHAN =====
    1, 2, 2, 1.5, 1, None,                 # J
    3, 4, 4, 3, 3, None,                   # O 
    5, 5, None, 6, 6, None, 5, 6, None,    # H
    7, 7.5, 8, None, 7.2, 7.8, None,       # A
    9, 9, None, 9, 10, None, 10, 10, None, # N

   # ===== CRISTIAN =====
    1, 2, 1, 1, 2, None,                   # C
    3, 3, 4, 4, 3, 4, None,                # R
    5, 6, None, 5.5, 5.5, None, 5, 6, None,# I
    7, 8, 7, 7, 8, 8, 7, None,             # S
    9, 10, None, 9.5, 9.5, None,           # T
    10.2, 10.5, 10.3, 10.3, 10.2, 10.5, None, #I
    11, 11.5, 12, None, 11.2, 11.8, None,  # A
    13, 13, None, 13, 14, None, 14, 14, None,    # N

    # ===== CAMILO =====
    1, 2, 1, 1, 2, None,                   # C
    3, 3.5, 4, None, 3.2, 3.8, None,       # A
    5, 5, 5.5, 5.5, 5.5, 6, 6, None,       # M
    7, 8, None, 7.5, 7.5, None, 7, 8, None,# I
    9, 9, None, 9, 10, None,               # L
    11, 12, 12, 11, 11, None,              # O

    # ===== EDISSON =====
    1, 2, None, 1, 2, None, 1, 2, None, 1, 1, None, # E
    3, 4, 3, 3, None,                      # D
    5, 6, None, 5.5, 5.5, None, 5, 6, None,# I
    8, 7, 7, 8, 8, 7, None,                # S
    10, 9, 9, 10, 10, 9, None,             # S
    11, 12, 12, 11, 11, None,              # O
    13, 13, None, 13, 14, None, 14, 14     # N
]

y = [
    # ===== JOHAN =====
    4, 4, 1.5, 1, 1.5, None,               # J
    1, 1, 4, 4, 1, None,                   # O
    1, 4, None, 1, 4, None, 2.5, 2.5, None,# H
    1, 4, 1, None, 2.5, 2.5, None,         # A
    1, 4, None, 4, 1, None, 1, 4, None,          # N
    
   # ===== CRISTIAN =====
    -1, -1, -1, -4, -4, None,                 # C
    -4, -1, -1, -2, -2, -4, None,             # R
    -1, -1, None, -1, -4, None, -4, -4, None, # I
    -1, -1, -1, -2.5, -2.5, -4, -4, None,     # S
    -1, -1, None, -1, -4, None,               # T
    -1, -1, -1, -4, -4, -4, None,             # I
    -4, -1, -4, None, -2.5, -2.5, None,       # A
    -4, -1, None, -1, -4, None, -4, -1, None,       # N

    # ===== CAMILO =====
    -6, -6, -6, -9, -9, None,              # C
    -9, -6, -9, None, -7.5, -7.5, None,    # A
    -9, -6, -6, -9, -6, -6, -9, None,      # M
    -6, -6, None, -6, -9, None, -9, -9, None, # I
    -6, -9, None, -9, -9, None,            # L
    -9, -9, -6, -6, -9, None,                # O

    # ===== EDISSON =====
    -11, -11, None, -13, -13, None, -15, -15, None, -11, -15, None, # E
    -15, -13, -11, -15, None,                       # D
    -11, -11, None, -11, -15, None, -15, -15, None, # I
    -11, -11, -13, -13, -15, -15, None,             # S
    -11, -11, -13, -13, -15, -15, None,             # S
    -15, -15, -11, -11, -15, None,                  # O
    -15, -11, None, -11, -15, None, -15, -11        # N
]

plt.plot(x, y)
plt.title("NOMBRES")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.gca().set_aspect('equal')
plt.grid()
plt.show()
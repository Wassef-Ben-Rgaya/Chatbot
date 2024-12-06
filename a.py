import numpy as np

# Matrice I
I = np.array([[0, 1, 3, 4],
              [5, 4, 0, 7],
              [7, 3, 8, 7],
              [3, 8, 0, 1],
              [2, 1, 0, 5]])

# Palette de couleurs t
t = np.array([[0, 0, 0],
              [0, 0, 1],
              [0, 1, 1],
              [0, 1, 0],
              [1, 1, 0],
              [1, 0, 0],
              [1, 0, 1],
              [0, 0, 0],
              [1, 1, 1]])

# Diviser la palette de couleurs en trois matrices de couleurs
R = t[:, 0]
G = t[:, 1]
B = t[:, 2]

# Créer les matrices de couleurs pour chaque pixel dans la matrice I
nrows, ncols = I.shape
image_r = np.zeros((nrows, ncols), dtype=np.uint8)
image_g = np.zeros((nrows, ncols), dtype=np.uint8)
image_b = np.zeros((nrows, ncols), dtype=np.uint8)

for i in range(nrows):
    for j in range(ncols):
        index = np.argmin(np.linalg.norm(t - np.array([I[i,j], I[i,j], I[i,j]]), axis=1))
        image_r[i,j] = R[index]
        image_g[i,j] = G[index]
        image_b[i,j] = B[index]
print(R)
print(G)
print(B)
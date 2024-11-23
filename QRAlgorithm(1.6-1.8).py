import numpy as np

def QRAlgorithm(A, maxK = 5):
    for _ in range(maxK):
        Q, R = np.linalg.qr(A)
        A = R @ Q

    return np.diag(A).round(2)

matrices = [
    np.array([[2, 3], [2, 1]]),
    np.array([[1, 1], [2, 1]]),
    np.array([[1, 0, -1], [1, 2, 1], [-4, 0, 1]]),
    np.array([[1, 1, -1], [0, 2, 0], [-2, 4, 2]])
]

for i, A in enumerate(matrices, start=1):
    print(f"Original matrix A{i}:\n{A}\n")
    eigenvalues = ", ".join(map(str, QRAlgorithm(A)))
    print(f"Eigenvalues of A{i} from QR:\n{eigenvalues}\n")

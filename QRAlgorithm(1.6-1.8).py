import numpy as np

def QRAlgorithm(A):
    maxK = 10
    for _ in range(maxK):
        Q, R = np.linalg.qr(A)
        A = R @ Q
    return np.diag(A).round(2)
#1.6
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

#1.7
A5 = np.array([[2,3],[-1,-2]])
print(f"Original matrix A5:\n{A5}\n")
eigenvalues = ", ".join(map(str, QRAlgorithm(A5)))
print(f"Eigenvalues of A5 from QR:\n{eigenvalues}\n")

#1.8
B = A5 + 0.9*np.identity(2)
print(f"Original matrix B:\n{B}\n")
eigenvalues = ", ".join(map(str, (QRAlgorithm(B))))
print(f"Eigenvalues of B from QR:\n{eigenvalues}\n")
eigenvalues = ", ".join(map(str, (QRAlgorithm(B) - 0.9).round(2)))
print(f"Eigenvalues of A5 from QR shifted:\n{eigenvalues}\n")
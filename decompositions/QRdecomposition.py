import numpy as np


def projection(u, a):
    factor = np.dot(u, a) / np.dot(u, u)
    return factor * u


def normalization(u):
    return u / np.linalg.norm(u, ord=2)


def gram_schmidt_algorith(A):
    Q = np.zeros_like(A, np.float_)
    R = np.zeros_like(A, np.float_)
    n = A.shape[1]
    for k in range(n):
        a_k = A[:, k]
        u = a_k - np.sum(np.array([projection(Q[:, i], a_k) for i in range(k)]), axis=0)
        Q[:, k] = normalization(u)
        R[k] = np.dot(Q[:, k], A)
    return Q, R


def standardBasisVector(length, index):
    standardVector = np.zeros(length, np.float_)
    standardVector[index] = 1
    return standardVector


def householdReflection(A):
    n = A.shape[0]
    m = A.shape[1]
    R0 = A.astype(np.float_).copy()
    Q0 = np.eye(A.shape[0])
    for k in range(min(A.shape[1] - 1, A.shape[0])):
        a_k = R0[k:, k].copy()
        a_k[:k] = 0
        sign = 1 if R0[k, k] >= 0 else -1
        u_k = a_k - sign * np.linalg.norm(a_k) * standardBasisVector(n - k, 0)
        v_k = normalization(u_k)
        H_k = np.eye(n - k) - 2 * np.einsum('i,j->ij', v_k, v_k.T)
        R_k = np.einsum('ik,kj->ij', H_k, R0[k:, k:])
        R0[k:, k:] = R_k
        tmpH = np.eye(n)
        tmpH[k:, k:] = H_k
        Q_k = np.einsum('ik,kj->ij', Q0, tmpH)
        Q0 = Q_k
    return Q0[:, :m], R0[:m]




# simple example of image compression using the SVD
# note: creates reconstructed compressed images;
# does not actually store the compressed data (see inline notes)

import imageio  # no image reading in scipy!
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg


def compress_example(fname, rank):
    """ quick svd compression of a file fname (must be png, RGB)
        with a rank r approximation.

        Note that this doesn't actually compress, since it doesn't
        store the compressed form [just outputs the reconstructed image]
    """
    # m x n x 4 array; img_matrix[m,n,0:3] -> (R,G,B) for that pixel
    img_matrix = imageio.imread(fname, format='.png')
    max_rank = min(img_matrix.shape[0:2])
    if rank >= max_rank:
        print("Selected rank > image dim!")
        rank = max_rank

    compressed = np.zeros(img_matrix.shape)
    if img_matrix.shape[2] == 4:  # if there is a transparency layer
        compressed[:, :, 3] = img_matrix[:, :, 3]  # keep transparency

    sigmas = np.zeros((max_rank, 3))  # for display later
    for col in range(3):
        U, S, Vt = linalg.svd(img_matrix[:, :, col])  # Vt is V^T
        sigmas[:, col] = S

        # by summing rank 1 terms
        # for k in range(rank):
        #    compressed[:, :, col] += S[k]*np.outer(U[:, k], Vh[k, :])

        # or using the thin SVD and some numpy matrix operations
        compressed[:, :, col] = np.matmul(U[:, :rank]*S[:rank], Vt[:rank, :])
        # (if compressing, you'd store the thin U/S/V in the line above)

    # png format usees *unsigned* 8 bit integers,
    # so round to closest value in [0, 255]
    compressed[compressed < 0] = 0
    compressed[compressed > 255] = 255
    fn = fname.split('.')[0]
    imageio.imwrite(f'{fn}_r{rank}.png',
                    compressed.astype(np.uint8), format='.png')

    return sigmas, max_rank


if __name__ == "__main__":
    fname = 'cat.png'
    ranks = [4, 10, 20, 40, 100, 200, 10000]
    input(f'creating {len(ranks)} images... proceed?')
    for rank in ranks:
        sigmas, max_rank = compress_example(fname, rank)

    # plot of sigma vector (max over RGB)
    plt.figure(figsize=(4, 3))
    plt.semilogy(range(max_rank), np.max(sigmas, 1), '-k')
    plt.xlabel('$k$')
    plt.ylabel('$\\sigma$')
    plt.title('singular values: (max(R,G,B))')
    plt.savefig('singular.pdf', bbox_inches='tight')
    plt.show()

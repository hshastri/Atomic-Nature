import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    seq = sys.argv[4:]
    test = []
    for i in range(1, len(seq)):
        pic = Picture(seq[i - 1])
        bf = BlobFinder(pic, tau)
        beads = bf.getBeads(P)
        pic = Picture(seq[i])
        bf = BlobFinder(pic, tau)
        beads2 = bf.getBeads(P)
        for q in beads2:
            for a in beads:
                test += [q.distanceTo(a)]
            if min(test) <= delta:
                stdio.writef('%.4f\n', min(test))
            test = []

if __name__ == '__main__':
    main()

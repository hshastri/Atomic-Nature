import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    disp = stdio.readAllFloats()
    D = self_diffusion(disp)
    K = boltzmann(D)
    AVOGADRO = avagadro(K)
    stdio.writef('Boltzman = %e\n', K)
    stdio.writef('Avogadro = %e\n', AVOGADRO)


def self_diffusion(disp):
    n = len(disp)
    PIX_METER = 0.175 * math.pow(10, -6)
    num = 0
    for v in disp:
        v *= PIX_METER
        num += (v * v)
    return num / (2 * n)


def boltzmann(D):
    T = 297
    ETA = 9.135 * math.pow(10, -4)
    RHO = 0.5 * math.pow(10, -6)
    return (D * (6 * math.pi * ETA * RHO)) / T


def avagadro(K):
    R = 8.31457
    return R / K


if __name__ == '__main__':
    main()

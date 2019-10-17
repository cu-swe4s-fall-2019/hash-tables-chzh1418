import sys
import os
import matplotlib.pyplot as plt
import argparse
import matplotlib
matplotlib.use('Agg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='scatter plot',
                                     prog='scatter')

    parser.add_argument('--out_file', type=str, help='Filename',
                        required=True)
    parser.add_argument('--x_label', type=str, help='x-axis label',
                        required=True)
    parser.add_argument('--y_label', type=str, help='y-axis label',
                        required=True)

    args = parser.parse_args()

    X = []
    Y = []
    i = 0
    for line in sys.stdin:
        A = line.rstrip().split()
        if len(A) >= 2:
            try:
                X.append(float(A[0]))
                Y.append(float(A[1]))
            except ValueError:
                print('Invalid integer')
                continue
        elif len(A) == 1:
            try:
                X.append(float(i))
                Y.append(float(A[0]))
                i += 1
            except ValueError:
                print('Invalid integer')
                continue
        else:
            print('Empty file')
            sys.exit(1)

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(args.x_label)
    ax.set_ylabel(args.y_label)

    plt.savefig(args.out_file, bbox_inches='tight')

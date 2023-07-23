import argparse
from fetcher import fetch

def main():
    parser = argparse.ArgumentParser(
        description="Simple and minimalistic fetching software, requires python 3 and nerdfonts"
    )
    parser.add_argument('-w', '--width', type=int, default=50)
    parser.add_argument('-nf', '--noframe', action='store_true')

    args = parser.parse_args()
    fetch(int(args.width), args.noframe)

if __name__ == "__main__":
    main()

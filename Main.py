import sys

if __name__ == "__main__":
    if len(sys.argv) != 6:
        sys.exit(" Podano bledna ilosc argumentow!")

    algorithm = sys.argv[1]
    param = sys.argv[2]
    source = sys.argv[3]
    output = sys.argv[4]
    stats = sys.argv[5]

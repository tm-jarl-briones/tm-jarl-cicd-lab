import argparse


def main(args):
    print(f"num_a: {args.num_a}")
    print(f"num_b: {args.num_b}")
    print(f"sum: {args.num_a + args.num_b}")


def parse_arguments():
    
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--num_a', required=True, type=float)
    parser.add_argument('--num_b', required=True, type=float)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
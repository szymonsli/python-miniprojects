import sys

hanoi = {
  "A": [],
  "B": [],
  "C": [],
}


def build_tower(n, src, via, dest):
  if n > 0:
    # build tower on via
    build_tower(n - 1, src, dest, via)

    # move the last piece from src to dest
    popped = hanoi[src].pop(0)
    hanoi[dest].insert(0, popped)
    print(f'Moved plate {popped} from {src} to {dest}')
    print(hanoi)

    # build tower on dest
    build_tower(n - 1, via, src, dest)


def main():
  arg = ""
  try:
    arg = sys.argv[1]
    arg = int(arg)
    if arg < 1:
      raise Exception()
    hanoi["A"] = list(range(1, arg + 1))
  except:
    print("Arg should be an integer greater than 0")
  build_tower(arg, "A", "B", "C")


if __name__ == "__main__":
  main()

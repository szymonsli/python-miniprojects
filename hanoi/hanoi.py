import sys

hanoi = {
  "A": [],
  "B": [],
  "C": [],
}
steps = 0


def build_tower(n, src, via, dest):
  global steps
  if n > 0:
    # build tower on via
    build_tower(n - 1, src, dest, via)

    # move the last disk from src to dest
    steps += 1
    popped = hanoi[src].pop(0)
    hanoi[dest].insert(0, popped)
    print(f'{steps}. Moved disk {popped} from {src} to {dest}')
    print(hanoi)

    # build tower on dest
    build_tower(n - 1, via, src, dest)


def main():
  disks = 0
  try:
    disks = sys.argv[1]
    disks = int(disks)
    if disks < 1:
      raise Exception()
    hanoi["A"] = list(range(1, disks + 1))
  except:
    print("Arg should be an integer greater than 0")
  build_tower(disks, "A", "B", "C")


if __name__ == "__main__":
  main()

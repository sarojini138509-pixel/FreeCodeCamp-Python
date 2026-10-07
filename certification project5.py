def hanoi_solver(n):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []

    result = []

    def record():
        result.append(f"{rod1} {rod2} {rod3}")

    def move(disks, source, target, auxiliary):
        if disks == 0:
            return

        move(disks - 1, source, auxiliary, target)

        disk = source.pop()
        target.append(disk)
        record()

        move(disks - 1, auxiliary, target, source)

    record()
    move(n, rod1, rod3, rod2)

    return "\n".join(result)

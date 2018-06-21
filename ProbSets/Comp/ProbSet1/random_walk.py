from random import choice
def random_walk(max_iters=1e12):
    walk = 0
    directions = [1, -1]
    for i in range(int(max_iters)):
        try:
             walk += choice(directions)
        except KeyboardInterrupt as e:
            print("\nProcess interrupted at iteration ", i)
            break
    else:
        print("Process completed")
    return walk

print(random_walk(5000))

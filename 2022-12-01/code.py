currentGnome = 0
with open('input.txt') as f:
    lines = f.readlines()
    gnomes = [0] * len(lines)
    for line in lines:
        if line == "\n":
            currentGnome = currentGnome + 1
        else:
            gnomes[currentGnome] = gnomes[currentGnome] + int(line)
    gnomes.sort(reverse=True)
    print(gnomes[0])
    print(sum(gnomes[:3]))
f.close()

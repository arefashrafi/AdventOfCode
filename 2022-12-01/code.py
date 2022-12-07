currentGnome = 0
lines = open('input').readlines()
gnomes = [0] * len(lines)
for line in lines:
    if line == "\n":
        currentGnome += 1
    else:
        gnomes[currentGnome] += int(line)
gnomes.sort(reverse=True)
print(gnomes[0])
print(sum(gnomes[:3]))

# Get data from _SB_.GIO0.CIPR
#
# Package (0x03)
# {
#     0x94, 
#     0x2B, 
#     0x0355
# }, 
#
# ->
#
# 0x94 0x2B 0x0355

import sys

a = []

if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} <path>")
	sys.exit(1)

with open(sys.argv[1]) as f:
	for line in f:
		a.append(line[:-2].split())

for i in range(len(a)):
	a[i][0] = int(a[i][0], 16) # TLMM GPIO idx
	a[i][1] = int(a[i][1], 16) # HWIRQ
	a[i][2] = int(a[i][2], 16) # some sort of mask? feature?

a = sorted(a, key = lambda x: x[1])

for line in a:
	print(f"{{ {line[1]}, {line[0]} }},\t{hex(line[2])}")

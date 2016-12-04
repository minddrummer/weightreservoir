from weightreservoir import reservoir

def main():
	uniform = reservoir.UniformSampling(size = 10)
	for i in xrange(1000):
		uniform.addOne(i)
	uniform.addAll([i for i in xrange(1000)])    
	print uniform.get()

	wsam = reservoir.WeightSampling(size = 10)
	for i in xrange(1000):
		wsam.addOne(i, i)
	wsam.addAll([i for i in range(1000)], [j for j in range(999,-1,-1)])
	print wsam.get()

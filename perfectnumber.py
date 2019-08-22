import multiprocessing
import time

def perfect_number(n):
	sum = 0
	for i in range(1, n):
		if(n % i == 0):
			sum += i

	return sum == n;

def loop(first, last):
	start_time = time.time()

	for i in range(first, last):
		if perfect_number(i):
			print(str(i))

	end_time = time.time()
	# print('Execution time = ' + str(end_time - start_time))

def main():
	first = 1
	last = 25001
	jobs = []
	for i in range(0, 4):
		process = multiprocessing.Process(target=loop, args=(first, last))

		first += 25000
		last += 25000

		jobs.append(process)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()

	print('end')

main()
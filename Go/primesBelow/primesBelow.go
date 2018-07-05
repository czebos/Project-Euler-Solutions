package main

import "fmt"

func main() {
	//https://projecteuler.net/problem=10
	fmt.Print(calcPrimeSum(2000000))
}

func calcPrimeSum(i int) int {
	sum := 2
	nextPrime := 2
	for nextPrime < i {
		fmt.Println(nextPrime)
		j := 2

		for (nextPrime+1)%j != 0 {
			j += 1
			if nextPrime+1%j == 0 && nextPrime+1 != j {
				nextPrime += 1
				j = 2
			}
			if nextPrime+1 == j {
				sum += nextPrime + 1
			}

		}
		nextPrime += 1
	}
	return sum
}

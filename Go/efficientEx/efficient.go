package main

import "fmt"

func main() {
	// https://projecteuler.net/problem=122
	possible := make([]int, 0)
	possible = append(possible, 1)
	outcomes := make([][]int, 0)
	outcomes = append(outcomes, possible)
	i := 2
	size := 0
	for i <= 200 {
		varia := breakDown(i, outcomes)
		minCount := 1000000
		for _, element := range varia {
			outcomes = append(outcomes, element)
			if len(element)-1 < minCount {
				minCount = len(element) - 1
			}
		}
		fmt.Println(outcomes)
		size += minCount
		i += 1
	}
	fmt.Println(size)

}

func breakDown(z int, array [][]int) [][]int {
	a := 0
	minCount := 100000
	for a < len(array) {
		for i := range array[a] {
			for j := range array[a] {
				if (array[a][i] + array[a][j]) == z {
					if len(array[a])+1 < minCount {
						minCount = len(array[a]) + 1
					}
				}
			}
		}
		a += 1
	}
	a = 0
	possible := make([]int, 0)
	for a < len(array) {
		for i := range array[a] {
			for j := range array[a] {
				if j >= i {
					if (array[a][i] + array[a][j]) == z {
						if len(array[a])+1 == minCount {
							possible = append(possible, a)
						}
					}
				}

			}
		}
		a += 1
	}

	situations := make([][]int, 0)

	for i := 0; i < len(possible); i++ {
		temp := make([]int, 0)
		for element := range array[possible[i]] {
			temp = append(temp, array[possible[i]][element])

		}
		temp = append(temp, z)
		situations = append(situations, temp)

	}
	return situations
}

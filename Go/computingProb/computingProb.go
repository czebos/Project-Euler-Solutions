package main

import "fmt"

func main() {
	//https://projecteuler.net/problem=205
	numerator := 0
	denominator := 0
	fourDice := outcomeProb(4, 8, 0)
	sixDice := outcomeProb(6, 5, 0)
	for value := range fourDice {
		for value2 := range sixDice {
			if fourDice[value] > sixDice[value2] {
				numerator += 1
			}
		}
	}
	fmt.Println(numerator)
	fmt.Println(denominator)
}

func outcomeProb(num int, rolls int, sum int) []int {
	numbers := make([]int, 0)
	if rolls > 0 {
		for i := 1; i <= num; i++ {
			numbers = append(numbers, outcomeProb(num, rolls-1, sum+i)...)
		}
	} else {
		for i := 1; i <= num; i++ {
			numbers = append(numbers, sum+i)
		}
	}
	return numbers

}

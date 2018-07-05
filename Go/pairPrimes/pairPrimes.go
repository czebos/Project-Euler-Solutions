package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	//https://projecteuler.net/problem=134
	prev := 5
	sum := 0
	for prev <= 1000000 {
		p := nextPrime(prev)
		sum += findNumber(prev, p)
		prev = p
	}
	fmt.Print(sum)
}

func nextPrime(p int) int {
	n := 2
	p += 1
	for p != n {
		for p%n != 0 {
			n += 1
		}
		if p != n {
			p += 1
			n = 2
		}
	}
	return p
}

func findNumber(z int, divisible int) int {
	string1 := strconv.Itoa(z)
	orig := strconv.Itoa(z)
	n := 1
	for z%divisible != 0 {
		string1 = strings.Join([]string{strconv.Itoa(n), string1}, "")
		int1, _ := strconv.Atoi(string1)
		if int1%divisible != 0 {
			string1 = orig
			n += 1
		} else {
			z = int1
		}
	}
	return z

}

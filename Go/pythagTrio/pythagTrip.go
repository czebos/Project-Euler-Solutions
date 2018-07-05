package main

import (
	"fmt"
)

func main() {
    // https://projecteuler.net/problem=9
    for a := 0;a < 1000;a++ {
        for b:= a+ 1; b<500 - a/2; b++{
            c := 1000 - a - b
            if a*a + b*b == c*c{
                fmt.Println(a,b,c)
                fmt.Print(a*b*c)
            }
        }

    }
}

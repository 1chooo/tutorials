package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	var aList []int
	fmt.Print("請輸入兩個數字： ")
	input := readInput()
	nums := strings.Split(input, " ")
	for _, numStr := range nums {
		num, err := strconv.Atoi(numStr)
		if err != nil {
			fmt.Println("Invalid input.")
			return
		}
		aList = append(aList, num)
	}

	fmt.Printf("Type of aList: %T\n", aList)

	a := 1.23456789
	fmt.Printf("Floor of a: %d\n", int(math.Floor(a)))

	fmt.Print("Enter apple price: ")
	applePrice := readInputAsInt()

	if applePrice > 50 {
		fmt.Println("Do not buy")
	} else if applePrice < 50 {
		fmt.Println("Buy less")
	} else {
		fmt.Println("Buy equal")
	}

	fmt.Println(5 / 2)
	fmt.Println(5.0 / 2)
	fmt.Println(5 / 2.0)
	fmt.Println(5.0 / 2.0)

	a = 10
	// b := 3
	// c := 1
	// x := 1

	// fmt.Println(a*x*x + b*x + c)
	fmt.Println(2*1*1 + 3*1 + 1)

	probability := 0.123456789

	fmt.Println("Probability:", probability)
	fmt.Printf("%.2f\n", probability)
	fmt.Printf("%.2f\n", probability)
	fmt.Printf("%.2f\n", math.Round(probability*100)/100)

	num := 450.2389
	fmt.Printf("%.2f\n", num)
	fmt.Printf("%.2f\n", num)
	fmt.Printf("%.2f\n", math.Round(num*100)/100)

	fmt.Print("請輸入你的名字： ")
	name := readInput()
	fmt.Printf("你好，%s\n", name)

	// fmt.Print("請輸入兩個數字： ")
	// a, b := readTwoIntegers()
	// c := a + b
	// fmt.Printf("計算結果：%d\n", c)

	// fmt.Print("請輸入三個數字： ")
	// a, b, c = readThreeIntegers()
	// fmt.Println(a, b, c)

	aStr := "1 2 3"
	fmt.Printf("Type of aStr: %T\n", aStr)
	bStr := strings.Split(aStr, " ")
	fmt.Printf("Type of bStr: %T\n", bStr)
	fmt.Println(bStr)
}

func readInput() string {
	var input string
	fmt.Scanln(&input)
	return input
}

func readInputAsInt() int {
	input := readInput()
	num, err := strconv.Atoi(input)
	if err != nil {
		fmt.Println("Invalid input.")
		return 0
	}
	return num
}

// func readTwoIntegers() (int, int) {
// 	input := readInput()
// 	nums := strings.Split(input, " ")
// 	if len(nums) != 2 {
// 		fmt.Println("Invalid input.")
// 		return 0, 0
// 	}
// 	a, errA := strconv.Atoi(nums[0])
// 	b, errB := strconv.Atoi(nums[1])
// 	if errA != nil || errB != nil {
// 		fmt.Println("Invalid input.")
// 		return 0, 0
// 	}
// 	return a, b
// }

// func readThreeIntegers() (int, int, int) {
// 	input := readInput()
// 	nums := strings.Split(input, " ")
// 	if len(nums) != 3 {
// 		fmt.Println("Invalid input.")
// 		return 0, 0, 0
// 	}
// 	a, errA := strconv.Atoi(nums[0])
// 	b, errB := strconv.Atoi(nums[1])
// 	c, errC := strconv.Atoi(nums[2])
// 	if errA != nil || errB != nil || errC != nil {
// 		fmt.Println("Invalid input.")
// 		return 0, 0, 0
// 	}
// 	return a, b, c
// }

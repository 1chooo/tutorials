package main

import (
	"fmt"
)

func main() {
	var applePrice int
	fmt.Print("請輸入蘋果價格: ")
	_, err := fmt.Scan(&applePrice)
	if err != nil {
		fmt.Println("錯誤：請輸入有效的數字")
		return
	}
	fmt.Println(applePrice)

	var maxNumber int
	fmt.Println("請輸入數字，以空格分隔：")
	_, err = fmt.Scan(&maxNumber)
	if err != nil {
		fmt.Println("錯誤：請輸入有效的數字")
		return
	}

	for i := 1; i < 2; i++ {
		var num int
		for {
			_, err := fmt.Scan(&num)
			if err != nil {
				fmt.Println("錯誤：請輸入有效的數字")
				continue
			}
			if num > maxNumber {
				maxNumber = num
			}
			break
		}
	}

	fmt.Println("最大的數字是:", maxNumber)

	var n int
	fmt.Print("請輸入一個數字: ")
	_, err = fmt.Scan(&n)
	if err != nil {
		fmt.Println("錯誤：請輸入有效的數字")
		return
	}

	if n >= 70 {
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}
}

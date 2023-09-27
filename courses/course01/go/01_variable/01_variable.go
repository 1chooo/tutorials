package main

import "fmt"

func main() {
    num := 100          // 變數 num 被賦予為 100 的數值
    word := "hello"     // 變數 word 被賦予為 'hello' 的字串
    area := 5 * 2       // 變數 area 被賦予為 5 * 2 的運算式

    word = "Hello CIA!"
    fmt.Println(word)
    fmt.Println("Hello CIA!")

    fmt.Println(num)
    fmt.Println(100)

    area = 5 * 2
    fmt.Println(area)
    fmt.Println(5 * 2)
}

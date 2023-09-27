package main

import "fmt"

func main() {
    applePrice := 50

    if applePrice > 50 {
        fmt.Println("Do not buy")
    } else if applePrice < 50 {
        fmt.Println("buy less")
    } else if applePrice == 50 {
        fmt.Println("buy equal")
    }

    applePrice = 50

    if applePrice > 50 {
        fmt.Println("Do not buy")
    } else {
        fmt.Println("buy")
    }

    applePrice = 50

    if applePrice > 50 {
        fmt.Println("Do not buy")
    } else if applePrice <= 50 {
        fmt.Println("buy")
    }
}

package main

import "fmt"

func main() {
    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }

    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }

    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }

    for i := 0; i < 10; i += 2 {
        fmt.Println(i)
    }

    for i := 0; i < 10; i++ {
        if i == 5 {
            fmt.Println(i)
            fmt.Println("舉手發問")
        } else {
            fmt.Println(i)
            fmt.Println("不舉手發問")
        }
    }

    for i := 0; i < 100; i++ {
        if i == 20 || i == 27 || i == 52 {
            fmt.Println(i)
            fmt.Println("hi")
        } else {
            fmt.Println(i)
            fmt.Println("no")
        }
    }
}

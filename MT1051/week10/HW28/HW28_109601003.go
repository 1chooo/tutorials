/*
Created Date: 2023/11/27
HW: 28
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func main() {
	A := [][]int{
		{25, 32, 18},
		{16, 22, 54},
		{31, 29, 8},
		{25, 14, 65},
	}

	B := [][]int{
		{14, 24, 7},
		{52, 32, 13},
		{33, 24, 55},
		{72, 81, 29},
	}

	result := elementWiseMultiplication(A, B)

	fmt.Println("A * B = {")
	printMatrix(result)
    fmt.Println("}")
}

func elementWiseMultiplication(A, B [][]int) [][]int {
	if len(A) != len(B) || len(A[0]) != len(B[0]) {
		panic("Matrices must have the same dimensions for element-wise multiplication")
	}

	rows, cols := len(A), len(A[0])
	result := make([][]int, rows)

	for i := 0; i < rows; i++ {
		result[i] = make([]int, cols)
		for j := 0; j < cols; j++ {
			result[i][j] = A[i][j] * B[i][j]
		}
	}

	return result
}

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
        fmt.Print("   ")
		fmt.Print(row)
        fmt.Println(",")
	}
}

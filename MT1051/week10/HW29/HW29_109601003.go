/*
Created Date: 2023/11/27
HW: 29
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
    "strings"
)

func main() {
	location := []string{
		"台北 - 桃園",
		"台北 - 新竹",
		"台北 - 台中",
		"台北 - 嘉義",
		"台北 - 高雄",
		"台北 - 花蓮",
	}
	prices := []int{44, 116, 241, 386, 544, 284}
	people := [][]int{
		{35273, 21534, 12573, 31567, 52386, 44138},
		{25673, 55728, 31245, 33278, 51342, 22464},
		{21345, 22179, 32189, 36296, 33106, 43278},
		{53278, 32785, 43167, 21367, 44579, 32685},
	}

	revenue := make([][]int, len(location))
	for i := range revenue {
		revenue[i] = make([]int, len(people[0]))
	}

	for i := 0; i < len(location); i++ {
		for j := 0; j < len(people); j++ {
			revenue[i][j] = prices[i] * people[j][i]
		}
	}

	fmt.Println("Q1:")
	fmt.Println("| 起站 | 終站 | Q1 營收 | Q2 營收 | Q3 營收 | Q4 總營收 |")
	fmt.Println("| ---- | ---- | ------- | ------- | ------- | --------- |")

	totalRevenue := make([]int, len(location))
	for i := 0; i < len(location); i++ {
		total := revenue[i][0] + revenue[i][1] + revenue[i][2] + revenue[i][3]
		totalRevenue[i] = total

		startEnd := splitLocation(location[i])
		fmt.Printf("| %s | %s | %d | %d | %d | %d |\n", startEnd[0], startEnd[1], revenue[i][0], revenue[i][1], revenue[i][2], revenue[i][3])
	}

	fmt.Println("\nQ2:")
	fmt.Println("| 起站 | 終站 | Q1, Q2, Q3, Q4 的總營收 |")
	fmt.Println("| ---- | ---- | ----------------------- |")

	for i := 0; i < len(location); i++ {
		startEnd := splitLocation(location[i])
		fmt.Printf("| %s | %s | %d |\n", startEnd[0], startEnd[1], totalRevenue[i])
	}

	fmt.Println("\nQ3:")
	maxRevenue := make([]int, len(location))
	maxRevenueIndex := make([]int, len(location))

	fmt.Println("各站年度最高營收季度:")
	fmt.Println("| 起站 | 終站 | 最高營收 | 季度 |")
	fmt.Println("| ---- | ---- | -------- | ---- |")

	for i := 0; i < len(location); i++ {
		max := revenue[i][0]
		index := 0
		for j := 1; j < len(people[0]); j++ {
			if revenue[i][j] > max {
				max = revenue[i][j]
				index = j
			}
		}
		maxRevenue[i] = max
		maxRevenueIndex[i] = index

		startEnd := splitLocation(location[i])
		fmt.Printf("| %s | %s | %d | Q%d |\n", startEnd[0], startEnd[1], max, index+1)
	}

	maxRevenueIndexOverall := argmax(revenue)
	maxRevenueIndexRow, maxRevenueIndexCol := unravelIndex(maxRevenueIndexOverall, len(location), len(people[0]))
	routeWithMaxRevenue := location[maxRevenueIndexRow]
	quarterWithMaxRevenue := maxRevenueIndexCol + 1
	maxRevenueForRoute := revenue[maxRevenueIndexRow][maxRevenueIndexCol]

	fmt.Printf("最高營收的航線是：%s 在第 %d 季度，該航線在該季度的營收為：%d 元\n", routeWithMaxRevenue, quarterWithMaxRevenue, maxRevenueForRoute)
}

func splitLocation(loc string) []string {
	return strings.Split(loc, " - ")
}

func argmax(arr [][]int) int {
	maxVal := arr[0][0]
	index := 0
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr[i]); j++ {
			if arr[i][j] > maxVal {
				maxVal = arr[i][j]
				index = i*len(arr[i]) + j
			}
		}
	}
	return index
}

func unravelIndex(index, rows, cols int) (int, int) {
	row := index / cols
	col := index % cols
	return row, col
}

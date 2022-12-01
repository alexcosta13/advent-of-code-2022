package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func parseInput(filePath string) ([]int, error) {
	readFile, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer readFile.Close()

	sc := bufio.NewScanner(readFile)

	var input []int
	var totalElf int

	for sc.Scan() {
		i, err := strconv.Atoi(sc.Text())

		if err != nil {
			// empty line
			input = append(input, totalElf)
			totalElf = 0
		} else {
			totalElf = totalElf + i
		}
	}
	return input, nil
}

func partOne(calories []int) int {
	max := 0
	for _, elf := range calories {
		if elf > max {
			max = elf
		}
	}
	return max
}

func partTwo(calories []int) int {
	max1 := 0
	max2 := 0
	max3 := 0

	for _, elf := range calories {
		if elf > max1 {
			max3 = max2
			max2 = max1
			max1 = elf
		} else if elf > max2 {
			max3 = max2
			max2 = elf
		} else if elf > max3 {
			max3 = elf
		}
	}

	return max1 + max2 + max3
}

func main() {
	calories, err := parseInput("input.txt")
	if err != nil {
		panic(err.Error())
	}

	resultOne := partOne(calories)
	fmt.Printf("First part: %d\n", resultOne)

	resultTwo := partTwo(calories)
	fmt.Printf("Second part: %d\n", resultTwo)
}

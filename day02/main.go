package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var TRANSFORM = map[string]string{
	"X": "A",
	"Y": "B",
	"Z": "C",
}

var SCORES = map[string]int{
	"A": 1,
	"B": 2,
	"C": 3,
}

var WIN = map[string]string{
	"A": "B",
	"B": "C",
	"C": "A",
}

var LOSE = map[string]string{
	"A": "C",
	"B": "A",
	"C": "B",
}

func parseInput(filePath string) ([][]string, error) {
	readFile, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer readFile.Close()

	sc := bufio.NewScanner(readFile)

	var data [][]string

	for sc.Scan() {
		line := strings.Fields(sc.Text())
		data = append(
			data,
			[]string{line[0], TRANSFORM[line[1]]},
		)
	}
	return data, nil
}

func partOne(data [][]string) int {
	score := 0
	for _, line := range data {
		if line[0] == line[1] {
			score = score + 3
		} else if WIN[line[0]] == line[1] {
			score = score + 6
		}
		score += SCORES[line[1]]
	}
	return score
}

func partTwo(data [][]string) int {
	var moves [][]string
	for _, line := range data {
		var move string
		if line[1] == "A" {
			// need to lose
			move = LOSE[line[0]]
		} else if line[1] == "B" {
			// need to draw
			move = line[0]
		} else if line[1] == "C" {
			// need to win
			move = WIN[line[0]]
		}
		moves = append(moves, []string{line[0], move})
	}
	return partOne(moves)
}

func main() {
	games, err := parseInput("input.txt")
	if err != nil {
		panic(err.Error())
	}

	resultOne := partOne(games)
	fmt.Printf("First part: %d\n", resultOne)

	resultTwo := partTwo(games)
	fmt.Printf("Second part: %d\n", resultTwo)
}

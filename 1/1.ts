import fs from "fs";

const nums: number[][] = [];
let cur: number[] = [];

fs.readFile("input.txt", "utf8", (err: unknown, data: string) => {
  if (err instanceof Error) {
    throw new Error(`Error : ${err}`);
  } else {
    for (let line of data.split("\n")) {
      let curLine = parseInt(line);
      if (Number.isNaN(curLine)) {
        nums.push([...cur]);
        cur = [];
        continue;
      }
      cur.push(curLine);
    }
  }

  const sortArr = (arr: number[]): number[] => {
    return arr.sort((a, b) => (a < b ? -1 : 1));
  };

  const maxValue = (arr: number[]) => {
    return arr.reduce((cur: number, acc: number) => (cur > acc ? cur : acc), 0);
  };

  const total_calories: number[] = [];

  for (let cals of nums) {
    total_calories.push(
      cals.reduce((cur: number, prev: number) => prev + cur, 0)
    );
  }

  const sortedCals = sortArr(total_calories);
  console.log(`Part 1: ${maxValue(total_calories)}`);
  console.log(
    `Part 2 : ${sortedCals
      .splice(sortedCals.length - 3)
      .reduce((cur: number, acc: number) => {
        return cur + acc;
      }, 0)}`
  );
});

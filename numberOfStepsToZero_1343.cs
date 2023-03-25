public int NumberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            if (num % 2 == 0) { // even -> divide by two
                num = num / 2;
            } else { //odd -> subtract 1
                num = num - 1;
            }
            steps++;
        }
        return steps;
    }

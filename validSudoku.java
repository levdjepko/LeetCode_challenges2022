class Solution {
    public boolean isValidSudoku(char[][] board) {
        // check if the Sudoku board is valid
        // check rows:
        
        boolean validBoard = true;
        HashSet<String> set = new HashSet<>();
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                // iterate over every position on the board
                char currentChar = board[i][j];
                if (currentChar == '.') {
                    continue;
                } else {
                    if(!set.add(currentChar + " found in row " + i) ||
                        !set.add(currentChar + " found in column " + j) ||
                        !set.add(currentChar + " found in sub Box " + i/3 + j/3))
                        return false;
                    }
   
            }
        }
        
        
        return validBoard;
    }
}

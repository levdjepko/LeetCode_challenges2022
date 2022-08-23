class Solution {
    public boolean isValidSudoku(char[][] board) {
        // check if Sudoku board is valid
        // check rows:
        int[] check = new int[20];
        Arrays.fill(check, 0);
        boolean validBoard = true;
        
        for (int i = 0; i < board.length && validBoard; i++) {
            Arrays.fill(check, 0);
            for (int column = 0; column < board[i].length && validBoard; column++) {
                if (Character.isDigit(board[i][column])){
                    check[(int)board[i][column]]++;
                }
                if (check[(int)board[i][column]] > 1) {
                    validBoard = false;
                }
            }
        }
        return validBoard;
}

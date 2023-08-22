/*You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.*/

public class Solution {
    public void Rotate(int[][] matrix) {
        // 1 . Transpose the matrix in place
        int size = matrix.GetLength(0);
        
        for (int i = 0; i < size; i++) {
            for (int j = i; j < size; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        // 2 . Swap the left and right
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][size - j - 1];
                matrix[i][size - j - 1] = temp;
            }
        }
        
    }
}

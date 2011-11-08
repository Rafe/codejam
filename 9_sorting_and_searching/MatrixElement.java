public class MatrixElement{
  public static void main(String[] args){
    
  }

  public static boolean findElement(int[][] matrix, int element){
    int M = matrix.length,
        N = matrix[0].length;
    int row = 0;
    int col = N-1;

    while(row < M && col >= 0){
      if(element == matrix[row][col]){
        return true;
      }else if(element < matrix[row][col]){
        col--;
      }else{
        row++;
      }
    }
    return false;
  }
}

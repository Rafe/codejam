class TicTacToe{
  enum Piece{
    Empty, Blue,Red
  };

  public int getWinner(int[][] board){
    if(board.length <= 0){
      throw EmptyBoardException();
    }

    int[] rowCount = new int[board.length];
    int[] colCount = new int[board[0].length];
    int diaCount = new int[2];
    int winner = 0;
    for(int i =0 ; i<board.length;i++){
      for(int j = 0; j < board[0].length;j++){
        rowCount[i] += board[i][j];
        colCount[j] += board[i][j];
        if(i==j){
          diaCount[0] += board[i][j];
        }
        if(i+j == board.length){
          diaCount[1] += board[i][j];
        }
      }
    }
    winner = getWinner(colCount);
    if(winner != 0) return winner; 
    winner = getWinner(rowCount);
    if(winner != 0) return winner; 
    winner = getWinner(diaCount);
    if(winner != 0) return winner; 
  }

  public int getWinner(int[] counts){
    int blueWin = 3;
    int redWin = 6;
    for(int e:counts){
      if(e==blueWin) return Piece.Blue;
      if(e==redWin) return Piece.Red;
    }
    return Piece.Empty;
  }
}


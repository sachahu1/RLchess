from typing import List, Tuple

from rlchess.board.slot import Slot


class ChessBoard(object):
  def __init__(self):
    self.board = self.compute_board()

  @staticmethod
  def compute_board() -> List[Slot]:
    board = []
    for row in range(8):
      for column in range(8):

        slot = Slot(row=row, column=column)

        board.append(slot)
    return board

  def __iter__(self):
    return iter(self.board)

  def __len__(self):
    return len(self.board)

  def __getitem__(self, position: Tuple[int, int]) -> Slot:
    row, column = position
    return self.board[row * 8 + column]

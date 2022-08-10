import logging
from typing import List, Tuple

from rlchess.board.pieces.pieces import Pieces, PieceColor
from rlchess.board.slot import Slot


class ChessBoard(object):
  def __init__(self):
    self.board = self.compute_board()
    self.place_initial_pieces()

  def place_initial_pieces(self):
    for column in range(8):
      color = PieceColor.WHITE
      # Place white pieces
      piece = Pieces.get_initial_piece(row=0, column=column, color=color)
      self[0, column].piece = piece
      logging.debug(f"Placing white {piece} at {0, column}")

      # Place white pawns
      piece = Pieces.get_initial_piece(row=1, column=column, color=color)
      self[1, column].piece = piece
      logging.debug(f"Placing white {piece} at {1, column}")

      color = PieceColor.BLACK

      # Place black pieces
      piece = Pieces.get_initial_piece(row=7, column=column, color=color)
      self[7, column].piece = piece
      logging.debug(f"Placing black {piece} at {7, column}")

      # Place black pawns
      piece = Pieces.get_initial_piece(row=6, column=column, color=color)
      self[6, column].piece = piece
      logging.debug(f"Placing black {piece} at {6, column}")

  @staticmethod
  def compute_board() -> List[Slot]:
    board = []
    for column in range(8):
      for row in range(8):

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

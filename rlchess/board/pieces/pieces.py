import pathlib
from enum import Enum

import pygame.image

from rlchess.board.pieces.abstract_piece import AbstractPiece
from rlchess.board.pieces.bishop import Bishop
from rlchess.board.pieces.king import King
from rlchess.board.pieces.knight import Knight
from rlchess.board.pieces.pawn import Pawn
from rlchess.board.pieces.queen import Queen
from rlchess.board.pieces.rook import Rook


class PiecesEnum(str, Enum):
  ROOK = "rook"
  LKNIGHT = "Lknight"
  RKNIGHT = "Rknight"
  BISHOP = "bishop"
  KING = "king"
  QUEEN = "queen"
  PAWN = "pawn"

class PieceImage(object):
  def __init__(self, image_path: pathlib.Path):
    self.image_path = image_path

    self.svg_image = pygame.image.load(image_path)

    self.image_size = self.svg_image.get_size()
    self.piece_size = (self.image_size[0] // 7 + 5, self.image_size[1] // 2)


class PieceColor(str, Enum):
  WHITE = "white"
  BLACK = "black"

class Pieces(object):
  white_pieces_order = [PiecesEnum.ROOK, PiecesEnum.LKNIGHT, PiecesEnum.BISHOP, PiecesEnum.KING, PiecesEnum.QUEEN, PiecesEnum.BISHOP, PiecesEnum.RKNIGHT, PiecesEnum.ROOK]
  black_pieces_order = white_pieces_order[::-1]

  pieces = {
    PiecesEnum.ROOK: (0, Rook),
    PiecesEnum.LKNIGHT: (1, Knight),
    PiecesEnum.BISHOP: (2, Bishop),
    PiecesEnum.KING: (3, King),
    PiecesEnum.QUEEN: (4, Queen),
    PiecesEnum.RKNIGHT: (5, Knight),
    PiecesEnum.PAWN: (6, Pawn),
  }

  image = PieceImage(pathlib.Path(__file__).parent.parent.parent / "assets/Chess-Pieces.svg")

  @classmethod
  def get_piece(cls, piece: PiecesEnum, color: PieceColor) -> AbstractPiece:

    piece_number, piece_object = cls.pieces[piece]

    piece_surface = pygame.Surface(cls.image.piece_size, pygame.SRCALPHA)

    if color == PieceColor.WHITE:
      piece_surface.blit(
        cls.image.svg_image,
        (0, 0),
        (piece_number * cls.image.piece_size[0], 0, (piece_number + 1) * cls.image.piece_size[0], cls.image.piece_size[1]),
      )
    else:
      piece_surface.blit(
        cls.image.svg_image,
        (0, 0),
        (piece_number * cls.image.piece_size[0], cls.image.piece_size[1], (piece_number + 1) * cls.image.piece_size[0], cls.image.image_size[1]),
      )

    return piece_object(piece_surface)

  @classmethod
  def get_initial_piece(cls, row: int, column: int, color: PieceColor):
    if row == 1 or row == 6:
      piece = PiecesEnum.PAWN
      return cls.get_piece(piece, color)

    if color == PieceColor.WHITE:
      return cls.get_piece(piece=cls.white_pieces_order[column], color=color)
    else:
      return cls.get_piece(piece=cls.black_pieces_order[column], color=color)

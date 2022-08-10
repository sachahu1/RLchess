from typing import Optional

import pygame

from rlchess.board.pieces.abstract_piece import AbstractPiece


class Rook(AbstractPiece):
  def __init__(self, image: Optional[pygame.Surface] = None):
    self.image = image

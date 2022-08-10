import logging
from typing import Optional

import pygame

from rlchess.board.board_config import BoardConfig
from rlchess.board.color_palette import ColorPalette
from rlchess.board.pieces.abstract_piece import AbstractPiece
from rlchess.utils.slot_utils import is_even


class Slot(object):
  def __init__(self, row, column):
    self.column_size = None
    self.row_size = None
    self.row = row
    self.column = column

    self._background_color = None

    self.slot_size = self.compute_slot_size()

    self.selected = False

    if is_even(self.row) != is_even(self.column):
      self.background_color = ColorPalette.LIGHT
    else:
      self.background_color = ColorPalette.DARK
    self.base_color = self.background_color

    self._has_piece = False
    self._piece: Optional[AbstractPiece] = None

  @property
  def piece(self) -> Optional[AbstractPiece]:
    return self._piece

  @piece.setter
  def piece(self, value: Optional[AbstractPiece]):
    self._piece = value

    if value:
      self._has_piece = True
    else:
      self._has_piece = False

  @property
  def has_piece(self):
    return self._has_piece

  @has_piece.setter
  def has_piece(self, value: bool):
    self._has_piece = value

  def compute_slot_size(self):
    self.row_size = BoardConfig.screen_size[0] // 8
    self.column_size = BoardConfig.screen_size[1] // 8
    return self.row_size, self.column_size

  @property
  def background_color(self):
    return self._background_color

  @background_color.setter
  def background_color(self, color: pygame.Color):
    self._background_color = color

  @property
  def drawing(self) -> pygame.Surface:
    slot_surface = pygame.Surface(self.slot_size)
    slot_surface.fill(self.background_color)

    if self.has_piece:
      piece_image = self.piece.image
      piece_image = pygame.transform.scale(piece_image, self.slot_size)
      slot_surface.blit(piece_image, (0, 0))

    return slot_surface

  def select(self):
    logging.debug(f"Selected Slot {self.row, self.column}")
    selected_color = pygame.Color(ColorPalette.SELECTED)
    selected_color = selected_color.lerp(self.background_color, 0.5)

    self.background_color = selected_color
    self.selected = True

  def unselect(self):
    self.background_color = self.base_color
    self.selected = False


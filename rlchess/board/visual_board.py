from typing import Tuple, Optional

import pygame

from rlchess.board.board import ChessBoard
from rlchess.board.board_config import BoardConfig
from rlchess.board.slot import Slot


class VisualBoard(object):

  def __init__(self, screen_size: Tuple[int, int] = BoardConfig.screen_size):
    pygame.init()

    self.board = ChessBoard()

    self.screen_size = screen_size
    self.height, self.width = self.screen_size[0], self.screen_size[1]
    self.screen = pygame.display.set_mode(screen_size)

    self.slot_size = self.screen_size[0] // 8, self.screen_size[1] // 8

    self.draw_board()

    self.selected_slot: Optional[Slot] = None

  def draw_board(self):
    for slot in self.board:
      self.screen.blit(slot.drawing, (slot.row * slot.row_size, slot.column * slot.column_size))

    pygame.display.flip()

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (
          (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
          running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
          row, column = self.find_click(event.pos)
          slot = self.board[row, column]
          self.select(slot)

      self.draw_board()

    pygame.quit()

  def find_click(self, click_position: Tuple[int, int]) -> Tuple[int, int]:
    return click_position[1] // self.slot_size[1], click_position[0] // self.slot_size[0]

  def select(self, slot):
    if self.selected_slot:
      self.selected_slot.unselect()
      self.selected_slot = None

    slot.select()
    self.selected_slot = slot

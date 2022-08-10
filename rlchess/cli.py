import logging

from rlchess.board.visual_board import VisualBoard


def run():
  board = VisualBoard()
  board.run()

if __name__ == '__main__':
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  run()

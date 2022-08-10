import abc
from typing import Optional

import pygame


class AbstractPiece(abc.ABC):
  @abc.abstractmethod
  def __init__(self, image: Optional[pygame.Surface] = None):
    self.image = image


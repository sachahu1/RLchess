from dataclasses import dataclass
from typing import Tuple


@dataclass
class BoardConfig:
  screen_size: Tuple[int, int] = (640, 640)

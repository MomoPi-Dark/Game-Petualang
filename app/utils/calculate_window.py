class CalculateWindow:
    """Aspect Ratio = 9 / 16 for Portrait, 16 / 9 for Landscape"""

    ASPECT_RATIOS = {"portrait": (9, 16), "landscape": (16, 9)}

    def __init__(self, window_width: int, aspect_ratio: str | tuple[int, int]):
        # Determine aspect ratio
        if (
            isinstance(aspect_ratio, tuple)
            and len(aspect_ratio) == 2
            and all(isinstance(x, int) and x > 0 for x in aspect_ratio)
        ):
            self.aspect_ratio = aspect_ratio
        elif aspect_ratio in self.ASPECT_RATIOS:
            self.aspect_ratio = self.ASPECT_RATIOS[aspect_ratio]
        else:
            raise ValueError(
                f"Invalid aspect ratio. Choose from: {', '.join(self.ASPECT_RATIOS.keys())} or provide a tuple of positive integers."
            )

        self._window_width = window_width
        self._window_height = self._calculate_height()

    def _calculate_height(self) -> int:
        width_ratio, height_ratio = self.aspect_ratio
        return int(self._window_width * height_ratio / width_ratio)

    def get_size(self):
        return self._window_width, self._window_height

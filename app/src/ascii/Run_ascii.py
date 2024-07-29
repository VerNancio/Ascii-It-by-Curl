import os

from .Ascii import Ascii

from ..colors import COLOR

class Run_ascii(Ascii):

    # def __init__(self) -> None:
        
    #     self.valid_extension: list[str] = ["mp4"]

    def __init__(self) -> None:

        super().__init__()


    def run_ascii(self, ascii_frames: list[str], max_loops = -1, color = COLOR['light_cyan']):

        loop_count = 0

        while True:

            loop_count += 1

            for frame in ascii_frames:

                yield color + f"\033[2J\033[1;1f{frame}"

            if loop_count == max_loops: 
                break

    
    def run_ascii_group(self, ascii_list: list[list[str]], max_loops: int = 2):

        while True:

            for ascii_frames in ascii_list:

                for ascii in self.run_ascii(ascii_frames=ascii_frames, max_loops=max_loops):

                    yield ascii

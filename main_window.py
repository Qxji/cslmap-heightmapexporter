import sys
import os
import glob

from city_data import CityData


def load_city(clsmap_path=None):  # passed sys.argv earlier to clsmap_path
    if clsmap_path is None:  # if sys.argv is empty (None), get path from dropped in *.cslmap file
        clsmap_path = glob.glob("*.cslmap")[0]
    __load_city_elements(clsmap_path)  # loads terrain, networks, buildings, transit
    backend_size = 4096


def __load_city_elements(clsmap_path):
    city_data = CityData(clsmap_path)
    city_data.get_terrains()


if __name__ == "__main__":
    print(sys.argv[1])
    if len(sys.argv) > 1:
        load_city(sys.argv[1])
    else:
        load_city()
    # sys.argv gets the specified path when running "python main_window.py <path_to_cslmap>"


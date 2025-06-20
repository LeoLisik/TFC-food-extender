from tfcfe_gen.Crop import Crop
from mcresources import ResourceManager


def generate_Crops():
    (Crop(rm, "buckwheat", "tfcfe", 8)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_food_item(None, 4, 0, 2)
     .generate_loot_table()
     .generate_climate_range(25, 100, 0, -4, 35, 5))


def generate_MNACrops():
    (Crop(rm, "wakebloom", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:wakebloom")
     .generate_climate_range(70, 100, 5, -10, 25, 10))

    (Crop(rm, "aum", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:aum")
     .generate_climate_range(25, 100, 0, -4, 35, 5))

    (Crop(rm, "cerublossom", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:cerublossom")
     .generate_climate_range(25, 100, 0, -4, 35, 5))

    (Crop(rm, "tarma_root", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:tarma_root")
     .generate_climate_range(70, 100, 5, -10, 25, 10))

    (Crop(rm, "desert_nova", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:desert_nova")
     .generate_climate_range(10, 40, 10, 5, 40, 10))


if __name__ == "__main__":
    rm = ResourceManager('tfcfe', 'src/main/resources')
    rm.lang({
        f"tfcfe.creative_tab.main": "TFC Food Extender"
    })
    generate_Crops()
    generate_MNACrops()
    rm.flush()

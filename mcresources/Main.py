from tfcfe_gen.Crop import Crop
from mcresources import ResourceManager

if __name__ == "__main__":
    rm = ResourceManager('tfcfe', 'src/main/resources')
    (Crop(rm, "buckwheat", "tfcfe", 8)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_food_item(None, 4, 0, 2)
     .generate_loot_table()
     .generate_climate_range(25, 100, 0, -4, 35, 5))

    (Crop(rm, "desert_nova", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:desert_nova")
     .generate_climate_range(25, 100, 0, -4, 35, 5))

    rm.flush()

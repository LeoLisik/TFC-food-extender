from tfcfe_gen.Crop import Crop
from tfcfe_gen.Item import Item
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
     .generate_climate_range(70, 100, 5, -10, 25, 10)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/wakebloom"}, 2000, 5, 5, 1))

    (Crop(rm, "aum", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:aum")
     .generate_climate_range(25, 100, 0, -4, 35, 5)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/aum"}, 2000, 5, 5, 1))

    (Crop(rm, "cerublossom", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:cerublossom")
     .generate_climate_range(25, 100, 0, -4, 35, 5)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/cerublossom"}, 2000, 5, 5, 1))

    (Crop(rm, "tarma_root", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:tarma_root")
     .generate_climate_range(70, 100, 5, -10, 25, 10)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/tarma_root"}, 2000, 5, 5, 1))

    (Crop(rm, "desert_nova", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:desert_nova")
     .generate_climate_range(10, 40, 10, 5, 40, 10)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/desert_nova"}, 2000, 5, 5, 1))


def generate_prepared_seeds():
    (Item(rm, "prepared_seeds", "wakebloom", "tfcfe")
     .generate_base()
     .generate_vanilla_craft(
        ingredients=['#tfc:seeds', 'tfc:plant/water_lily', 'tfc:rock/gravel/shale'],
        result_count=1,
        shaped=False))

    (Item(rm, "prepared_seeds", "aum", "tfcfe")
     .generate_base()
     .generate_vanilla_craft(
        ingredients=['#tfc:seeds', 'tfc:dirt/sandy_loam', 'tfc:plant/primrose', 'tfc:plant/butterfly_milkweed'],
        result_count=1,
        shaped=False))

    (Item(rm, "prepared_seeds", "cerublossom", "tfcfe")
     .generate_base()
     .generate_vanilla_craft(
        ingredients=['#tfc:seeds', 'tfc:dirt/sandy_loam', 'tfc:plant/grape_hyacinth'],
        result_count=1,
        shaped=False))

    (Item(rm, "prepared_seeds", "tarma_root", "tfcfe")
     .generate_base()
     .generate_vanilla_craft(
        ingredients=['#tfc:seeds', 'tfc:plant/arrowhead', 'tfc:food/cattail_root', 'tfc:mud/loam'],
        result_count=1,
        shaped=False))

    (Item(rm, "prepared_seeds", "desert_nova", "tfcfe")
     .generate_base()
     .generate_vanilla_craft(
        ingredients=['#tfc:seeds', '#forge:sand', 'tfc:plant/barrel_cactus'],
        result_count=1,
        shaped=False))


if __name__ == "__main__":
    rm = ResourceManager('tfcfe', 'src/main/resources')
    rm.lang({
        f"tfcfe.creative_tab.main": "TFC Food Extender"
    })
    generate_Crops()
    generate_MNACrops()
    generate_prepared_seeds()
    rm.flush()

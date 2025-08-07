from tfcfe_gen.Book import Book
from tfcfe_gen.Crop import Crop
from tfcfe_gen.Item import Item
from mcresources import ResourceManager
from tfcfe_gen.Utils import mod_loaded


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
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/wakebloom"}, 2000, 5, 5, 1)
     .generate_seed_craft(["#tfc:seeds", "tfc:plant/water_lily", "tfc:rock/gravel/shale"], 1, False, conditions=[
        {
          "type": "forge:not",
          "value": {
            "type": "forge:mod_loaded",
            "modid": "bloodmagic"
          }
        }
      ]))

    (Crop(rm, "aum", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:aum")
     .generate_climate_range(25, 100, 0, -4, 35, 5)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/aum"}, 2000, 5, 5, 1)
     .generate_seed_craft(["#tfc:seeds", "tfc:dirt/sandy_loam", "tfc:plant/primrose", "tfc:plant/butterfly_milkweed"], 1, False, conditions=[
        {
            "type": "forge:not",
            "value": {
                "type": "forge:mod_loaded",
                "modid": "bloodmagic"
            }
        }
    ])
     )

    (Crop(rm, "cerublossom", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:cerublossom")
     .generate_climate_range(25, 100, 0, -4, 35, 5)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/cerublossom"}, 2000, 5, 5, 1)
     .generate_seed_craft(["#tfc:seeds", "tfc:dirt/sandy_loam", "tfc:plant/grape_hyacinth"], 1, False, conditions=[
        {
            "type": "forge:not",
            "value": {
                "type": "forge:mod_loaded",
                "modid": "bloodmagic"
            }
        }
    ])
     )

    (Crop(rm, "tarma_root", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:tarma_root")
     .generate_climate_range(70, 100, 5, -10, 25, 10)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/tarma_root"}, 2000, 5, 5, 1)
     .generate_seed_craft(["#tfc:seeds", "tfc:plant/arrowhead", "tfc:food/cattail_root", "tfc:mud/loam"], 1, False, conditions=[
        {
            "type": "forge:not",
            "value": {
                "type": "forge:mod_loaded",
                "modid": "bloodmagic"
            }
        }
    ])
     )

    (Crop(rm, "desert_nova", "tfcfe", 6)
     .generate_default_crop()
     .generate_dead_crop()
     .generate_wild_crop()
     .generate_seed_item()
     .generate_loot_table("mna:desert_nova")
     .generate_climate_range(10, 40, 10, 5, 40, 10)
     .generate_bloodmagic_altar_seed_craft({"item": "tfcfe:prepared_seeds/desert_nova"}, 2000, 5, 5, 1)
     .generate_seed_craft(["#tfc:seeds", "#forge:sandstone", "minecraft:water_bucket"], 1, False, conditions=[
        {
            "type": "forge:not",
            "value": {
                "type": "forge:mod_loaded",
                "modid": "bloodmagic"
            }
        }
    ])
     )


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
        ingredients=['#tfc:seeds', '#forge:sandstone', 'minecraft:water_bucket'],
        result_count=1,
        shaped=False))

def update_tfc_book():
    book = Book(
        rm,
        mod_id='tfc',
        book_id='field_guide',
        create_book=False,
        book_name='Field Guide',
        landing_text='Welcome to your journey!'
    )

    category = book.generate_category(
        category_id='magic',
        name='Magic start',
        description='How to start doing magic',
        icon='mna:animus_dust',
        sortnum=11,
        flag='mod:mna'
    )

    entry = category.generate_entry(
        entry_id='getting_start_bloodmagic',
        name='Introduction',
        icon='minecraft:wheat_seeds',
        priority=True,
        flag='&mod:mna,mod:bloodmagic'
    )

    entry.add_text_page(title="Where to start?", text="To explore magic you need some magic flowers. "
                                           "To get them, you need to prepare some seeds, then fill them with magic on "
                                           "blood altar and finally grow seeds like any other crops.")
    entry.add_text_page(text="Next pages will show you how to prepare seeds and grow them! Do not forget the sequence:$(br)"
                             "seed->prepared seed->magic seed->magic crop->flower")

    entry.add_crafting_page("tfcfe:prepared_seeds/wakebloom", text="Wakebloom is a lake crop, so try to find ingredients in there")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
        "pattern": [
            ["X"],
            ["Y"],
            ["0"]
        ],
        "mapping": {
            "X": f"tfcfe:crop/wakebloom[age={age}]",
            "Y": "tfc:farmland/loam"
        }
    })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Wakebloom$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -10 - 25 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 70 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:prepared_seeds/aum",
                            text="Aum is a common crop, so try to find ingredients in forests")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/aum[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Aum$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -4 - 35 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 25 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:prepared_seeds/cerublossom",
                            text="Aum is a common crop, so try to find ingredients in forests")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/cerublossom[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Cerublossom$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -4 - 35 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 25 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:prepared_seeds/tarma_root",
                            text="Tarma root is a swamp crop, so try to find ingredients in there")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/tarma_root[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Tarma Root$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -10 - 25 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 70 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:prepared_seeds/desert_nova",
                            text="Desert nova is a desert crop, so try to find ingredients in there")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/desert_nova[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Desert Nova$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): 5 - 40 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 10 - 40 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.save()

    entry = category.generate_entry(
        entry_id='getting_start',
        name='Introduction',
        icon='minecraft:wheat_seeds',
        priority=True,
        flag='&mod:mna,!mod:bloodmagic')

    entry.add_text_page(title="Where to start?", text="To explore magic you need some magic flowers. "
                                                      "To get them, you need to create some seeds "
                                                      "and grow them like any other crops.")
    entry.add_text_page(
        text="Next pages will show you how to make seeds and grow them! Good luck!")

    entry.add_crafting_page("tfcfe:seeds/wakebloom",
                            text="Wakebloom is a lake crop, so try to find ingredients in there")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/wakebloom[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Wakebloom$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -10 - 25 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 70 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:seeds/aum",
                            text="Aum is a common crop, so try to find ingredients in forests")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/aum[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Aum$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -4 - 35 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 25 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:seeds/cerublossom",
                            text="Aum is a common crop, so try to find ingredients in forests")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/cerublossom[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Cerublossom$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -4 - 35 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 25 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:seeds/tarma_root",
                            text="Tarma root is a swamp crop, so try to find ingredients in there")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/tarma_root[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Tarma Root$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): -10 - 25 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 70 - 100 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.add_crafting_page("tfcfe:seeds/desert_nova",
                            text="Desert nova is a desert crop, so try to find ingredients in there")
    multiblocks = []
    for age in range(6):
        multiblocks.append({
            "pattern": [
                ["X"],
                ["Y"],
                ["0"]
            ],
            "mapping": {
                "X": f"tfcfe:crop/desert_nova[age={age}]",
                "Y": "tfc:farmland/loam"
            }
        })
    entry.add_tfc_multimultiblock_page(multiblocks, "$(bold)Desert Nova$(br)"
                                                    "$(bold)$(l:the_world/climate#temperature)Temperature$(): 5 - 40 °C$(br)"
                                                    "$(bold)$(l:mechanics/hydration)Hydration$(): 10 - 40 %$(br)"
                                                    "$(bold)Nutrient$(): Phosphorus")

    entry.save()


if __name__ == "__main__":
    rm = ResourceManager('tfcfe', 'src/main/resources')
    rm.lang({
        f"tfcfe.creative_tab.main": "TFC Food Extender"
    })
    print("Generating crops")
    generate_Crops()
    print("Generating MNA crops")
    generate_MNACrops()
    print("Generating prepared seeds")
    generate_prepared_seeds()
    print("Generating TFC Field guide updates")
    update_tfc_book()
    rm.flush()
    print("Done")

package io.github.leolisik.tfcfoodextender.common.items;

import io.github.leolisik.tfcfoodextender.TFCFoodExtender;
import io.github.leolisik.tfcfoodextender.common.blocks.FEBlocks;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.Crop;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.ICropLike;
import io.github.leolisik.tfcfoodextender.common.compat.bloodmagic.items.PreparedSeed;
import io.github.leolisik.tfcfoodextender.common.compat.mna.blocks.crop.MNACrop;
import net.dries007.tfc.util.Helpers;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemNameBlockItem;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;
import java.util.function.Supplier;

@SuppressWarnings("unused")
public class FEItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, TFCFoodExtender.MODID);
    public static final Map<Food, RegistryObject<Item>> FOODS = Helpers.mapOfKeys(Food.class, food -> register("food/" + food.name(), () -> new Item(new Item.Properties().food(food.getFoodProperties()))));
    public static final Map<ICropLike, RegistryObject<Item>> CROP_SEEDS = new LinkedHashMap<>();
    public static final Map<PreparedSeed, RegistryObject<Item>> PREPARED_SEEDS = new LinkedHashMap<>();

    static {
        CROP_SEEDS.putAll(Helpers.mapOfKeys(Crop.class, crop -> register("seeds/" + crop.name(), () -> new ItemNameBlockItem(FEBlocks.CROPS.get(crop).get(), new Item.Properties()))));

        if (TFCFoodExtender.isMNALoaded) {
            CROP_SEEDS.putAll(Helpers.mapOfKeys(MNACrop.class, crop -> register("seeds/" + crop.name(), () -> new ItemNameBlockItem(FEBlocks.CROPS.get(crop).get(), new Item.Properties()))));

            if (TFCFoodExtender.isBloodMagicLoaded) {
                PREPARED_SEEDS.putAll(Helpers.mapOfKeys(PreparedSeed.class, seed -> register("prepared_seeds/" + seed.name())));
            }
        }
    }

    private static RegistryObject<Item> register(String name)
    {
        return register(name, () -> new Item(new Item.Properties()));
    }

    private static <T extends Item> RegistryObject<T> register(String name, Supplier<T> item) {
        return ITEMS.register(name.toLowerCase(Locale.ROOT), item);
    }
}

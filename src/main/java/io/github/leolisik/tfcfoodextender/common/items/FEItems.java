package io.github.leolisik.tfcfoodextender.common.items;

import io.github.leolisik.tfcfoodextender.TFCFoodExtender;
import io.github.leolisik.tfcfoodextender.common.blocks.FEBlocks;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.Crop;
import net.dries007.tfc.util.Helpers;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemNameBlockItem;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import java.util.Locale;
import java.util.Map;
import java.util.function.Supplier;

@SuppressWarnings("unused")
public class FEItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, TFCFoodExtender.MODID);
    public static final Map<Crop, RegistryObject<Item>> CROP_SEEDS = Helpers.mapOfKeys(Crop.class, crop -> register("seeds/" + crop.name(), () -> new ItemNameBlockItem(FEBlocks.CROPS.get(crop).get(), new Item.Properties())));

    private static <T extends Item> RegistryObject<T> register(String name, Supplier<T> item) {
        return ITEMS.register(name.toLowerCase(Locale.ROOT), item);
    }
}

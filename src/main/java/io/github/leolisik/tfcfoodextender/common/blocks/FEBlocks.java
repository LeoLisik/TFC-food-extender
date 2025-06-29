package io.github.leolisik.tfcfoodextender.common.blocks;

import io.github.leolisik.tfcfoodextender.TFCFoodExtender;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.Crop;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.ICropLike;
import io.github.leolisik.tfcfoodextender.common.compat.mna.blocks.crop.MNACrop;
import io.github.leolisik.tfcfoodextender.common.items.FEItems;
import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.util.registry.RegistrationHelpers;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;

import javax.annotation.Nullable;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.function.Supplier;

@SuppressWarnings("unused")
public final class FEBlocks {
    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(Registries.BLOCK, TFCFoodExtender.MODID);
    public static final Map<ICropLike, RegistryObject<Block>> CROPS = new LinkedHashMap<>();
    public static final Map<ICropLike, RegistryObject<Block>> DEAD_CROPS = new LinkedHashMap<>();
    public static final Map<ICropLike, RegistryObject<Block>> WILD_CROPS = new LinkedHashMap<>();

    static {
        CROPS.putAll(Helpers.mapOfKeys(Crop.class, crop -> registerNoItem("crop/" +crop.name(), crop::create)));
        DEAD_CROPS.putAll(Helpers.mapOfKeys(Crop.class, crop -> registerNoItem("dead_crop/" + crop.name(), crop::createDead)));
        WILD_CROPS.putAll(Helpers.mapOfKeys(Crop.class, crop -> register("wild_crop/" + crop.name(), crop::createWild)));

        if (TFCFoodExtender.isMNALoaded) {
            CROPS.putAll(Helpers.mapOfKeys(MNACrop.class, crop -> registerNoItem("crop/" +crop.name(), crop::create)));
            DEAD_CROPS.putAll(Helpers.mapOfKeys(MNACrop.class, crop -> registerNoItem("dead_crop/" + crop.name(), crop::createDead)));
            WILD_CROPS.putAll(Helpers.mapOfKeys(MNACrop.class, crop -> register("wild_crop/" + crop.name(), crop::createWild)));
        }
    }

    private static <T extends Block> RegistryObject<T> registerNoItem(String name, Supplier<T> blockSupplier) {
        return register(name, blockSupplier, (Function<T, ? extends BlockItem>) null);
    }

    private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> blockSupplier) {
        return register(name, blockSupplier, block -> new BlockItem(block, new Item.Properties()));
    }

    private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> blockSupplier, @Nullable Function<T, ? extends BlockItem> blockItemFactory) {
        return RegistrationHelpers.registerBlock(FEBlocks.BLOCKS, FEItems.ITEMS, name, blockSupplier, blockItemFactory);
    }
}
package io.github.leolisik.tfcfoodextender.common.blockentities;

import io.github.leolisik.tfcfoodextender.TFCFoodExtender;
import io.github.leolisik.tfcfoodextender.common.blocks.FEBlocks;
import net.dries007.tfc.util.registry.RegistrationHelpers;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;

import java.util.function.Supplier;
import java.util.stream.Stream;

public class FEBlockEntities {
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES = DeferredRegister.create(Registries.BLOCK_ENTITY_TYPE, TFCFoodExtender.MODID);;
    public static final RegistryObject<BlockEntityType<CropBlockEntity>> CROP = register("crop", CropBlockEntity::new, FEBlocks.CROPS.values().stream());

    private static <T extends BlockEntity> RegistryObject<BlockEntityType<T>> register(String name, BlockEntityType.BlockEntitySupplier<T> factory, Stream<? extends Supplier<? extends Block>> blocks) {
        return RegistrationHelpers.register(BLOCK_ENTITIES, name, factory, blocks);
    }
}

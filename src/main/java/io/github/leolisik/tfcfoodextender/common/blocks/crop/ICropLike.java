package io.github.leolisik.tfcfoodextender.common.blocks.crop;

import net.dries007.tfc.common.blockentities.FarmlandBlockEntity;
import net.dries007.tfc.util.climate.ClimateRange;
import net.minecraft.world.level.block.Block;

import java.util.function.Supplier;

public interface ICropLike {
    String getSerializedName();
    FarmlandBlockEntity.NutrientType getPrimaryNutrient();
    Supplier<ClimateRange> getClimateRange();
    Block create();
    Block createDead();
    Block createWild();
}
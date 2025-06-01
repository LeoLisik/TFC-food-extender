package io.github.leolisik.tfcfoodextender.common.blocks.crop;

import io.github.leolisik.tfcfoodextender.common.blocks.FEBlocks;
import io.github.leolisik.tfcfoodextender.common.items.FEItems;
import io.github.leolisik.tfcfoodextender.common.util.climate.ClimateRanges;
import net.dries007.tfc.common.blockentities.FarmlandBlockEntity;
import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.common.blocks.TFCBlockStateProperties;
import net.dries007.tfc.util.climate.ClimateRange;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.properties.IntegerProperty;

import java.util.function.Supplier;

public abstract class DefaultCropBlock extends net.dries007.tfc.common.blocks.crop.DefaultCropBlock
{
    public static DefaultCropBlock create(ExtendedProperties properties, int stages, ICropLike crop)
    {
        final IntegerProperty property = TFCBlockStateProperties.getAgeProperty(stages - 1);
        return new DefaultCropBlock(properties, stages - 1, FEBlocks.DEAD_CROPS.get(crop), FEItems.CROP_SEEDS.get(crop), crop.getPrimaryNutrient(), ClimateRanges.CROPS.get(crop))
        {
            @Override
            public IntegerProperty getAgeProperty()
            {
                return property;
            }
        };
    }

    protected DefaultCropBlock(ExtendedProperties properties, int maxAge, Supplier<? extends Block> dead, Supplier<? extends Item> seeds, FarmlandBlockEntity.NutrientType primaryNutrient, Supplier<ClimateRange> climateRange)
    {
        super(properties, maxAge, dead, seeds, primaryNutrient, climateRange);
    }
}
package io.github.leolisik.tfcfoodextender.common.blocks.crop;

import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.util.climate.ClimateRange;

import java.util.function.Supplier;

public class DeadCropBlock extends net.dries007.tfc.common.blocks.crop.DeadCropBlock {
    public DeadCropBlock(ExtendedProperties properties, Supplier<ClimateRange> range) {
        super(properties, range);
    }
}

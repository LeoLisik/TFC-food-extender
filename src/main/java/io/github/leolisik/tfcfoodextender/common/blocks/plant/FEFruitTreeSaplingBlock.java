package io.github.leolisik.tfcfoodextender.common.blocks.plant;

import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.common.blocks.plant.fruit.FruitTreeSaplingBlock;
import net.dries007.tfc.common.blocks.plant.fruit.Lifecycle;
import net.dries007.tfc.util.climate.ClimateRange;
import net.minecraft.world.level.block.Block;

import java.util.function.Supplier;

public class FEFruitTreeSaplingBlock extends FruitTreeSaplingBlock {
    public FEFruitTreeSaplingBlock(ExtendedProperties properties, Supplier<? extends Block> block, int treeGrowthDays, Supplier<ClimateRange> climateRange, Lifecycle[] stages) {
        super(properties, block, treeGrowthDays, climateRange, stages);
    }

    public FEFruitTreeSaplingBlock(ExtendedProperties properties, Supplier<? extends Block> block, Supplier<Integer> treeGrowthDays, Supplier<ClimateRange> climateRange, Lifecycle[] stages)
    {
        super(properties, block, treeGrowthDays, climateRange, stages);
    }
}

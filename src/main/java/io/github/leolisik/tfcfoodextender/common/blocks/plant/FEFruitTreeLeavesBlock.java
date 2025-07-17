package io.github.leolisik.tfcfoodextender.common.blocks.plant;

import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.common.blocks.plant.fruit.FruitTreeLeavesBlock;
import net.dries007.tfc.common.blocks.plant.fruit.Lifecycle;
import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.util.climate.ClimateRange;
import net.minecraft.core.BlockPos;
import net.minecraft.util.RandomSource;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.state.BlockState;

import java.util.function.Supplier;

public class FEFruitTreeLeavesBlock extends FruitTreeLeavesBlock {
    public FEFruitTreeLeavesBlock(ExtendedProperties properties, Supplier<? extends Item> productItem, Lifecycle[] stages, Supplier<ClimateRange> climateRange, int color)
    {
        super(properties, productItem, stages, climateRange, color);
    }

    // TODO: make animate tick
    /*@Override
    public void animateTick(BlockState state, Level level, BlockPos pos, RandomSource random)
    {
        if (random.nextInt(100) == 0 && state.getValue(LIFECYCLE) == Lifecycle.FLOWERING && Helpers.isBlock(this, FLTags.Blocks.BUZZING_LEAVES))
        {
            SwarmEffect.particles(level, pos, random);
        }
    }*/
}

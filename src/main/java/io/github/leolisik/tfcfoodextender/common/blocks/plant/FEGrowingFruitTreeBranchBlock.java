package io.github.leolisik.tfcfoodextender.common.blocks.plant;

import io.github.leolisik.tfcfoodextender.common.blockentities.FETickCounterBlockEntity;
import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.common.blocks.plant.fruit.FruitTreeLeavesBlock;
import net.dries007.tfc.common.blocks.plant.fruit.GrowingFruitTreeBranchBlock;
import net.dries007.tfc.util.climate.Climate;
import net.dries007.tfc.util.climate.ClimateRange;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;

import java.util.function.Supplier;

public class FEGrowingFruitTreeBranchBlock extends GrowingFruitTreeBranchBlock {
    private final Supplier<ClimateRange> climateRange;

    public FEGrowingFruitTreeBranchBlock(ExtendedProperties properties, Supplier<? extends Block> body, Supplier<? extends Block> leaves, Supplier<ClimateRange> climateRange) {
        super(properties, body, leaves, climateRange);
        this.climateRange = climateRange;
    }

    @Override
    public void randomTick(BlockState state, ServerLevel level, BlockPos pos, RandomSource rand) {
        int hydration = FruitTreeLeavesBlock.getHydration(level, pos);
        float temp = Climate.getTemperature(level, pos);
        if (!this.climateRange.get().checkBoth(hydration, temp, false) && !(Boolean)state.getValue(NATURAL)) {
            FETickCounterBlockEntity.reset(level, pos);
        }
        super.randomTick(state, level, pos, rand);
    }
}

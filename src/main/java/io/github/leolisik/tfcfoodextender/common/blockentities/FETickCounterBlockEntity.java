package io.github.leolisik.tfcfoodextender.common.blockentities;

import net.dries007.tfc.common.blockentities.TickCounterBlockEntity;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockState;

public class FETickCounterBlockEntity extends TickCounterBlockEntity {
    public static void reset(Level level, BlockPos pos)
    {
        level.getBlockEntity(pos, FEBlockEntities.TICK_COUNTER.get()).ifPresent(TickCounterBlockEntity::resetCounter);
    }

    public FETickCounterBlockEntity(BlockPos pos, BlockState state)
    {
        super(FEBlockEntities.TICK_COUNTER.get(), pos, state);
    }

    @Override
    public BlockEntityType<?> getType()
    {
        return FEBlockEntities.TICK_COUNTER.get();
    }
}

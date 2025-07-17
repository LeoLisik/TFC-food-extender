package io.github.leolisik.tfcfoodextender.common.blockentities;

import net.dries007.tfc.common.blockentities.BerryBushBlockEntity;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockState;

public class FEBerryBushBlockEntity extends BerryBushBlockEntity {
    public FEBerryBushBlockEntity(BlockPos pos, BlockState state)
    {
        super(pos, state);
    }

    protected FEBerryBushBlockEntity(BlockEntityType<?> type, BlockPos pos, BlockState state)
    {
        super(type, pos, state);
    }

    @Override
    public BlockEntityType<?> getType()
    {
        return FEBlockEntities.BERRY_BUSH.get();
    }
}

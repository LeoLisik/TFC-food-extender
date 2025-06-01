package io.github.leolisik.tfcfoodextender.common.blockentities;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;

public class CropBlockEntity extends net.dries007.tfc.common.blockentities.CropBlockEntity {
    public CropBlockEntity(BlockPos pos, BlockState state) {
        super(FEBlockEntities.CROP.get(), pos, state);
    }
}

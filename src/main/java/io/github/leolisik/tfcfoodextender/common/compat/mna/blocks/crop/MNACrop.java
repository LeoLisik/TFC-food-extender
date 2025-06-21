package io.github.leolisik.tfcfoodextender.common.compat.mna.blocks.crop;

import io.github.leolisik.tfcfoodextender.common.blockentities.FEBlockEntities;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.Crop;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.DeadCropBlock;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.DefaultCropBlock;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.ICropLike;
import io.github.leolisik.tfcfoodextender.common.util.climate.ClimateRanges;
import net.dries007.tfc.common.blockentities.CropBlockEntity;
import net.dries007.tfc.common.blockentities.FarmlandBlockEntity.NutrientType;
import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.common.blocks.crop.WildCropBlock;
import net.dries007.tfc.util.climate.ClimateRange;
import net.minecraft.util.StringRepresentable;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.material.MapColor;

import java.util.Locale;
import java.util.function.Function;
import java.util.function.Supplier;

@SuppressWarnings("unused")
public enum MNACrop implements StringRepresentable, ICropLike {
    DESERT_NOVA(NutrientType.PHOSPHOROUS, 6),
    WAKEBLOOM(NutrientType.PHOSPHOROUS, 6),
    TARMA_ROOT(NutrientType.PHOSPHOROUS, 6),
    AUM(NutrientType.PHOSPHOROUS, 6),
    CERUBLOSSOM(NutrientType.PHOSPHOROUS, 6),
    ;

    private final String serializedName;
    private final NutrientType primaryNutrient;
    private final Supplier<Block> factory;
    private final Supplier<Block> deadFactory;
    private final Supplier<Block> wildFactory;

    MNACrop(NutrientType primaryNutrient, int singleBlockStages) {
        this(primaryNutrient, self -> DefaultCropBlock.create(crop(), singleBlockStages, self), self -> new DeadCropBlock(dead(), self.getClimateRange()), self -> new WildCropBlock(dead().randomTicks()));
    }

    MNACrop(NutrientType primaryNutrient, Function<MNACrop, Block> factory, Function<MNACrop, Block> deadFactory, Function<MNACrop, Block> wildFactory)
    {
        this.serializedName = name().toLowerCase(Locale.ROOT);
        this.primaryNutrient = primaryNutrient;
        this.factory = () -> factory.apply(this);
        this.deadFactory = () -> deadFactory.apply(this);
        this.wildFactory = () -> wildFactory.apply(this);
    }

    private static ExtendedProperties dead()
    {
        return ExtendedProperties.of(MapColor.PLANT).noCollission().randomTicks().strength(0.4F).sound(SoundType.CROP).flammable(60, 30);
    }

    private static ExtendedProperties crop()
    {
        return dead().blockEntity(FEBlockEntities.CROP).serverTicks(CropBlockEntity::serverTick);
    }

    @Override
    public String getSerializedName() {
        return serializedName;
    }

    public NutrientType getPrimaryNutrient()
    {
        return primaryNutrient;
    }

    public Supplier<ClimateRange> getClimateRange()
    {
        return ClimateRanges.CROPS.get(this);
    }

    public Block create()
    {
        return factory.get();
    }

    public Block createDead()
    {
        return deadFactory.get();
    }

    public Block createWild()
    {
        return wildFactory.get();
    }
}

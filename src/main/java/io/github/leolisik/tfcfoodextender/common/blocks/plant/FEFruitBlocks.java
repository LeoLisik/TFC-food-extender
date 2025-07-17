package io.github.leolisik.tfcfoodextender.common.blocks.plant;

import io.github.leolisik.tfcfoodextender.common.blockentities.FEBlockEntities;
import io.github.leolisik.tfcfoodextender.common.blocks.FEBlocks;
import io.github.leolisik.tfcfoodextender.common.items.FEItems;
import io.github.leolisik.tfcfoodextender.common.items.Food;
import io.github.leolisik.tfcfoodextender.common.util.climate.ClimateRanges;
import net.dries007.tfc.common.blockentities.BerryBushBlockEntity;
import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.common.blocks.plant.fruit.FruitTreeBranchBlock;
import net.dries007.tfc.common.blocks.plant.fruit.FruitTreeLeavesBlock;
import net.dries007.tfc.common.blocks.plant.fruit.Lifecycle;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.material.MapColor;

import java.awt.Color;
import java.util.function.Supplier;

import static net.dries007.tfc.common.blocks.plant.fruit.Lifecycle.*;

public final class FEFruitBlocks {
    public enum Tree {
        // TODO: Change color
        Apricot(FEItems.FOODS.get(Food.APRICOT), new Color(255, 255, 255).getRGB(), new Lifecycle[] {HEALTHY, HEALTHY, HEALTHY, FLOWERING, FLOWERING, FRUITING, DORMANT, DORMANT, DORMANT, DORMANT, DORMANT, HEALTHY}),;

        private final Supplier<Item> product;
        private final int color;
        private final Lifecycle[] stages;

        Tree(Supplier<Item> product, int color, Lifecycle[] stages) {
            this.product = product;
            this.color = color;
            this.stages = stages;
        }

        public Block createSapling() {
            return new FEFruitTreeSaplingBlock(ExtendedProperties.of().noCollission().randomTicks().strength(0).sound(SoundType.GRASS).blockEntity(FEBlockEntities.TICK_COUNTER).flammableLikeLeaves(), FEBlocks.FRUIT_TREE_GROWING_BRANCHES.get(this), 8, ClimateRanges.FRUIT_TREES.get(this), stages);
        }

        // TODO: Maybe add potted sapling
        /*public Block createPottedSapling() {

        }*/

        public Block createLeaves() {
            return new FEFruitTreeLeavesBlock(ExtendedProperties.of().mapColor(FruitTreeLeavesBlock::getMapColor).strength(0.5F).sound(SoundType.GRASS).randomTicks().noOcclusion().blockEntity(FEBlockEntities.BERRY_BUSH).serverTicks(BerryBushBlockEntity::serverTick).flammableLikeLeaves(), product, stages, ClimateRanges.FRUIT_TREES.get(this), color);
        }

        public Block createBranch() {
            return new FruitTreeBranchBlock(ExtendedProperties.of().mapColor(MapColor.WOOD).sound(SoundType.SCAFFOLDING).randomTicks().strength(1.0F).flammableLikeLogs(), ClimateRanges.FRUIT_TREES.get(this));
        }

        public Block createGrowingBranch() {
            return new FEGrowingFruitTreeBranchBlock(ExtendedProperties.of().mapColor(MapColor.WOOD).sound(SoundType.SCAFFOLDING).randomTicks().strength(1.0F).blockEntity(FEBlockEntities.TICK_COUNTER).flammableLikeLogs(), FEBlocks.FRUIT_TREE_BRANCHES.get(this), FEBlocks.FRUIT_TREE_LEAVES.get(this), ClimateRanges.FRUIT_TREES.get(this));
        }
    }
}

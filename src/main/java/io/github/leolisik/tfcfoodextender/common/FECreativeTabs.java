package io.github.leolisik.tfcfoodextender.common;

import io.github.leolisik.tfcfoodextender.TFCFoodExtender;
import io.github.leolisik.tfcfoodextender.common.items.FEItems;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.ItemLike;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;
import io.github.leolisik.tfcfoodextender.common.items.Food;

import java.util.function.Supplier;

public final class FECreativeTabs {
    public static final DeferredRegister<CreativeModeTab> CREATIVE_TABS = DeferredRegister.create(Registries.CREATIVE_MODE_TAB, TFCFoodExtender.MODID);
    public static final RegistryObject<CreativeModeTab> MAIN_TAB = register("main", () -> new ItemStack(FEItems.FOODS.get(Food.BUCKWHEAT).get()),  FECreativeTabs::fillFETab);

    private static RegistryObject<CreativeModeTab> register(String name, Supplier<ItemStack> icon, CreativeModeTab.DisplayItemsGenerator displayItems)
    {
        return CREATIVE_TABS.register(name, () -> CreativeModeTab.builder()
                .icon(icon)
                .title(Component.translatable("tfcfe.creative_tab." + name))
                .displayItems(displayItems)
                .build());
    }

    public static void fillFETab(CreativeModeTab.ItemDisplayParameters parameters, CreativeModeTab.Output out)
    {
        for (var food : FEItems.FOODS.values()) {
            accept(out, food);
        }
        for (var seed : FEItems.CROP_SEEDS.values()) {
            accept(out, seed);
        }
        for (var prepared_seed : FEItems.PREPARED_SEEDS.values()) {
            accept(out, prepared_seed);
        }
    }

    private static <T extends ItemLike, R extends Supplier<T>> void accept(CreativeModeTab.Output out, R reg)
    {
        out.accept(reg.get());
    }
}

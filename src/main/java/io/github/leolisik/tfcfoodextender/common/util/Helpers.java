package io.github.leolisik.tfcfoodextender.common.util;

import io.github.leolisik.tfcfoodextender.TFCFoodExtender;
import net.minecraft.resources.ResourceLocation;

import static net.dries007.tfc.util.Helpers.resourceLocation;

public final class Helpers
{
    public static ResourceLocation identifier(String name)
    {
        return resourceLocation(TFCFoodExtender.MODID, name);
    }
}
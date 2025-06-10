package io.github.leolisik.tfcfoodextender.common.util.climate;

import io.github.leolisik.tfcfoodextender.TFCFoodExtender;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.Crop;
import io.github.leolisik.tfcfoodextender.common.blocks.crop.ICropLike;
import io.github.leolisik.tfcfoodextender.common.compat.mna.blocks.crop.MNACrop;
import io.github.leolisik.tfcfoodextender.common.util.Helpers;
import net.dries007.tfc.util.RegisteredDataManager;
import net.dries007.tfc.util.climate.ClimateRange;

import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;
import java.util.function.Supplier;

import static net.dries007.tfc.util.Helpers.mapOfKeys;

@SuppressWarnings("unused")
public class ClimateRanges {
    public static final Map<ICropLike, Supplier<ClimateRange>> CROPS = new LinkedHashMap<>();


    static {
        CROPS.putAll(mapOfKeys(Crop.class, crop -> register("crop/" +crop.getSerializedName())));

        if (TFCFoodExtender.isMNALoaded) {
            CROPS.putAll(mapOfKeys(MNACrop.class, crop -> register("crop/" +crop.getSerializedName())));
        }
    }

    private static RegisteredDataManager.Entry<ClimateRange> register(String name)
    {
        return ClimateRange.MANAGER.register(Helpers.identifier(name.toLowerCase(Locale.ROOT)));
    }
}

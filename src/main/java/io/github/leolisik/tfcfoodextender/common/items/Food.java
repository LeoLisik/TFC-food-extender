package io.github.leolisik.tfcfoodextender.common.items;

import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;

@SuppressWarnings("unused")
public enum Food {
    BUCKWHEAT;

    private final boolean meat;
    private final boolean fast;
    private final boolean fruit;

    Food()
    {
        this(false, false, false);
    }

    Food(boolean meat, boolean fast)
    {
        this(meat, fast, false);
    }

    Food(boolean meat, boolean fast, boolean fruit)
    {
        this.meat = meat;
        this.fast = fast;
        this.fruit = fruit;
    }

    public boolean isFruit()
    {
        return fruit;
    }

    public FoodProperties getFoodProperties() {
        FoodProperties.Builder builder = new FoodProperties.Builder();
        if (meat) builder.meat();
        if (fast) builder.fast();
        return builder.nutrition(4).saturationMod(0.3f).build();
    }

    public Item.Properties createProperties()
    {
        return new Item.Properties().food(getFoodProperties());
    }
}

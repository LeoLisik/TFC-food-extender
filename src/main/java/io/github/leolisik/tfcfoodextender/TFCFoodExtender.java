package io.github.leolisik.tfcfoodextender;

import com.mojang.logging.LogUtils;
import io.github.leolisik.tfcfoodextender.common.FECreativeTabs;
import io.github.leolisik.tfcfoodextender.common.blockentities.FEBlockEntities;
import io.github.leolisik.tfcfoodextender.common.blocks.FEBlocks;
import io.github.leolisik.tfcfoodextender.common.items.FEItems;
import net.minecraft.client.Minecraft;
import net.minecraft.client.renderer.ItemBlockRenderTypes;
import net.minecraft.client.renderer.RenderType;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.ModList;
import net.minecraftforge.fml.ModLoadingContext;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.config.ModConfig;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import org.slf4j.Logger;

@Mod(TFCFoodExtender.MODID)
public class TFCFoodExtender
{
    public static final String MODID = "tfcfe";
    private static final Logger LOGGER = LogUtils.getLogger();
    //public static final boolean isMNALoaded = ModList.get().isLoaded("mna");
    public static final boolean isMNALoaded = true;

    @SuppressWarnings("removal")
    public TFCFoodExtender() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();

        FEItems.ITEMS.register(modEventBus);
        FEBlocks.BLOCKS.register(modEventBus);
        FEBlockEntities.BLOCK_ENTITIES.register(modEventBus);
        FECreativeTabs.CREATIVE_TABS.register(modEventBus);

        modEventBus.addListener(this::commonSetup);

        MinecraftForge.EVENT_BUS.register(this);

        ModLoadingContext.get().registerConfig(ModConfig.Type.COMMON, Config.SPEC);
    }

    private void commonSetup(final FMLCommonSetupEvent event)
    {
        // Some common setup code
        LOGGER.info("HELLO FROM COMMON SETUP");

        if (Config.logDirtBlock)
            LOGGER.info("DIRT BLOCK >> {}", ForgeRegistries.BLOCKS.getKey(Blocks.DIRT));

        LOGGER.info(Config.magicNumberIntroduction + Config.magicNumber);

        Config.items.forEach((item) -> LOGGER.info("ITEM >> {}", item.toString()));
    }

    // You can use SubscribeEvent and let the Event Bus discover methods to call
    @SubscribeEvent
    public void onServerStarting(ServerStartingEvent event)
    {
        // Do something when the server starts
        LOGGER.info("HELLO from server starting");
    }

    // You can use EventBusSubscriber to automatically register all static methods in the class annotated with @SubscribeEvent
    @Mod.EventBusSubscriber(modid = MODID, bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
    public static class ClientModEvents
    {
        @SubscribeEvent
        @SuppressWarnings("removal")
        public static void onClientSetup(FMLClientSetupEvent event)
        {
            event.enqueueWork(() -> {
                for (RegistryObject<Block> crop : FEBlocks.CROPS.values()) {
                    ItemBlockRenderTypes.setRenderLayer(crop.get(), RenderType.cutout());
                }
                for (RegistryObject<Block> crop : FEBlocks.WILD_CROPS.values()) {
                    ItemBlockRenderTypes.setRenderLayer(crop.get(), RenderType.cutout());
                }
                for (RegistryObject<Block> crop : FEBlocks.DEAD_CROPS.values()) {
                    ItemBlockRenderTypes.setRenderLayer(crop.get(), RenderType.cutout());
                }
            });
            // Some client setup code
            LOGGER.info("HELLO FROM CLIENT SETUP");
            LOGGER.info("MINECRAFT NAME >> {}", Minecraft.getInstance().getUser().getName());
        }
    }
}
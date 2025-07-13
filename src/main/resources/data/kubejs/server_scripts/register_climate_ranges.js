ServerEvents.onEvent('tfc:register_climate_ranges', event => {
  event.climateRange(climate => {
    climate.minTemperature(-20)
    climate.maxTemperature(50)
    climate.minHydration(1)
    climate.maxHydration(400)
    climate.maxForest(2)
  }, 'tfcfe:wild_crop/buckwheat')
})
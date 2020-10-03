<template>
  <div>
    <tile-metric
      :title="title"
      :value="value"
      :difference="difference"
      :icon="icon"
      :colour="colour"
    />
  </div>
</template>

<script>
import TileMetricLoading from './TileMetricLoading.vue'
import TileMetricError from './TileMetricError.vue'

const TileMetric = () => ({
  component: import('./TileMetricDefault.vue'),
  delay: 100,
  timeout: 3000,
  loading: TileMetricLoading,
  error: TileMetricError,
})
export default {
  components: {
    TileMetric,
  },
  props: {
    title: {
      type: String,
      default: '',
    },
    value: {
      type: Number,
      default: 0,
    },
    difference: {
      type: Number,
      default: 0,
    },
    icon: {
      type: String,
      default: '',
    },
    colour: {
      type: String,
      default: '',
    },
  },
}
</script>

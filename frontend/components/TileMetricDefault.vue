<template>
  <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
    <div
      class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
    >
      <div class="flex-auto p-4">
        <div class="flex flex-wrap">
          <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
            <h5 class="text-gray-500 uppercase font-bold text-xs">
              {{ title }}
            </h5>
            <span class="font-semibold text-xl text-gray-800">
              {{ value }}
            </span>
          </div>
          <div class="relative w-auto pl-4 flex-initial">
            <div
              class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full"
              :class="colour"
            >
              <i :class="icon" />
            </div>
          </div>
        </div>
        <p class="text-sm text-gray-500 mt-4">
          <template v-if="difference > 0">
            <span class="text-green-500 mr-2">
              <i class="fas fa-angle-up" /> {{ difference }}
            </span>
          </template>
          <template v-else-if="difference == 0">
            <span class="text-grey-500 mr-2">
              <i class="fas fa-angle-right" /> {{ difference }}
            </span>
          </template>
          <template v-else>
            <span class="text-red-500 mr-2">
              <i class="fas fa-angle-down" /> {{ difference }}
            </span>
          </template>
          <span class="whitespace-no-wrap"> Since last month. </span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.min.css'

export default {
  props: {
    title: {
      type: String,
      default: 'Metric',
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
      default: 'fas fa-percent',
    },
    colour: {
      type: String,
      default: 'bg-grey-300',
    },
  },
}
</script>

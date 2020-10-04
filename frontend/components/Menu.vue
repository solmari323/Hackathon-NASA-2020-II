<template>
  <div class="p-4 menu">
    <div class="close w-full flex justify-end">
      <img
        class="h-6 w-6 m-4"
        src="./../assets/img/close.svg"
        @click="this.$emit('close')"
      />
    </div>
    <div
      v-if="upPrograms.length + currPrograms.length > 0"
      class="mission-list overflow-auto"
    >
      <div v-for="c_program in currPrograms" :key="c_program.id">
        <program-tile
          :current="true"
          :name="c_program.name"
          :type="c_program.type"
          :start-date="c_program.startDate"
          :end-date="c_program.endDate"
        />
      </div>
      <p class="ml-4 uppercase text-secondary">Upcoming Programs</p>
      <hr class="ml-4" />
      <div
        v-for="program in upPrograms"
        :key="program.id"
        class="upcoming-programs"
      >
        <program-tile
          :current="false"
          :name="program.name"
          :type="program.type"
          :start-date="program.startDate"
          :end-date="program.endDate"
        />
      </div>
    </div>
    <div v-else class="h-full flex justify-center">
      <p class="text-secondary text-center mt-6">
        You currently have no programs. Try creating one!
      </p>
    </div>
    <div class="absolute bottom-0 right-0 m-4">
      <img src="./../assets/img/add.svg" alt="" />
    </div>
  </div>
</template>

<script>
import ProgramTile from './ProgramTile.vue'
export default {
  name: 'Menu',
  components: { ProgramTile },
  props: {
    upPrograms: {
      type: Array,
      default: () => [],
    },
    currPrograms: {
      type: Array,
      default: () => [],
    },
  },
}
</script>

<style scoped>
.menu {
  height: 100%;
  width: 90vw;
  position: absolute;
  right: 0;
  overflow: hidden;
  box-shadow: -3px 0 5px #38383823;
}

.mission-list {
  height: 95%;
}
</style>

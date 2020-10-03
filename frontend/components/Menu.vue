<template>
  <div class="p-4 menu">
    <div class="close w-full flex justify-end">
      <img class="h-6 w-6 m-4" src="./../assets/img/close.svg" alt="" />
    </div>
    <div v-if="programs.length > 0" class="">
      <program-tile
        :current="current"
        name="Crew Dragon 2"
        type="Space Mission"
        startDate="25 Sep 2020"
        endDate="02 Jan 2020"
      />
      <p class="ml-4 uppercase text-secondary">Upcoming Programs</p>
      <hr class="ml-4" />
      <div
        v-for="program in programs"
        :key="program.id"
        class="upcoming-programs"
      >
        <program-tile
          :current="false"
          :name="program.name"
          :type="program.type"
          :startDate="program.startDate"
          :endDate="program.endDate"
        />
      </div>
    </div>
    <div v-else class="h-full flex justify-center">
      <p class="text-secondary text-center mt-6">
        You currently have no programs. Try creating one!
      </p>
    </div>
  </div>
  
</template>

<script>
import ProgramTile from './ProgramTile.vue'
export default {
  name: 'Menu',
  components: { ProgramTile },
  props: {
    programs: {
      type: Array,
      default() {
        return []
      },
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
  box-shadow: -3px 0 5px #38383823;
}
</style>

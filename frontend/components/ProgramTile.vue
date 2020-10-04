<template>
  <div class="tile flex flex-row items-center ml-4 my-4">
    <div class="grad bg-gradient-to-br from-primary-light to-primary"></div>
    <div class="mission-info my-4 ml-6">
      <p
        v-if="current"
        class="text-sm font-bold text-primary-light mb-1 uppercase"
      >
        Current Mission
      </p>
      <p class="text-xl font-bold text-black">{{ name }},</p>
      <p class="text-xl -mt-1 font-light text-secondary">{{ type }}</p>
      <p class="text-xs mt-1 font-bold text-primary">
        {{ startDate + ' - ' + endDate }}
      </p>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ProgramTile',
  props: {
    current: { type: Boolean, default: false },
    name: { type: String, default: '' },
    type: { type: String, default: '' },
    startDate: { type: String, default: '' },
    endDate: { type: String, default: '' },
  },
}
</script>

<style scoped>
.grad {
  height: 7em;
  width: 12px;
  background: rgb(246, 114, 60);
  background: linear-gradient(
    -45deg,
    rgba(246, 114, 60, 1) 0%,
    rgba(254, 172, 138, 1) 100%
  );
  border-radius: 50px;
}
</style>

<template>
  <div>
    <div class="flex justify-between p-8 pb-2">
      <p class="text-4xl font-bold text-black">
        {{ dates[currDate].dow }},
        <span class="text-gray-500 font-light">{{ dates[currDate].do }}</span>
      </p>
      <img class="" src="./../assets/img/menu.svg" alt="" />
    </div>
    <div class="flex w-full h-28 pl-8 overflow-x-auto">
      <div
        v-for="date in dates"
        :key="date.id"
        class="w-20 h-24 flex flex-shrink-0 flex-col justify-center items-center rounded mr-4"
        :class="{
          'bg-gradient-to-br from-primary-light to-primary':
            date.id == currDate,
        }"
        @click="currDate = date.id"
      >
        <p
          class="text-s font-regular"
          :class="{
            'text-black': date.id != currDate,
            'text-white': date.id == currDate,
          }"
        >
          {{ date.dow }}
        </p>
        <p
          class="text-2xl font-medium"
          :class="{
            'text-black': date.id != currDate,
            'text-white': date.id == currDate,
          }"
        >
          {{ date.dn }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NavigationDaily',
  data() {
    return {
      currDate: 0,
      dates: [],
    }
  },
  created() {
    for (let i = 0; i < 8; i++) {
      const temp = {
        id: i,
        date: this.$moment().add(i, 'd'),
        dow: this.$moment().add(i, 'd').format('ddd'),
        do: this.$moment().add(i, 'd').format('Do'),
        dn: this.$moment().add(i, 'd').format('DD'),
      }
      this.dates.push(temp)
    }
  },
}
</script>

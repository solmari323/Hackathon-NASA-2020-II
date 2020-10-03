<template>
  <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
    <div
      class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
    >
      <div class="flex-auto p-4">
        <div class="flex flex-wrap">
          <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
            <h5 class="text-gray-500 uppercase font-bold text-xs">
              <span class="skeleton-box h-3 w-32 inline-block"></span>
            </h5>
            <span class="font-semibold text-xl text-gray-800">
              <span class="skeleton-box h-4 w-16 inline-block"></span>
            </span>
          </div>
          <div class="relative w-auto pl-4 flex-initial">
            <div
              class="skeleton-box text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full bg-gray-300"
            >
              <i class="fas"></i>
            </div>
          </div>
        </div>
        <p class="text-sm text-gray-500 mt-4">
          <span class="text-green-500 mr-2">
            <span class="skeleton-box h-3 w-2 inline-block"></span>
            <span class="skeleton-box h-3 w-4 inline-block mr-2"></span>
            <span class="skeleton-box h-3 w-32 inline-block"></span>
          </span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

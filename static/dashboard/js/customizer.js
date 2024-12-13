const layouts = ["vertical", "two-column", "hovered", "detached", "horizontal"];
const customizerComponent = `<button
  id="customizer-btn"
  class="fixed ltr:right-4 rtl:left-4 z-50 top-1/2 bg-primary text-n0 w-10 h-10 rounded-full flex items-center justify-center">
  <i class="las la-cog animate-spin-slow"></i>
</button>
<div class="z-[60] duration-500 ltr:right-0 rtl:left-0" id="customizer-wrapper">  
  <aside
    id="customizer"
    class="w-[280px] xxxl:w-[336px] shadow-sm z-[52] duration-300 fixed ltr:right-0 rtl:left-0 h-full bg-n0 dark:bg-bg4 top-0 customizer-hide overflow-y-auto">
    <div
      class="p-4 flex justify-between items-center border-b border-n30 dark:border-n500">
      <div>
        <h5 class="h5 mb-2">Theme customizer</h5>
        <p class="text-sm">Customize &amp; Preview in Real Time</p>
      </div>
      <button id="customizer-close-btn">
        <i class="las la-times"></i>
      </button>
    </div>
    <div class="p-4 border-b border-n30 dark:border-n500">
      <span class="mb-3 text-n60 block text-sm">Themeing</span>
      <h6 class="h6 mb-3">Mode</h6>
      <div class="flex gap-4">
        <button
          class="flex items-center gap-2 px-3 py-2 rounded-lg border border-n30 dark:border-n500"
          id="light-btn">            
          <i class="las la-sun"></i>
          <span>Light </span>
        </button>
        <button
          class="flex items-center gap-2 px-3 py-2 rounded-lg border border-n30 dark:border-n500"
          id="dark-btn">              
          <i class="las la-moon"></i>
          <span>Dark </span>
        </button>
      </div>
    </div>
    <div class="p-4 border-b border-n30 dark:border-n500">
      <span class="mb-3 text-n60 block text-sm">Layout</span>
      <h6 class="h6 mb-3">Direction</h6>
      <div class="flex gap-4 mb-6">
        <button
          class="flex items-center gap-2 px-4 py-2 rounded-lg ltr:bg-primary ltr:text-n0 bg-transparent border ltr:border-n30 dark:border-n500"
          onclick="setLtr()">
          <span>LTR</span>
        </button>
        <button
          class="flex items-center gap-2 px-3 py-2 rounded-lg rtl:bg-primary rtl:text-n0 border border-n30 dark:border-n500"
          onclick="setRtl()">
          <span>RTL</span>
        </button>
      </div>
      <h6 class="h6 mb-3">Sidebar</h6>
      <div class="flex gap-4 flex-wrap" id="layout-container">
        ${layouts
          .map(
            (layout) =>
              `<button class="border border-n30 dark:border-n500 capitalize rounded-lg px-4 py-2 layout-btn">${layout}</button>`
          )
          .join("")}
      </div>
    </div>
  </aside>
</div>`;

const customizerContainer = document.getElementById("customizer-container");

// Set the innerHTML of the container to your customizer HTML string
if (customizerContainer) {
    customizerContainer.innerHTML = customizerComponent;
}
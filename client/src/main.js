import Vue from 'vue'
import App from './App.vue'

//import VueNativeSock from 'vue-native-websocket'
import VueApexCharts from 'vue-apexcharts'

import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
//Vue.use(VueNativeSock, 'ws://localhost:8000/traffic/ELTX73001122',{ format: 'json' })
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

<template>
  <v-app>
    <v-card>
    <v-tabs
      background-color="deep-purple accent-4"
      center-active
      dark
    >
      <v-tab @click=" () => { this.$router.push({name:'Gpon'})}">GPON</v-tab>
      <v-tab @click=" () => { this.$router.push('About')}">Information ports on switch</v-tab>
    </v-tabs>
  </v-card>
    <v-main>
      <router-view/>
    </v-main>
    <v-footer padless dark>
    <v-col
      class="text-center"
      cols="12"
    >
      2022 — <strong>Chinya</strong>
    </v-col>
  </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

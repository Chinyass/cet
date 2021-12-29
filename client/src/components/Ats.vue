<template>
  <v-container fluid>
    <v-checkbox
      v-model="selected"
      :label="name"
      :value="name"
      @click="uncover"
    ></v-checkbox>
  </v-container>
</template>

<script>
export default {
    name:'Ats',
    props:{
        name : String
    },
    data: () => ({
         selected: [],
    }),
    methods: {
        uncover(){
            console.log(this.selected)
        }
    },
}
</script>
<style scoped>

</style>
<template>
    <v-container>
        <v-container fluid>
            <ul>
                <li v-for="name in ats" :key="name">
                    <v-checkbox
                    v-model="selected_ats"
                    :label="name"
                    :value="name"
                    @click="uncover_ats"
                    >
                    </v-checkbox>
                    <ul>
                    </ul>
                </li>
            </ul>
        </v-container>
    </v-container>
</template>

<script>
export default {
    name: 'Gpon',
    data: () => ({
         selected_ats: [],
         selected_olt: [],
         ats: ['ATC-3','ATC-6'],
         olt: ['10.3.0.26','10.6.0.5']
    }),
    methods: {
        uncover_ats(){
            console.log(this.selected_ats)
        },
        uncover_olt(){
            console.log(this.selected_olt)
        }
    },
}
</script>
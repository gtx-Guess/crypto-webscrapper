<template>
    <div>
        <button @click="refreshData">Refresh Crypto Data</button><br><br><br>
        <table>
            <tr>
                <th v-for="header in crypto_headers">{{ header }}</th>
            </tr>
            <tr v-for="row in crypto_data">
                <td v-for="item in row">{{ item }}</td>
            </tr>
        </table>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
const BASE_URL = import.meta.env.VITE_SERVER_URL;
const crypto_headers = ref('');
const crypto_data = ref('');

(async () => {
    try{
        const resp = await axios.get(BASE_URL);
        console.log(resp);
        crypto_headers.value = resp.data[0];
        crypto_data.value = resp.data[1];
    }catch(error){
        console.log(error.response);
    };

})();

async function refreshData(){
    try{
        const resp = await axios.get(BASE_URL);
        console.log(resp);
        crypto_headers.value = resp.data[0];
        crypto_data.value = resp.data[1];
    }catch(error){
        console.log(error.response);
    };
};

</script>

<style scoped>
th, td{
    padding: 12px;
}
th, td{
    border: 1px solid black;
}
button{
    background: rgba(191, 191, 191, 0.486);
}

</style>

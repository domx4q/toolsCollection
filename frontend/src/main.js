import {createApp} from 'vue'
import './style.css'
import App from './App.vue'

import axios from 'axios'
import VueAxios from 'vue-axios'

import { plugin, defaultConfig } from '@formkit/vue'
import { de } from '@formkit/i18n'
import './assets/formkit.css'
const config = {
    locales: { de },
    locale: 'de',
    theme: 'genesis',
}

const app = createApp(App);
app.use(VueAxios, axios);
app.provide('axios', app.config.globalProperties.axios);
app.use(plugin, defaultConfig(config));
app.mount('#app');
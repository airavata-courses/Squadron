import Vue from 'vue';

import { store } from './_store';
import { router } from './_helpers';
import App from './app/App';
import VueRouter from 'vue-router';

window.axios=require('axios');
Vue.use(VueRouter);
import { ValidationProvider } from 'vee-validate';
Vue.component('ValidationProvider', ValidationProvider);
// setup fake backend
import { configureFakeBackend } from './_helpers';
configureFakeBackend();

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
});

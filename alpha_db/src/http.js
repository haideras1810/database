import axios from 'axios';
// import {store} from '@/store.js';
export const axiosInstance = axios.create({
    baseURL:'http://localhost:8000/api/',
    timeout: 1000,
    headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type':'application/json',

    }
});
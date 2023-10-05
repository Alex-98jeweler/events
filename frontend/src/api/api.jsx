import axios from "axios";

export const baseUrl = "http://127.0.0.1:8000"

const $api = axios.create({
    // withCredentials: true,
    baseURL: baseUrl,
})

$api.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem('jwt_token')}`
    return config;
})


$api.interceptors.response.use((config) => {
    return config;
},async (error) => {
    const originalRequest = error.config;
    if (error.response.status == 401 && error.config && !error.config._isRetry) {
        originalRequest._isRetry = true;
        try {
            const response = await axios.post(`${baseUrl}/api/v1/auth/jwt/refresh`, {"refresh": localStorage.getItem('refresh')})
            localStorage.setItem('jwt_token', response.data.access);
            return $api.request(originalRequest);
        } catch (e) {
            console.log('НЕ АВТОРИЗОВАН')
        }
    }
    throw error;
})

export default $api;

import $api from "../api/api";



export default class UserService {

    constructor() {
        makeAutoObservable(this);
    }

    async  getList() {
        const response = await $api.get('/api/v1/users/')
        return response.data.result
    }

    async getUserById(id) {
        const response = await $api.get(`/api/v1/users/${id}/`)
        return response.data.result
    }

    static async getUserMe() {
        const response = await $api.get(`/api/v1/users/me/`)
        return response.data.result
    }

}
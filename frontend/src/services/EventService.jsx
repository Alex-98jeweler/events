import axios from "axios";
import $api from "../api/api";
import { makeAutoObservable } from "mobx";


export default class EventService {

    constructor() {
        makeAutoObservable(this);
    }

    async getList() {
        const resp = await $api.get('/api/v1/event')
        return resp.data.result
    }

    async getDetail(id) {
        const resp = await $api.get(`/api/v1/event/${id}`)
        return resp.data.result
    }
}
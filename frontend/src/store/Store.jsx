import axios from "axios";
import AuthService from "../services/AuthService";
import UserService from "../services/UserService";
import { baseUrl } from "../api/api";
import { makeAutoObservable } from "mobx";


export default class Store {
    user = {};
    isAuth = false;
    isLoading = false;

    constructor() {
        makeAutoObservable(this);
    }

    setAuth(bool) {
        this.isAuth = bool;
    }

    setUser(user) {
        this.user = user;
    }

    setLoading(bool) {
        this.isLoading = bool;
    }

    async login(username, password) {
        try {
            console.log('here')
            const response = await AuthService.login(username, password);
            console.log(response)
            localStorage.setItem('jwt_token', response.access);
            localStorage.setItem('refresh', response.refresh);
            this.setAuth(true);
            const user = await UserService.getUserMe();
            console.log(user)
            this.setUser(user);
        } catch (e) {
            console.log(e)
        }   
    }

    async registration(username, password, first_name, last_name, birthday) {
        try {
            const response = await AuthService.registration(username, password, first_name, last_name, birthday)
            console.log(response);
            this.login(username, password);
        } catch(e) {
            console.log(e)
        }
    }

    async logout() {
        localStorage.removeItem('jwt_token');
        localStorage.removeItem('refresh');
        this.setAuth(false);
        this.setUser({})
    }

    async checkAuth() {
        this.setLoading(true);
        try {
            var data = {"refresh": localStorage.getItem('refresh')};
            const response = await axios.post(
                `${baseUrl}/api/v1/auth/jwt/refresh/`, 
                data
            )
            localStorage.setItem('jwt_token', response.data.result.access)
            this.setAuth(true);
            // const user = await UserService.getUserMe()
            // this.setUser(user)
        } catch(e) {
            console.log(e);
        } finally {
            this.setLoading(false);
        }
    }
}
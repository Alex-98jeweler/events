import axios from "axios";
import { baseUrl } from "../api/api";


export default class AuthService {

    static async login(username, password) {
        const response = await axios.post(`${baseUrl}/api/v1/auth/jwt/create/`, {username, password})
        return response.data.result
    }

    static async registration(
        username, 
        password,
        first_name,
        last_name,
        birthday) 
        {
            const response = await axios.post(`${baseUrl}/api/v1/users/`, {username, password, first_name, last_name, birthday})
            return response.data.result
        }
    
    static async logout() {

    }

}
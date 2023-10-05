import { useParams } from "react-router-dom";
import UserService from "../../services/UserService";
import { useEffect, useState } from "react";


const UserDetail = () => {
    const {id} = useParams();
    const [user, setUser] = useState({})
    const userService = new UserService();

    const fetchUser = async () => {
        const data = await userService.getUserById(id)
        setUser(data)
    }

    useEffect(
        () => {
            fetchUser()
        },
        []
    )

    return (
        <div>
            <h2>Имя</h2>
            <p>{user.first_name}</p>
            <h2>Фамилия</h2>
            <p>{user.last_name}</p>

        </div>
    )


}

export default UserDetail;
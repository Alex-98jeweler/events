import { Link } from "react-router-dom";
import UserService from "../../services/UserService";
import { useEffect, useState } from "react";



const UserList = () => {
    const [users, setUsers] = useState([])
    const userService = new UserService();

    const fetchUsers = async () => {
        const data = await userService.getList()
        setUsers(data)
    }

    useEffect(
        () => {
            fetchUsers()
        },
        []
    )

    return (
        <div>
            <ul>
                {users.map((user => <li key={user.id}><Link to={`${user.id}`}>{user.first_name} {user.last_name}</Link></li>))}
            </ul>
        </div>
    )


}

export default UserList;
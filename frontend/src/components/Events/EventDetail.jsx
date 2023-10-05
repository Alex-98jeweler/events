import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import EventService from "../../services/EventService";
import { observer } from "mobx-react-lite";



const EventDetail = () => {
    const { id } = useParams();
    const [event, setEvent] = useState({});
    const [followers, setFollowers] = useState([])

    const eventService = new EventService();

    async function getEvent() {
        const data = await eventService.getDetail(id);
        setEvent(data);
        setFollowers(data.followers)
    }

    useEffect(() => {
        getEvent()
    }, [])
    return (
        <div>
            <h1>{event.title}</h1>
            <p>{event.description}</p>
            <h2>Участники</h2>
            <ul>
                {followers.length > 0 ? followers.map(
                    follower => <li key={follower.id}>
                        <Link to={`/users/${follower.id}`}>
                            {follower.first_name} {follower.last_name}
                        </Link>
                    </li>
                    )
                 : <li>Участников нету</li>}
            </ul>
        </div>
    )
}

export default observer(EventDetail);
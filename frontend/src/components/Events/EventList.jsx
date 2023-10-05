import axios from "axios";
import { useState, useEffect} from "react";
import { baseUrl } from "../../api/api";
import EventService from "../../services/EventService";
import { Link } from "react-router-dom";
import { observer } from "mobx-react-lite";


function EventList() {

    const [events, setEvents] = useState([]);

    const eventService = new EventService();

    const fetchData = async () => {
        const data = await eventService.getList()
        setEvents(data)
        console.log('here')
    }

    useEffect(() => {
        fetchData();
    }, [])

    return (
        <div>
            <h2>Все события</h2>
            <ul>{events.map(event=> <li key={event.id}><Link to={`${event.id}`}>{event.title}</Link></li>)}</ul>
        </div>
    )
}

export default observer(EventList);
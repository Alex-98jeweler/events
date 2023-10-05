import { Link } from "react-router-dom";



export default function HeaderList() {
    return (
        <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li><Link to="/" className="nav-link px-2 link-secondary">Главная</Link></li>
            <li><Link to="/events" className="nav-link link-body-emphasis">Все события</Link></li>
            <li><Link to="/my-events" className="nav-link link-body-emphasis">Мои события</Link></li>
        </ul>
    )
}
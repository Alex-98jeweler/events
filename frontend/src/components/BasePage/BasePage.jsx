import { Outlet } from "react-router-dom"
import HeaderList from "./HeaderList"
import { useContext } from "react"
import { Context } from "../../main"

export const BasePage = () => {
    const {store} = useContext(Context)

    return (
        <>
        <header className="p-3 mb-3 border-bottom">
            <div className="container">
            <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
                <a href="/" className="d-flex align-items-center mb-2 mb-lg-0 link-body-emphasis text-decoration-none">
                <img src="/bootstrap-logo.svg" alt="" width={40} height={32}/>
                </a>

                <HeaderList />

                <div className="dropdown text-end">
                <a href="#" className="d-block link-body-emphasis text-decoration-none dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                    <img src="https://github.com/mdo.png" alt="mdo" width="32" height="32" className="rounded-circle"/>
                </a>
                <ul className="dropdown-menu text-small">
                    <li><a className="dropdown-item" href="/my-profile">Мой профиль</a></li>
                    <li><hr className="dropdown-divider"/></li>
                    <li><a className="dropdown-item" href="/" onClick={(e) => {e.preventDefault();store.logout()}}>Выйти</a></li>
                </ul>
                </div>
            </div>
            </div>
        </header>
        <main>
            <Outlet />
        </main>
        <footer className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
            <div className="col-md-4 d-flex align-items-center">
                <a href="/" className="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
                    <svg className="bi" width="30" height="24"><use xlinkHref="#bootstrap"></use></svg>
                </a>
                <span className="mb-3 mb-md-0 text-body-secondary">© 2023 Alex Zubakin</span>
            </div>

            <ul className="nav col-md-4 justify-content-end list-unstyled d-flex">
                <li className="ms-3"><a className="text-body-secondary" href="#"><img src="/vk.png" alt="" /></a></li>
                <li className="ms-3"><a className="text-body-secondary" href="#"><img src="/youtube.png" alt="" /></a></li>
            </ul>
        </footer>
        </>
    )
}
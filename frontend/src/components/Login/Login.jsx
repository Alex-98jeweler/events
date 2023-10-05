import { useContext, useState } from "react"
import { Context } from "../../main"
import { observer } from "mobx-react-lite";



function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const {store} = useContext(Context);

    return (
        <div className="form-signin">
            <form>
                <h1 className="h3 mb-3 fw-normal"></h1>

                <div className="form-floating">
                    <input 
                        type="username"
                        className="form-control"
                        id="floatingInput"
                        placeholder="name@example.com"
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <label htmlFor="floatingInput">Логин</label>
                </div>
                <div className="form-floating">
                    <input 
                        type="password"
                        className="form-control"
                        id="floatingPassword"
                        placeholder="Password"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <label htmlFor="floatingPassword">Пароль</label>
                </div>
                <button onClick={(e) => {e.preventDefault();store.login(username, password)}}>
                    Войти
                </button>
            </form>
        </div>
        
   
    )
}

export default observer(Login);
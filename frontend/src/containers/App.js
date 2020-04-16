import React from "react"
import Alert from "react-s-alert"
import { Route, Switch, withRouter } from "react-router"
import { BrowserRouter } from "react-router-dom"
import "react-s-alert/dist/s-alert-default.css"
import LandingPage from "./LandingPage"


const style = {
    main: {
        padding: "10px",
    },
}

const InsideApp = withRouter(() => (
    <div>
        <Alert stack={{ limit: 3 }} html />
        <div style={style.main}>
            <Switch>
                <Route path="/" exact component={LandingPage} />
            </Switch>
        </div>
    </div>
))

const App = () => (
    <BrowserRouter>
        <InsideApp />
    </BrowserRouter>
)

export default App

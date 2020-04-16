import React from "react"
import Alert from "react-s-alert"
import { Route, Switch, withRouter } from "react-router"
import { BrowserRouter } from "react-router-dom"
import { LoginWrapper, UserManager, PermissionCheck } from "@ibmau/react-authentication"
import { DataSetManager } from "@ibmau/react-datasets"
import { ContentManager } from "@ibmau/react-content"
import "react-s-alert/dist/s-alert-default.css"
import LandingPage from "./LandingPage"


const style = {
    main: {
        maxWidth: "1280px",
        margin: "auto",
        padding: "30px",
    },
}

const InsideApp = withRouter(props => (
    <div>
        <Alert stack={{ limit: 3 }} html />
        <div style={style.main}>
            <Switch>
                <Route path="/" exact component={LandingPage} />
                <Route
                    path="/admin/user"
                    exact
                    component={() => (
                        <PermissionCheck currentUser={props.currentUser} requiredPermissions="admin" showError>
                            <UserManager currentUser={props.currentUser} isW3 permissions={["data", "content"]} />
                        </PermissionCheck>
                    )}
                />
                <Route
                    path="/admin/data"
                    exact
                    component={() => (
                        <PermissionCheck currentUser={props.currentUser} requiredPermissions="data" showError>
                            <DataSetManager
                                currentUser={props.currentUser}
                                assignments={{
                                    assignmentKey1: {
                                        label: "Assignment Object #1",
                                        dataTypes: ["type1", "type2", "type3"],
                                    },
                                }}
                            />
                        </PermissionCheck>
                    )}
                />
                <Route
                    path="/admin/content"
                    exact
                    component={() => (
                        <PermissionCheck currentUser={props.currentUser} requiredPermissions="content" showError>
                            <ContentManager
                                currentUser={props.currentUser}
                                references={["demo1", "demo2"]}
                                contentTypes={{
                                    description: {
                                        list: false,
                                        fields: ["title", "description"],
                                    },
                                    team: {
                                        list: true,
                                        fields: ["name", "role"],
                                    },
                                }}
                            />
                        </PermissionCheck>
                    )}
                />
            </Switch>
        </div>
    </div>
))

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            currentUser: null,  // stores currently logged in user
        }
        this.setUser = this.setUser.bind(this)  // handler for post-login
    }

    setUser(user) {
        // log-in successful, update this component's currentUser state
        this.setState({
            currentUser: user,
        })
    }

    render() {
        return (
            <BrowserRouter>
                <LoginWrapper setUser={this.setUser} isW3>
                    <InsideApp currentUser={this.state.currentUser} />
                </LoginWrapper>
            </BrowserRouter>
        )
    }
}

export default App

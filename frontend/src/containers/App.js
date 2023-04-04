import React from "react"
import { Route } from "react-router"
import { RouterProvider, createBrowserRouter, createRoutesFromElements } from "react-router-dom"
import LandingPage from "./LandingPage"


const style = {
    main: {
        padding: "10px",
    },
}

const App = () => (
    <div>
        <div style={style.main}>
            <RouterProvider router={createBrowserRouter(
                createRoutesFromElements(
                    <Route path="/" element={<LandingPage />}>
                    </Route>
                )
            )} />
        </div>
    </div>
)

export default App

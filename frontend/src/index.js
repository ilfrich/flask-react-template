import React from "react"
import { library } from "@fortawesome/fontawesome-svg-core"
import {
    faTrashAlt,
    faEdit,
    faCog,
    faSyncAlt,
    faChevronDown,
    faChevronRight,
    faDownload,
    faCheck,
    faTimes,
} from "@fortawesome/free-solid-svg-icons"
import { createRoot } from "react-dom/client"
import App from "./containers/App"

// configure fontawesome
const icons = [faTrashAlt, faEdit, faCog, faSyncAlt, faChevronDown, faChevronRight, faDownload, faCheck, faTimes]
icons.forEach(icon => {
    library.add(icon)
})

createRoot(document.getElementById("root")).render(
    <App />
)

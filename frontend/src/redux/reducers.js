import { combineReducers } from "redux"
import { ExampleReducer } from "./example"

// register all reducers for the various store spaces
export const rootReducer = combineReducers({
    example: ExampleReducer,
})

export default rootReducer

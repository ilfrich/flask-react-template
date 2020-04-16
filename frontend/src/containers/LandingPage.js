import React from "react"
import { connect } from "react-redux"
import { getExamples } from "../redux/example"

@connect(store => ({
    // linking the redux store with this component
    examples: store.example.exampleList,
}))
class LandingPage extends React.Component {

    componentDidMount() {
        this.props.dispatch(getExamples())
    }

    render() {
        return <div>Landing Page</div>
    }
}

export default LandingPage

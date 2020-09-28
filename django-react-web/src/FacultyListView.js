import React from "react";
import axios from "axios";
import Facultys from "../Component/Faculty";
import CustomForm from "./Component/Form";


class FacultyList extends React.Component {
    state = {
        loadingData: true,

        Facultys: []
    };

    fetchFacultys = () => {
        this._isMounted = true;
        if (this.state.loadingData)
            axios
                .get("http://127.0.0.1:8000/listall/")
                .then((res) => {
                    this.setState({
                        loadingData: false,

                        Facultys: res.data
                    })
                })
                .catch((e) => {
                    console.log('error', e)
                })



    }

    componentDidMount() {
        this.fetchFacultys();
    }

    componentWillReceiveProps(newProps) {
        if (newProps.token) {
            this.fetchFacultys();
        }
    }

    render() {
        return (
            <div>
                <Facultys data={this.state.Facultys} /> <br />
                <h2> Create an Faculty </h2>
                <CustomForm requestType="post" FacultyID={null} btnText="Create" />
            </div>
        );

    }
}

export default FacultyList;

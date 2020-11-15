import React from 'react';
import '../../CSS/Quantity.css';

import axios from "axios";

class Faculty extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
        };
    }

    componentDidMount() {
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.headers = {
            "Content-Type": "application/json",
        };

        this.getFacultyList();

    }

    getFacultyList = () => {
        axios.get("http://127.0.0.1:8000/api-web/Major/")
            .then(res => {
                const data = res.data;
                this.setState({ data });
                console.log(res.data);
            })
    }


    render() {
        return (
            <div className="flex-container-column">
                {this.state.data.map(major => {
                    return (
                        <li key={major.majorId}>
                            {major.majorName}
                        </li>
                    );
                }
                )}
            </div>
        );
    }
}



export default Faculty;
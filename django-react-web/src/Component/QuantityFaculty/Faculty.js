import React from 'react';
import '../../CSS/Quantity.css';

import axios from "axios";

class Faculty extends React.Component {

    state = {
        data: [],
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
        axios.get("https://fullstacktest-justdjango.herokuapp.com/api-web/Major/")
            .then(res => {
                const data = res.data;
                this.setState({ data });
                console.log(res.data);
            })
    }


    render() {
        console.log(this.state.data)
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

                <div>
                    <h2>ทดสอบข้อความ มีปัญหาทีไหนกันแน่จ้ะ - -</h2>

                </div>

            </div>




        );
    }
}



export default Faculty;
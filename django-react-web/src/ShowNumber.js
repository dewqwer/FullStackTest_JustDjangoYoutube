import React from "react";
import { Form, Input, Button } from "antd";
import { connect } from "react-redux";
import axios from "axios";


class ShowNumber extends React.Component {

    state = {
        data: [],
    };


    componentDidMount() {
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.headers = {
            "Content-Type": "application/json",
        };



        this.getSubjectList();
    }


    getSubjectList = async () => {
        // this.props.match.params.id
        const res = await axios.get(
            "http://127.0.0.1:8000/realTestNum/",
        );
        console.log(res.data);
        this.setState({ data: res.data });
    };



    // handleFormSubmit = async (event, requestType, facultyID) => {


    //     if (requestType === "post") {
    //         await axios.post("http://127.0.0.1:8000/create/", postObj)
    //             .then(res => {
    //                 if (res.status === 201) {
    //                     this.props.history.push(`/`);
    //                 }
    //             })
    //     } else if (requestType === "put") {
    //         await axios.put(`http://127.0.0.1:8000/${facultyID}/update/`, postObj)
    //             .then(res => {
    //                 if (res.status === 200) {
    //                     this.props.history.push(`/`);
    //                 }
    //             })
    //     }
    // };

    render() {
        console.log(this.state.data)
        return (
            < div >

                <h1>Num: {this.state.data.num}</h1>

            </div >
        );


    }




}


export default ShowNumber;

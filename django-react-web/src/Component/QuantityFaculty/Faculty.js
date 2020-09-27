import React, { Component } from 'react';
import FacultyList from './ShowFaculty';
// import firebase from 'firebase';
import AddBox from './AddFaculty';
import QuestionIcon from '../../IMG/Question.jpg';
import NextIcon from '../../IMG/Next.jpg';

class Faculty extends Component {
    // constructor(props) {
    //     super(props); var firebaseConfig = {
    //         apiKey: "AIzaSyCgerCkI1mr7e07xWQzKP4NVyB9oC3XwU4",
    //         authDomain: "senior-fai.firebaseapp.com",
    //         databaseURL: "https://senior-fai.firebaseio.com",
    //         projectId: "senior-fai",
    //         storageBucket: "senior-fai.appspot.com",
    //         messagingSenderId: "862530252379",
    //         appId: "1:862530252379:web:8be01dd78daa026dee997e",
    //         measurementId: "G-YBP3PN9PEF"
    //     };
    //     if (!firebase.apps.length) {
    //         firebase.initializeApp(firebaseConfig);
    //         firebase.analytics();
    //     }
    // }
    render() {
        return (
            // <div className="background">
            /* <div className="question">
                    <img width="2%" onClick={this.question} src={QuestionIcon}></img>
                </div>
                <div className="block">
                    <FacultyList db={firebase} />
                    <div>
                        <img src={NextIcon} width="3%" className="Next"></img>
                    </div>
                </div>
                <div>
                    <div>
                        <AddBox db={firebase} />
                    </div>
                </div> */



            // </div>
            < div >
                <p> This page must show all list faculty. </p >

                <p> แสดงคณะทั้งหมดที่มี </p>

            </div >
        );
    };
}

export default Faculty;
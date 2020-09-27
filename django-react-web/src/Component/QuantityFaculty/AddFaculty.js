import React, { Component } from 'react';
import trim from 'trim';


class AddFaculty extends Component {
    constructor(props) {
        super(props);
        this.onChange = this.onChange.bind(this);
        this.onKeyup = this.onKeyup.bind(this);
        this.state = {
            message: ''
        };
    }
    onChange(e) {
        this.setState({
            message: e.target.value
        });
    }
    onKeyup(e) {
        if (e.keyCode === 13 && trim(e.target.value) !== '') {
            e.preventDefault();
            let dbCon = this.props.db.database().ref('/messages');
            dbCon.push({
                message: trim(e.target.value)
            });
            this.setState({
                message: ''
            });
        }
    }
    render() {
        return (
            <div>
                <form>
                    <textarea
                        placeholder="Name of faculty"
                        cols="40"
                        onChange={this.onChange}
                        onKeyUp={this.onKeyup}
                        value={this.state.message}>
                    </textarea>
                </form>
            </div>
        )
    }
}
export default AddFaculty
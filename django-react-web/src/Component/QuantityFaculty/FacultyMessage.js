import React, { Component } from 'react';
var deleteBtnStyle = {
    float: "right"
}
class message extends Component {
    constructor(props) {
        super(props);
        this.onClickDelete = this.onClickDelete.bind(this);
    }
    onClickDelete(e) {
        e.preventDefault();
        let dbCon = this.props.db.database().ref('/messages');
        dbCon.child(this.props.msgKey).remove();
    }
    render() {
        return (
            <div>
                {this.props.message}
                <a style={deleteBtnStyle}
                    onClick={this.onClickDelete}>
                    Delete
        </a>
            </div>
        )
    }
}
export default message
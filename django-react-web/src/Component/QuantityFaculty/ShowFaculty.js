import React from 'react';
import '../../CSS/Quantity.css';
import Message from './FacultyMessage';
import _ from 'lodash';

class ShowFaculty extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            messages: []
        };
        let app = this.props.db.database().ref('messages');
        app.on('value', snapshot => {
            this.getData(snapshot.val());
        });
    }
    handleClick = () => {
        console.log('this is:', this);
    }
    question() {
        alert("Press any word");
    }
    getData(values) {
        let messagesVal = values;
        let messages = _(messagesVal)
            .keys()
            .map(messageKey => {
                let cloned = _.clone(messagesVal[messageKey]);
                cloned.key = messageKey;
                return cloned;
            }).value();
        this.setState({
            messages: messages
        });
    }
    render() {
        let messageNodes = this.state.messages.map((message) => {
            return (
                <div className="flex-container-column">
                    <button>
                        <Message
                            msgKey={message.key}
                            message={message.message} // ทำให้ button เป็นสีและขนาดเท่ากับที่ออกแบบ เอาไปใส่ใน flex จะได้ขึ้นทีละ button
                            db={this.props.db} /> {/*ส่งค่า db*/}
                    </button>
                </div>

            )
        });
        return (
            <div>
                {messageNodes}
            </div>
        );
    }
};


export default ShowFaculty;
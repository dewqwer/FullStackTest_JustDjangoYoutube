import React from "react";
import axios from "axios";
import { connect } from "react-redux";
import { Button, Card } from "antd";
import CustomForm from "../components/Form";


class ArticleDetail extends React.Component {
    state = {
        article: {}
    };

    componentDidMount() {
        const facultyID = this.props.match.params.facultyID;
        axios.get(`http://127.0.0.1:8000/api/${facultyID}`).then(res => {
            this.setState({
                article: res.data
            });
        });
    }

    handleDelete = event => {
        event.preventDefault();
        const facultyID = this.props.match.params.facultyID;
        axios.defaults.headers = {
            "Content-Type": "application/json",
            Authorization: `Token ${this.props.token}`
        };
        axios.delete(`http://127.0.0.1:8000/api/${facultyID}/delete/`)
            .then(res => {
                if (res.status === 204) {
                    this.props.history.push(`/`);
                }
            })
    };

    render() {
        return (
            <div>
                <Card title={this.state.article.title}>
                    <p> {this.state.article.content} </p>
                </Card>
                <CustomForm
                    {...this.props}
                    token={this.props.token}
                    requestType="put"
                    facultyID={this.props.match.params.facultyID}
                    btnText="Update"
                />
                <form onSubmit={this.handleDelete}>
                    <Button type="danger" htmlType="submit">
                        Delete
          </Button>
                </form>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        token: state.token
    };
};

export default connect(mapStateToProps)(ArticleDetail);

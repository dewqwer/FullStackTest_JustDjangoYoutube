import React from "react";
import { Form, Input, Button } from "antd";
import { connect } from "react-redux";
import axios from "axios";

const FormItem = Form.Item;


class CustomForm extends React.Component {

  handleFormSubmit = async (event, requestType, articleID) => {
    event.preventDefault();

    const postObj = {
      facultyName: event.target.elements.facultyName.value,
      content: event.target.elements.content.value
    }

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${this.props.token}`,
    };

    if (requestType === "post") {
      await axios.post("http://127.0.0.1:8000/create/", postObj)
        .then(res => {
          if (res.status === 201) {
            this.props.history.push(`/`);
          }
        })
    } else if (requestType === "put") {
      await axios.put(`http://127.0.0.1:8000/${facultyID}/update/`, postObj)
        .then(res => {
          if (res.status === 200) {
            this.props.history.push(`/`);
          }
        })
    }
  };

  render() {
    return (
      <div>
        <Form
          onSubmit={event =>
            this.handleFormSubmit(
              event,
              this.props.requestType,
              this.props.articleID
            )
          }
        >
          <FormItem label="facultyName">
            <Input name="facultyName" placeholder="Put a facultyName here" />
          </FormItem>
          <FormItem label="peopleInFaculty">
            <Input name="peopleInFaculty" placeholder="Enter some content ..." />
          </FormItem>
          <FormItem label="university">
            <Input name="university" placeholder="Put a title here" />
          </FormItem>
          <FormItem label="queueFaculty">
            <Input name="queueFaculty" placeholder="Enter some content ..." />
          </FormItem>
          <FormItem label="queueFacultyPassed">
            <Input name="queueFacultyPassed" placeholder="Enter some content ..." />
          </FormItem>


          
          
          
          
          <FormItem>
            <Button type="primary" htmlType="submit">
              {this.props.btnText}
            </Button>
          </FormItem>
        </Form>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.token
  };
};

export default connect(mapStateToProps)(CustomForm);

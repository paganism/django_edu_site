import React, { Component } from "react";
import { browserHistory } from "react-router";
import CoursesService from "../CoursesService";

/* Import Components */

import Input from "../components/Input";
import TextArea from "../components/TextArea";
import Button from "../components/Button";

const coursesService = new CoursesService();


class FormContainer extends Component {
  constructor(props) {
    super(props);

    this.state = {
      newCourse: {
        title: "",
        duration: "",
        about: "",
        id: "",
      },

    };
    this.handleTextArea = this.handleTextArea.bind(this);
    this.handleDuration = this.handleDuration.bind(this);
    this.handleCourseName = this.handleCourseName.bind(this);
    this.handleFormSubmit = this.handleFormSubmit.bind(this);
    this.handleDelSubmit = this.handleDelSubmit.bind(this);
    this.handleClearForm = this.handleClearForm.bind(this);
    this.handleInput = this.handleInput.bind(this);
  }

  componentDidMount() {
    let self  =  this;
    const { match: { params } } = this.props;
    if(params && params.pk)
    {
    coursesService.getCourse(params.pk).then(function (result) {
        self.setState({ newCourse:  result})
     })
    };
  }
  /* This lifecycle hook gets executed when the component mounts */

  handleCourseName(e) {
    let value = e.target.value;
    this.setState(
      prevState => ({
        newCourse: {
          ...prevState.newCourse,
          title: value
        }
      }),
      // () => console.log(this.state.newCourse)
    );
  }

  handleDuration(e) {
    let value = e.target.value;
    this.setState(
      prevState => ({
        newCourse: {
          ...prevState.newCourse,
          duration: value
        }
      }),
      // () => console.log(this.state.newCourse)
    );
  }

  handleInput(e) {
    let value = e.target.value;
    let name = e.target.name;
    this.setState(
      prevState => ({
        newCourse: {
          ...prevState.newCourse,
          [name]: value
        }
      }),
      // () => console.log(this.state.newCourse)
    );
  }

  handleTextArea(e) {
    let value = e.target.value;
    this.setState(
      prevState => ({
        newCourse: {
          ...prevState.newCourse,
          about: value
        }
      }),
      // () => console.log(this.state.newCourse)
    );
  }

  handleFormSubmit(e) {
    e.preventDefault();
    let courseData = this.state.newCourse;

    coursesService.updateCourse(courseData).then(() => {window.location.assign(`/course/${this.props.match.params.pk}`)});
  }

  handleDelSubmit(e) {
    e.preventDefault();
    let courseData = this.state.newCourse;

    coursesService.deleteCourse(courseData).then(() => {window.location.assign(`/courses`)});
  
  }

  handleClearForm(e) {
    e.preventDefault();
    this.setState({
      newCourse: {
        title: "",
        duration: "",
        about: ""
      }
    });
  }

  render() {
    return (
      <div>
        <form className="container-fluid" onSubmit={this.handleFormSubmit}>
          <Input
            inputType={"text"}
            title={"Название курса"}
            name={"title"}
            value={this.state.newCourse.title}
            placeholder={"Введите название курса"}
            handleChange={this.handleInput}
          />{" "}
          {/* Name of the user */}
          <Input
            inputType={"number"}
            name={"duration"}
            title={"Продолжительность (месяцев)"}
            value={this.state.newCourse.duration}
            placeholder={"Введите длительность курса"}
            handleChange={this.handleDuration}
          />{" "}
          {/* Duration */}

          <TextArea
            title={"О курсе"}
            rows={10}
            value={this.state.newCourse.about}
            name={"currentPetInfo"}
            handleChange={this.handleTextArea}
            placeholder={"Describe your past experience and skills"}
          />
          {/* About course*/}
          <Button
            action={this.handleFormSubmit}
            type={"primary"}
            title={"Обновить"}
            style={buttonStyle}
          />{" "}
          {/*Submit */}
          <Button
            action={this.handleClearForm}
            type={"secondary"}
            title={"Очистить"}
            style={buttonStyle}
          />{" "}
          {/* Clear the form */}
          {/* <Button
            action={this.handleDelForm}
            type={"secondary"}
            title={"Удалить курс"}
            style={buttonStyle}
          />{" "}
          Clear the form */}
        </form>
        <form className="container-fluid" onSubmit={this.handleDelSubmit}>
        <Button
            action={this.handleDelForm}
            type={"secondary"}
            title={"Удалить курс"}
            style={buttonStyle}
          />{" "}
        </form>
      </div>
    );
  }
}

const buttonStyle = {
  margin: "10px 10px 10px 10px"
};

export default FormContainer;

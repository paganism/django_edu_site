import  React, { Component } from  'react';
import  CoursesService  from  './CoursesService';

const coursesService = new CoursesService();

class CoursesList extends Component {

    constructor(props) {
        super(props);
        this.state  = {
            courses: [],
        };
    }

    componentDidMount() {
        let self  =  this;
        coursesService.getCourses().then(function (result) {
            self.setState({ courses:  result.results})
        });
    }

    render() {
        return (
            <div class="row">

                {this.state.courses.map( c  =>

                    <div class="jumbotron col-lg-12">
                        <div class="col-md-3 col-lg-3">
                            <a href={"/course/" + c.pk}><h1>{c.title}</h1></a>
                        </div>
                        <div class="col-md-3 col-lg-3">
                            <img src={c.course_pic} width="100" alt={c.title}/>
                        </div>
                        <div class="course-descr col-md-12 col-lg-12 ">
                            <p>{c.about}</p>
                        </div>
                    </div>
                )}
            </div>
        );
    }
    }

export default CoursesList;

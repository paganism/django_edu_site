import  React, { Component } from  'react';
import  CoursesService  from  './CoursesService';

const coursesService = new CoursesService();

class Course extends Component {
    
constructor(props) {
    super(props);
    this.state  = {
        course_data: [],
    };
}

componentDidMount() {
    var  self  =  this;
    const { match: { params } } = this.props;
    if(params && params.pk)
    {
    coursesService.getCourse(params.pk).then(function (result) {
        self.setState({ course_data:  result})
    })
  };
}

render() {
    return (
        <div class="row">
        
            <p>{ this.state.course_data.about }</p>
    
        <div class="course-detail">
            <p> Продолжительность курса: { this.state.course_data.duration } мес.</p>
            <form method="post" action="">
                        
                <input type="submit" class="btn btn-light" value="Поступить на курс" />
                <input type="hidden" name="pk" value="{ this.state.course_data.pk }" />
            </form>
            
            <p>Дни проведения занятий:</p>
                <ul class="days">
        
                    <li class="nav-item active">{this.state.course_data.day}</li>
                    
                </ul>
            <p>Время проведения: 20:00 Мск</p>
            
            <p>Поступить на курс могут только зарегистрированные пользователи</p>
        </div>
       </div>
    );
    }
}

export  default  Course;

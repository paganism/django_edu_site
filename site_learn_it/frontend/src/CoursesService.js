import axios from 'axios';
const api_URL = 'http://localhost:8000';

export default class CourseService{

    constructor(){}

    getCourses() {
        const url = `${api_URL}/api-oauth/courses/`;
        return axios.get(url).then(response => response.data);
    }
    getCourseByURL(link){
        const url = `${api_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getCourse(pk) {
        const url = `${api_URL}/api-oauth/courses/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteCourse(course){
        const url = `${api_URL}/api-oauth/courses/${course.pk}`;
        return axios.delete(url);
    }
    createCourse(course){
        const url = `${api_URL}/api-oauth/courses/`;
        return axios.post(url,course);
    }
    updateCourse(course){
        const url = `${api_URL}/api-oauth/courses/${course.pk}`;
        return axios.put(url,course);
    }
}

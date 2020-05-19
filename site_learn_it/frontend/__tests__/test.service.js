import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import  CoursesService  from  '../src/CoursesService';
import { api_URL } from  '../src/CoursesService';

const coursesService = new CoursesService();

describe('Service', () => {
    it('returns data when getCourse is called', done => {
        let mock = new MockAdapter(axios);
        const data = {pk: 1, title: 'testCourse'};

        mock.onGet(`${api_URL}/api-oauth/courses/${data['pk']}`).reply(200, data);

        coursesService.getCourse(1).then(response => {
            expect(response).toEqual(data);
            done();
        });
    });

    it('returns data when getCourse is called', done => {
        let mock = new MockAdapter(axios);
        const data = {count: 11, results: [{pk: 1, title: 'testCourse'}, {pk: 2, title: 'testCourse2'}], };

        mock.onGet(`${api_URL}/api-oauth/courses/`).reply(200, data);

        coursesService.getCourses().then(response => {
            expect(response).toEqual(data);
            done();
        });
    });
    
    it('returns "created" data when createCourses is called', done => {
        let mock = new MockAdapter(axios);

        const course = {pk: 1, title: 'testCourse'};
        mock.onPost(`${api_URL}/api-oauth/courses/`).reply(201);

        coursesService.createCourse(course).then(response => {

            expect(response.config.data).toEqual(JSON.stringify(course));
            done();
        });
    });

    it('returns "updated" data when updateCourses is called', done => {
        let mock = new MockAdapter(axios);

        const course = {pk: 1, title: 'testCourse'};
        mock.onPut(`${api_URL}/api-oauth/courses/${course['pk']}`).reply(201);

        coursesService.updateCourse(course).then(response => {
            expect(response.config.data).toEqual(JSON.stringify(course));
            done();
        });
    });
});
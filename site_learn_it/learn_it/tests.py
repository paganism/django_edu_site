import json

from graphene_django.utils.testing import GraphQLTestCase
from site_learn_it.schema import schema
from apiapp.factories import UserFactory, CourseFactory
from learn_it.models import CustomUser, Course


class GQLTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUpTestData(cls):
        cls.counter = 1
        for u in range(10):
            if cls.counter <= 5:
                cls.user = UserFactory(username='nikola'+str(cls.counter), role='s', )
            else:
                cls.user = UserFactory(username='nikola' + str(cls.counter), role='t', )
            cls.user.set_password('nikola')
            cls.course = CourseFactory(title='TestCourse' + str(cls.counter), duration=6, about='test descr')
            cls.course.students.add(cls.user)
            cls.user.save()
            cls.counter+=1

    def test_simple_all_users_query(self):
        response = self.query(
            '''
            query allUsers($limit: Int!) {
              allUsers(limit: $limit) {
                id
                username
                role
              }
            }
            ''',
            op_name='allUsers',
            variables={'limit': 4}

        )
        content = json.loads(response.content)

        self.assertEqual(len(content['data']['allUsers']), 4)
        self.assertResponseNoErrors(response)

    def test_filtered_users_query(self):
        response = self.query(
            '''
            query {
              filteredUsers (username_Istartswith: "nikola") {
                edges {
                  node {
                    id,
                    username,
                    firstName,
                    lastName
                  }
                }
              }
            }
            ''',
            op_name='filteredUsers'
        )
        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        self.assertContains(response, 'nikola')

    def test_all_courses_query(self):
        response = self.query(
            '''
            query {
              allCourses{
                id
                title
                student: students (role:"s"){
                  edges{
                    node{
                      id
                      username
                      role
                    }
                  }
                }
                teacher: students (role:"t"){
                  edges{
                    node{
                      id
                      username
                      role
                    }
                  }
                }
              }
            }
            ''',
            op_name='allCourses'
        )
        content = json.loads(response.content)

        self.assertEqual(content['data']['allCourses'][4]['student']['edges'][0]['node']['username'],
                         CustomUser.objects.get(id=5, role='s').username)
        self.assertEqual(content['data']['allCourses'][5]['teacher']['edges'][0]['node']['username'],
                         CustomUser.objects.get(id=6, role='t').username)
        self.assertResponseNoErrors(response)

    def test_some_mutation(self):
        response = self.query(
            '''
            mutation {
              changeCourseName(newTitle: "JavaScript", courseId:3) {
                course{
                  title
                }
              }
            }
            ''',
            op_name='changeCourseName'
        )

        self.assertEqual(Course.objects.get(id=3).title, 'JavaScript')
        self.assertResponseNoErrors(response)

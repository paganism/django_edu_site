import json

from graphene_django.utils.testing import GraphQLTestCase
from site_learn_it.schema import schema


class GQLTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_simple_all_users_query(self):
        response = self.query(
            '''
            query {
              allUsers(limit:4) {
                id
                username
                role
              }
            }
            ''',
            op_name='allUsers'
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_filtered_users_query(self):
        response = self.query(
            '''
            query {
              filteredUsers (username_Istartswith: "v") {
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
                      username
                    }
                  }
                }
                teacher: students (role:"t"){
                  edges{
                    node{
                      username
                    }
                  }
                }
              }
            }
            ''',
            op_name='allCourses'
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)


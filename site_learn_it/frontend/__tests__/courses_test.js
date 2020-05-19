// function filterByTerm(inputArr, searchTerm) {
//   return inputArr.filter(function(arrayElement) {
//     return arrayElement.url.match(searchTerm);
//   });
// }

// describe("Filter function", () => {
//   test("it should filter by a search term (link)", () => {
//     const input = [
//       { id: 1, url: "https://www.url1.dev" },
//       { id: 2, url: "https://www.url2.dev" },
//       { id: 3, url: "https://www.link3.dev" }
//     ];
//     const output = [{ id: 3, url: "https://www.link3.dev" }];
//     expect(filterByTerm(input, "link")).toEqual(output);
//   });
// });

import React from 'react';
import { shallow } from 'enzyme';
import Courses from '../src/Courses';
import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() });

describe('Courses', () => {
    it('create component Courses', () => {
        
        const wrapper = shallow(<Courses  />);
        expect(wrapper.find('div')).toHaveLength(1);
    });
});
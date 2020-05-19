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
import { shallow, mount } from "enzyme";
import * as React from "react";
import Input from "../src/components/Input";

import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() });



describe("Input Component Tests", () => {
    it("Renders correctly in DOM", () => {
        shallow(
            <Input text="Test" />
        );
    });
    it("Expects to find input HTML element in the DOM", () => {
        const wrapper = shallow(<Input name="testname" title="testtitle"/>);
        expect(wrapper.find('input')).toHaveLength(1);
    });


    it('Should change value when onChange was called', () => {
        const mockOnChange = jest.fn();
        const props = {
            label: 'Test Label',
            type: 'text',
            onChange: mockOnChange,
            value: 'Hello world',
        }
        const wrapper = mount(<Input {...props}/>);
        const event = {
                target: {
                    value: 'This is just for test'
                }
            }
        wrapper.find('input').simulate('change', event);
        expect(mockOnChange).toHaveBeenCalledTimes(1);
    })

    it("Expects to find input HTML element with className test in the DOM", () => {
        const wrapper = shallow(<Input name="testname" title="testtitle"/>);
        console.log(wrapper.find('input').html());
        expect(wrapper.find('input').hasClass('form-control')).toEqual(true);
    });

});
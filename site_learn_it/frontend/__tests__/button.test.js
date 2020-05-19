import { shallow } from "enzyme";
import * as React from "react";
import Button from "../src/components/Button";

import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() });



describe("Button Component Tests", () => {
    it("Renders correctly in DOM", () => {
        shallow(
            <Button text="Test" />
        );
    });
    it("Expects to find button HTML element in the DOM", () => {
        const wrapper = shallow(<Button text="test"/>)
        expect(wrapper.find('button')).toHaveLength(1);
    });

    it("Expects to find button HTML element with className test in the DOM", () => {
        const wrapper = shallow(<Button type="primary"/>);
        expect(wrapper.find('button').hasClass('btn btn-primary')).toEqual(true);
    });

    it("Expects to find button HTML element with className test in the DOM", () => {
        const wrapper = shallow(<Button type="secondary"/>);
        expect(wrapper.find('button').hasClass('btn btn-secondary')).toEqual(true);
    });


    it("Expects to run onClick function when button is pressed in the DOM", () => {
        const mockCallBackClick = jest.fn();
        const wrapper = shallow(<Button action={mockCallBackClick} className="test" text="test"/>);
        wrapper.find('button').simulate('click');
        expect(mockCallBackClick).toHaveBeenCalledTimes(1);
        expect(mockCallBackClick.mock.calls.length).toEqual(1);
    });
});
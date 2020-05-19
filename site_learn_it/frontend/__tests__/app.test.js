import React from 'react';
import { shallow } from 'enzyme';
import Enzyme from 'enzyme';
import App from '../src/App';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() });

it('App renders without crashing', () => {
    shallow(<App />);
});

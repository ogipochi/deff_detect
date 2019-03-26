import {combineReducers} from 'redux';
import convert_reducers from './convert_reducers';

export default combineReducers({
    convert:convert_reducers
});
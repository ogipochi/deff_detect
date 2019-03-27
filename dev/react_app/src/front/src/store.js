import {createStore,applyMiddleware,compose} from 'redux';
import rootReducer from "./reducers";
import thunk from "redux-thunk";



const initialStore = {};
const middleware = [thunk];

const  store = createStore(
    rootReducer,
    initialStore,
    compose(
        applyMiddleware(...middleware),
        //window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__() // Redux Dev Tool使用のための設定
    )
)

export default store;

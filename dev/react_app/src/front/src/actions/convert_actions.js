import {GET_CHARA_NAMES,
    GET_SETTINGS,CHANGE_TEXT,
    POST_CHARA_NAMES,
    CONVERT_TEXT_TO_LIST,IDENTIFY_FILE,
    RESET_TEXT,INPUT_EXCEL_FILES,
    GENERATE_DEFF_FILES,
    CHANGE_SHEET_NAME,
    CAHNGE_VERSION,
    CHANGE_NAME_DETECTION,
    TOGGLE_NAME_EVALUATION,
    CHANGE_NAME_EVALUATION_REAR,
    SELECT_SETTINGS
} from "./types";
import {baseUrl} from "../config";



export const toggleNameEvaluation = (name) =>(dispatch)=>{
    dispatch({
        type  : TOGGLE_NAME_EVALUATION,
        payload : name
    })
}

export const getSettings = () =>(dispatch)=>{
    const url = baseUrl + "/settings/";
    return fetch(url).then(response=>{
        if (!response.ok){
            throw Error;
        }
        return response.json()
    }).then(responseJson=>{
        dispatch({
            type:GET_SETTINGS,
            payload:responseJson.data
        })
    })
}

export const selectSettings = (id) =>(dispatch) =>{
    return dispatch({
        type: SELECT_SETTINGS,
        payload:id
    })
}

export const getCharaNames = (setting_id) =>(dispatch) =>{
    const url = baseUrl + "/chara_names/" + setting_id + "/";
    return fetch(url).then(response=>{
        if(!response.ok){
            throw Error;
        }
        return response.json();
    }).then(responseJson =>{
        dispatch({
            type:GET_CHARA_NAMES,
            payload:responseJson.data
        })
    })
}

export const postCharaNames = (setting_id,data) =>(dispatch) =>{
    const url = baseUrl + "/chara_names/" + setting_id + "/";
    return fetch(url,{method:"POST",body:JSON.stringify(data)}).then(
        response=>{
            if(!response.ok){
                throw Error;
            }
            return response.json();
        }
    ).then(responseJson=>{
        dispatch({
            type : POST_CHARA_NAMES,
            payload : responseJson.data
        })
    })
}

export const changeText = (text) =>(dispatch) =>{
    return dispatch({
        type:CHANGE_TEXT,
        payload:text
    })
}

export const convertTextToList = (data) =>(dispatch) =>{
    const postData = {
        text : data.text,
        version : Number(data.version),
        waitingId:data.waitingId,
        hero : data.hero,
        similarity:data.similarity,
        settingId : data.settingId,
        nameDetect : data.nameDetect
    }
    const url = baseUrl + `/text_to_list/`;
    return fetch(url,{method:"POST",body:JSON.stringify(postData)}).then(response=>{
        if(!response.ok){
            throw Error;
        }
        return response.json()
    }).then(responseJson=>{
        dispatch({
            type : CONVERT_TEXT_TO_LIST,
            payload : responseJson.data
        })
    })
}

export const identifyFile= ()=>(dispatch)=>{
    return dispatch({
        type:IDENTIFY_FILE
    })
}

export const inputExcelFiles = (file) =>(dispatch) =>{
    let data = {};
    data.fileName = file.name;
    data.fileType = file.type;
    const reader = new FileReader();
    reader.addEventListener("load",function(){
        data.fileData = this.result;
        dispatch({
            type:INPUT_EXCEL_FILES,
            payload:data
        })
    },false);
    reader.readAsDataURL(file);
}

export const generateDeffFiles = (data) => (dispatch) =>{
    const url = baseUrl + "/generate_deff/";
    const postData = {};
    postData.settingId = data.settingId;
    postData.textList = data.textList;
    postData.waitingId = data.waitingId;
    postData.hero = data.hero;
    postData.similarity = data.similarity;
    postData.fileData = data.excelFileData;
    postData.fileType = data.excelFileType;
    
    return fetch(url,{method:"POST",body:JSON.stringify(postData)}).then(response=>{
        if(!response.ok){
            throw Error;
        }
        return response.json()
    }).then(responseJson=>{
        dispatch({
            type:GENERATE_DEFF_FILES,
            payload:responseJson
        })
    });

}

export const changeSheetName = (sheetName) =>(dispatch)=>{
    return dispatch(
        {
            type:CHANGE_SHEET_NAME,
            payload:sheetName
        }
    )
}

export const changeVersioin = (value) =>(dispatch)=>{
    return dispatch(
        {
            type:CAHNGE_VERSION,
            payload : value
        }
    )
}

export const changeNameDetection = (value) =>(dispatch) =>{
    return dispatch(
        {
            type:CHANGE_NAME_DETECTION,
            payload : value
        }
    )
}

export const changeNameEvaluationRear = (i,value) =>(dispatch)=>{
    return dispatch(
        {
            type : CHANGE_NAME_EVALUATION_REAR,
            payload : {
                i:i,
                value:value
            }
        }
    )
}
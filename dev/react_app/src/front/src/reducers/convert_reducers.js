import {GET_CHARA_NAMES,GET_SETTINGS,CHANGE_TEXT,IDENTIFY_FILE, 
    CONVERT_TEXT_TO_LIST,INPUT_EXCEL_FILES, GENERATE_DEFF_FILES, 
    CHANGE_SHEET_NAME , CAHNGE_VERSION, CHANGE_NAME_DETECTION, TOGGLE_NAME_EVALUATION,CHANGE_NAME_EVALUATION_REAR, POST_CHARA_NAMES, SELECT_SETTINGS} from "../actions/types";
import {baseUrl,rootUrl} from "../config";

const initialState = {
    excelFileData:"",
    excelFileType:"",
    excelFileName:"",
    text : "",
    settings:[],
    charaNames:[],
    resultFiles:[],
    convertedList:[],
    waitingInLines :[],
    resultList:[],
    version : 1,
    nameDetect:"1",
    nameEvaluation:[],
}


export default function(state=initialState,action){
    const nextState = Object.assign({},state);
    switch(action.type){
        case POST_CHARA_NAMES:
        return nextState;
        case CHANGE_NAME_EVALUATION_REAR:
        nextState.nameEvaluation[action.payload.i].nameRear = action.payload.value;
        return nextState;
        case TOGGLE_NAME_EVALUATION:
        for(let i in nextState.nameEvaluation){
            if (nextState.nameEvaluation[i].nameOrigin==action.payload){
                nextState.nameEvaluation[i].checked = !nextState.nameEvaluation[i].checked;
            }
        }
        return nextState;
        case GET_CHARA_NAMES:
        nextState.charaNames = action.payload;
        return nextState;
        case CHANGE_NAME_DETECTION:
        nextState.nameDetect = action.payload;
        return nextState;
        case CHANGE_SHEET_NAME:
            for(let i in nextState.settings){
                if(nextState.settings[i].selected){
                    nextState.settings[i].sheetName = action.payload;
                }
            }
            return nextState;
        case SELECT_SETTINGS:
        for (let i in nextState.settings){
            if(nextState.settings[i].id==action.payload){
                nextState.settings[i].selected = true;
            }else{
                nextState.settings[i].selected = true;
            }
        }
        return nextState;
        case GENERATE_DEFF_FILES:
        let id = action.payload.data["waiting_id"];
        let filePath = action.payload.data["file_path"]
        for(let i in nextState.resultList){
            if (nextState.resultList[i].waitingId ==id){
                nextState.resultList[i].downloadURL = `${rootUrl}/${filePath}`
                
            }
        }
        return nextState;
        case CONVERT_TEXT_TO_LIST:
        const waitingId = action.payload.waiting_id;
        for(let i in nextState.waitingInLines){
            if (nextState.waitingInLines[i].waitingId==waitingId){
                const result = Object.assign({},nextState.waitingInLines[i]);
                result.textList = action.payload.result;
                // result.nameEvalList = action.payload.name_eval_list
                result.downloadURL = "";
                // resultListに追加
                nextState.resultList.push(result);
                // waitinInLinesから削除
                nextState.waitingInLines = nextState.waitingInLines.filter(n => n !== i);
                for(let i in action.payload.name_eval_list){
                    nextState.nameEvaluation.push(
                        {
                            nameOrigin:action.payload.name_eval_list[i],
                            nameRear : "",
                            checked:false}
                    );
                    
                }
            
            }
        }
        return nextState;
        case GET_SETTINGS:
        nextState.settings = action.payload;
        for (let i in nextState.settings){
            if(i==0){
                nextState.settings[i].selected=true
            }else{
                nextState.settings[i].selected=false
            }
        }
        return nextState;
        case IDENTIFY_FILE:
        // ファイルとテキストをidを振り順番待ちへ
        let now = Date.now();
        let setting = false;
        for (let i in nextState.settings){
            if (nextState.settings[i].selected){
                setting = nextState.settings[i]
            }
        }
        const waitingInLine = {
            excelFileData : nextState.excelFileData,
            excelFileName : nextState.excelFileName,
            excelFileType: nextState.excelFileType,
            text : nextState.text,
            version:nextState.version,
            waitingId:now,
            complete:false,  //テキストの送信時にはこの部分を確認する
            hero:setting.hero,
            similarity:setting.similarity,
            settingId:setting.id,
            sheetName:setting.sheet_name,
            nameDetect:nextState.nameDetect
        };
        nextState.waitingInLines.push(waitingInLine);
        // 初期化
        nextState.excelFileData = undefined;
        nextState.excelFileName = "";
        nextState.excelFileType = "";
        nextState.text = "";

        let inputExcel = document.querySelector("#input-xlsx");
        inputExcel.value="";
        return nextState;
        case CHANGE_TEXT:
        nextState.text = action.payload;
        return nextState;
        case INPUT_EXCEL_FILES:
        nextState.excelFileData = action.payload.fileData;
        nextState.excelFileName = action.payload.fileName;
        nextState.excelFileType = action.payload.fileType;
        return nextState;
        case CAHNGE_VERSION:
        nextState.version = action.payload;
        return nextState;
        default:
        return nextState;
    }
}


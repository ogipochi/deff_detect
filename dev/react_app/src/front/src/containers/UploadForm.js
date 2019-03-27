import React, { Component } from "react";
import { connect } from 'react-redux';
import "../assets/stylesheet/base.css";
import {
    getSettings, changeText, identifyFile,
    convertTextToList, inputExcelFiles, generateDeffFiles,
    changeSheetName, changeVersioin, changeNameDetection, toggleNameEvaluation,
    changeNameEvaluationRear, postCharaNames, getCharaNames, selectSettings, resetNameEvaluation
} from "../actions/convert_actions";
import { rootUrl } from "../config";

class UploadForm extends Component {
    componentWillMount() {
        this.props.getSettings().then(() => {
            let setting = undefined;
            for (let i in this.props.settings) {
                if (this.props.settings[i].selected) {
                    setting = this.props.settings[i];
                }
            }
            this.props.getCharaNames(setting.id);
        }
        );
        this.submitEvalNames = this.submitEvalNames.bind(this);
    }
    submitData = (e) => {
        this.props.identifyFile();
        this.props.convertTextToList(this.props.waitingInLines[this.props.waitingInLines.length - 1]).then(() => {
            this.props.generateDeffFiles(this.props.resultList[this.props.resultList.length - 1]).then(() => {
                this.forceUpdate();
            });
        });
    }
    submitEvalNames = (e) => {
        let setting_id = 0;
        for (let i in this.props.settings) {
            if (this.props.settings[i].selected) {
                setting_id = this.props.settings[i].id;
            }
        }
        this.props.postCharaNames(setting_id, this.props.nameEvaluation).then(() => { 
            this.props.resetNameEvaluation();
            this.props.getCharaNames().then(()=>{
                this.forceUpdate();
            });
        
        });
    }
    render() {
        return (
            <div className="area--UploadForm">
                <div className="area-main--UploadForm">
                    <textarea placeholder="ワードファイルをコピーペーストしてください&#13;&#10;全選択　　：　Ctrl + A (Windows) , Command + A (Mac)&#13;&#10;コピー　　：　Ctrl + C (Windows) , Command + C (Mac)&#13;&#10;ペースト　：　Ctrl + V (Windows) , Command + V (Mac)" className="textarea-word--UploadForm" value={this.props.text} onChange={(e) => { this.props.changeText(e.target.value) }} />
                </div>
                <div className="area-sub--UploadForm">
                    <div className="area-control--UploadForm">
                        <input id="input-xlsx" type="file" onChange={(event) => { this.props.inputExcelFiles(event.target.files[event.target.files.length - 1]) }}></input>
                        <select value={this.props.version} onChange={(event) => { this.props.changeVersioin(event.target.value) }}>
                            <option value="1">
                                Utage:差異抽出
                        </option>
                            <option value="2">
                                Dialog:差異抽出
                    </option>

                        </select>
                        <div>
                            <input type="radio" id="input-name-detect-01" name="input-name-detect" value="1" checked={this.props.nameDetect == "1"} onChange={(e) => { this.props.changeNameDetection(e.target.value) }} />
                            <label for="input-name-detect-01">名前検出あり</label>
                            <input type="radio" id="input-name-detect-02" name="input-name-detect" value="2" checked={this.props.nameDetect == "2"} onChange={(e) => { this.props.changeNameDetection(e.target.value) }} />
                            <label for="input-name-detect-02">名前検出なし</label>
                        </div>
                        <select onChange={(e) => { this.props.selectSettings(e.target.value) }}>
                            {this.props.settings.map(setting => {
                                return (
                                    <option value={setting.id}>
                                        {setting.name}
                                    </option>
                                )
                            })}
                        </select>
                        <div>
                            <div className="btn-submit--UploadForm" onClick={(e) => { this.submitData(e) }}>送信</div>
                        </div>
                    </div>
                    <div className="area-result--UploadForm">
                        <div>変換済ファイル</div>
                        {this.props.resultList.map(result => {
                            let datetime = new Date(result.waitingId);
                            if (result.downloadURL == "") {
                                return (<div>{datetime.toTimeString()}：処理中</div>)
                            }
                            return (
                                <div>{datetime.toTimeString()}：
                                    <a href={result.downloadURL}>
                                        ダウンロード
                                    </a>

                                </div>
                            )
                        })}
                    </div>
                    <div className="area-name--UploadForm">
                        <div className="box-namelist--UploadForm">
                            <table className="tbl-namelist--UploadForm">
                                <tr>
                                    <th>変換前(Word)</th>
                                    <th>変換後(Excel)</th>
                                </tr>
                                {this.props.charaNames.map(charaName => {
                                    return (
                                        <tr className="tr-namelist--UploadForm">
                                            <td>{charaName.name_origin}</td><td>{charaName.name_rear}</td>
                                        </tr>
                                    )
                                })}
                            </table>
                        </div>
                        <div className="box-evallist--UploadForm">
                            <div>名前検出</div>
                            {this.props.nameEvaluation.map((nameEval, i) => {
                                return (
                                    <div>
                                        <input id={`name-check-${i}--UploadForm`} type="checkbox" checked={nameEval.checked} value={nameEval.nameOrigin} onChange={(e) => {
                                            this.props.toggleNameEvaluation(e.target.value);
                                            this.forceUpdate();

                                        }} />
                                        <label for={`name-check-${i}--UploadForm`}>{nameEval.nameOrigin}</label>=>
                                    <input type="text" value={nameEval.nameRear} onChange={(e) => { this.props.changeNameEvaluationRear(i, e.target.value); this.forceUpdate(); }} />
                                    </div>
                                )
                            })}
                            {this.props.resultList.length > 0 && <div className="btn-submit--UploadForm" onClick={(e) => { this.submitEvalNames() }}>名前を追加</div>}
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}


const mapStateToProps = state => (
    {
        excelFileData: state.convert.excelFileData,
        excelFileType: state.convert.excelFileType,
        excelFileName: state.convert.excelFileName,
        text: state.convert.text,
        settings: state.convert.settings,
        charaNames: state.convert.charaNames,
        waitingInLines: state.convert.waitingInLines,
        resultList: state.convert.resultList,
        version: state.convert.version,
        nameDetect: state.convert.nameDetect,
        nameEvaluation: state.convert.nameEvaluation,
    }
)

export default connect(mapStateToProps, {
    getSettings,
    changeText,
    identifyFile,
    convertTextToList,
    inputExcelFiles,
    generateDeffFiles,
    changeSheetName,
    changeVersioin,
    changeNameDetection,
    toggleNameEvaluation,
    changeNameEvaluationRear,
    postCharaNames,
    getCharaNames,
    selectSettings,
    resetNameEvaluation

})(UploadForm);
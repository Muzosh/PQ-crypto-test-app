import QtQuick 2.15
import QtQuick.Controls 2.15


Button{
    id: customLoginBtn
    text: qsTr("Login")
    implicitWidth: 200
    implicitHeight: 40

    property color colorDefault: "transparent"
    property color colorMouseOver: "#a0c2ff"
    property color colorPressed: "#fff"
    property color textDefault: "#fff"
    property color textPressed: "#000"
    property color borderDefault: "#fff"
    property color borderPressed: "transparent"

    QtObject{
        id: internal
        property var changeColorBg:
            if(customLoginBtn.down){
                customLoginBtn.down ? colorPressed : colorDefault

            }else{
                customLoginBtn.hovered ? colorMouseOver : colorDefault
            }
        property var changeColorTxt:
            if(customLoginBtn.down){
                customLoginBtn.down ? textPressed : textDefault
            }else{
                customLoginBtn.hovered ? textDefault : textDefault
            }
        property var changeBorder:
            if(customLoginBtn.down){
                customLoginBtn.down ? borderPressed : borderDefault
            }else{
                customLoginBtn.hovered ? borderPressed : borderDefault
            }
    }

    background: Rectangle{
        color: internal.changeColorBg
        border.color: internal.changeBorder
        border.width: 3
        radius: 15
    }
    contentItem: Item {
        Text{
            id: loginTxt
            text: customLoginBtn.text
            color: internal.changeColorTxt
            font.pointSize: 10
            font.family: "Opensans"
            anchors.verticalCenter: parent.verticalCenter
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

}
/*##^##
Designer {
    D{i:0;autoSize:true;height:40;width:200}
}
##^##*/

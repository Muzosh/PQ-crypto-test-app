import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import "btn"


Window {
    id: login
    width: 720
    height: 400
    visible: true


    Rectangle {
        id: loginScreen
        width: 720
        height: 300
        visible: true
        color: "#132571"
        radius: 0
        border.width: 0
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        clip: false
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#ff132571"
            }

            GradientStop {
                position: 0.00678
                color: "#323b78"
            }

            GradientStop {
                position: 1
                color: "#151e1c"
            }

            GradientStop {
                position: 1.01355
                color: "#132571"
            }

        }

        Text {
            id: loginTitleH1
            color: "#ffffff"
            text: "Project<strong>PQ</strong>"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: loginSubtitleH2.top
            font.pixelSize: 60
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.bottomMargin: -21
            anchors.topMargin: 74
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            bottomPadding: 15
            font.underline: false
            font.weight: Font.Thin
            font.family: "Open Sans"
            minimumPixelSize: 40
            fontSizeMode: Text.VerticalFit
            textFormat: Text.RichText
        }

        Text {
            id: loginSubtitleH2
            color: "#ffffff"
            text: qsTr("Semestral project MPC-KRY")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: loginInput.top
            font.pixelSize: 24
            horizontalAlignment: Text.AlignHCenter
            anchors.bottomMargin: 35
            anchors.topMargin: 150
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            font.italic: false
            font.bold: false
            font.family: "open sans"
        }

        TextField {
            id: loginInput
            y: 205
            height: 50
            background: Rectangle{
                id: loginBg
                radius: 10
                color: "#a0c2ff"
            }
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            horizontalAlignment: Text.AlignHCenter
            leftPadding: 10
            hoverEnabled: true
            placeholderTextColor: "#fff"
            font.hintingPreference: Font.PreferNoHinting
            padding: 10
            rightPadding: 10
            bottomPadding: 10
            topPadding: 10
            font.styleName: "Regular"
            font.pointSize: 12
            font.family: "Open Sans"
            anchors.bottomMargin: 125
            anchors.rightMargin: 120
            anchors.leftMargin: 120
            placeholderText: qsTr("Enter masterpass")
            echoMode: TextInput.Password
        }

        Text {
            id: copyright
            x: 351
            y: 318
            color: "#7fffffff"
            text: "Created: Bc. Dzadíková, Bc. Janout, Bc. Lovinger, Bc. Muzikant"
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            font.pixelSize: 12
            anchors.rightMargin: 30
            anchors.bottomMargin: 8
            textFormat: Text.RichText
        }

        LoginBtn {
            id: loginBtn
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: loginInput.bottom
            anchors.bottom: parent.bottom
            anchors.topMargin: 25
            textPressed: "#ffffff"
            colorPressed: "#132771"
            anchors.bottomMargin: 60
            anchors.rightMargin: 250
            anchors.leftMargin: 250
            rotation: 0
            onClicked: {
                password.checkingPass(loginInput.text)
            }
        }

        Connections{
            target: password

            function onCheckPass(stringText){
                if(stringText === "true"){
                    //copyright.text = "Correct pass"
                    loginBg.color = "#008000"
                    login.close()

                }else{
                    copyright.text = "False pass"
                    loginBg.color = "#FF0000"
                }
            }


        }




    }
}

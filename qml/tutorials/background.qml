
import QtQuick 2.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.3

ApplicationWindow {
    width: 640; height: 360
    style: ApplicationWindowStyle {
        background: BorderImage {
            source: "diamond.jpg"
            border { left: 0; top: 20; right: 0; bottom: 0 }
        }
    }
}

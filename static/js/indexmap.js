var map;
var marker;
var infoWindow;

function initMap() {

    //マップ初期表示の位置設定
    var target = document.getElementById('target');
    var centerp = { lat: 37.67229496806523, lng: 137.88838989062504 };

    //マップ表示
    map = new google.maps.Map(target, {
        center: centerp,
        zoom: 5,

    });

    var ingressButtonDiv = document.createElement("div1");
    var ingressButton = new ingressControl(ingressButtonDiv, map);

    ingressButtonDiv.index = 1;
    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(ingressButtonDiv);

    // 検索実行ボタンが押下されたとき
    document.getElementById('search').addEventListener('click', function () {

        var place = document.getElementById('keyword').value;
        var geocoder = new google.maps.Geocoder();      // geocoderのコンストラクタ

        geocoder.geocode({
            address: place
        }, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {

                var bounds = new google.maps.LatLngBounds();

                for (var i in results) {
                    if (results[0].geometry) {
                        // 緯度経度を取得
                        var latlng = results[0].geometry.location;
                        // 住所を取得
                        var address = results[0].formatted_address;
                        // 検索結果地が含まれるように範囲を拡大
                        bounds.extend(latlng);
                        // マーカーのセット
                        setMarker(latlng);
                        // マーカーへの吹き出しの追加
                        setInfoW(place, latlng, address);
                        // マーカーにクリックイベントを追加
                        markerEvent();
                    }
                }
            } else if (status == google.maps.GeocoderStatus.ZERO_RESULTS) {
                alert("見つかりません");
            } else {
                console.log(status);
                alert("エラー発生");
            }
        });

    });

    // 結果クリアーボタン押下時
    // document.getElementById('clear').addEventListener('click', function () {
    //     deleteMakers();
    // });

}

function ingressControl(buttonDiv, map) {
    var buttonUI = document.createElement("div1");

    buttonUI.style.backgroundColor = "rgb(0, 79, 74)";
    buttonUI.style.border = "1px solid #59fbea";
    buttonUI.style.boxShadow = "rgba(0, 0, 0, 0.3) 0px 1px 4px -1px";
    buttonUI.style.cursor = "pointer";
    buttonUI.style.padding = "1px 6px";

    buttonUI.style.color = "#59fbea";
    buttonUI.style.fontFamily = "Coda, Arial,sans-serif";
    buttonUI.style.fontSize = "15px";
    buttonUI.style.textAlign = "center";

    buttonUI.title = "投稿する";
    buttonUI.innerHTML = "投稿する";

    buttonDiv.style.padding = "5px";
    buttonDiv.appendChild(buttonUI);

    google.maps.event.addDomListener(buttonUI, "click", function () {
        window.location.href = "http://localhost:8000/makepost";
    });
}

// マーカーのセットを実施する
function setMarker(setplace) {
    // 既にあるマーカーを削除
    deleteMakers();

    var iconUrl = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png';
    marker = new google.maps.Marker({
        position: setplace,
        map: map,
        icon: iconUrl
    });
}

//マーカーを削除する
function deleteMakers() {
    if (marker != null) {
        marker.setMap(null);
    }
    marker = null;
}

// マーカーへの吹き出しの追加
function setInfoW(place, latlng, address) {
    infoWindow = new google.maps.InfoWindow({
        content: "<a href='http://www.google.com/search?q=" + place + "' target='_blank'>" + place + "</a><br><br>" + latlng + "<br><br>" + address + "<br><br><a href='http://www.google.com/search?q=" + place + "&tbm=isch' target='_blank'>画像検索 by google</a>"
    });
}

// クリックイベント
function markerEvent() {
    marker.addListener('click', function () {
        infoWindow.open(map, marker);
    });
}

let lat = 35.7100069; // 緯度
let lng= 139.8108103; // 経度
let zoom = 12; // ズームレベル

let map = L.map("map"); // 地図の生成
map.setView([lat, lng], zoom); // 緯度経度、ズームレベルを設定する

// タイルレイヤを生成し、地図に追加する
// 今回はOpenStreetMapを表示する
// zはズームレベル、xとyはタイルの座標。sはサブドメインで、複数のサーバーを使って負荷を分散させるために使われるランダム値。
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 
  {
    // 著作権の表示
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }
).addTo(map);


prefCode = 27;
endPoint = "api/prefs/" + prefCode;

// 外部のGeoJSONファイルを取得する
fetch(endPoint)
  .then(response => response.json())
  // GeoJSONを地図に追加する
  .then(data => {
    L.geoJSON(data).addTo(map);
  });

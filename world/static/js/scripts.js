let geoJsonFile = "world/static/restaurantdata.geojson";
            fetch(geoJsonFile)
            .then(res => res.json())
            .then(data => console.log(data));
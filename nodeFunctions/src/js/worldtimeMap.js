import "ol/ol.css";
import GeoJSON from "ol/format/GeoJSON";
import VectorSource from "ol/source/Vector";
import { Style, Fill, Text, Stroke } from "ol/style";
import VectorLayer from "ol/layer/Vector";
import { Map, View } from "ol";
import Select from "ol/interaction/Select";
import sync from "ol-hashed";

const worldtime_map = document.querySelector("#worldtime_map");

// only dev mode
// const WorldCountriesJson = require('./KenyaRegions.json')

const WorldCountriesVector = new VectorSource({
  features: new GeoJSON().readFeatures(WorldCountriesJson, {
    // dataProjection: 'EPSG:4326',
    // featureProjection: 'EPSG:3857',
    extractGeometryName: true,
  }),
});


const countriesTextLabel = feature => `${feature.get("name")}`;

const countriesTextStyle = feature =>
  new Text({
    textAlign: "center",
    textBaseline: "middle",
    font: `light 16px "Trebuchet MS", Helvetica, sans-serif`,
    text: countriesTextLabel(feature),
    placement: "polygon",
    fill: new Fill({
      color: "rgb(0, 51, 51)",
    }),
  });

  const countriesPolygonStyle = feature => {
  return new Style({
    fill: new Fill({
      color: "rgb(0, 204, 204)",
    }),
    stroke: new Stroke({
      color: "rgb(255, 255, 255)",
      width: 1,
    }),
    text: countriesTextStyle(feature),
  });
};

// countries layer
const worldCountriesLayer = new VectorLayer({
  source: WorldCountriesVector,
  style: countriesPolygonStyle,
});

const worldclockMap = new Map({
  target: worldtime_map,
  layers: [worldCountriesLayer],
  view: new View({
    center: [0, 0],
    zoom: 19,
  }),
});

// selection options
//By default, this is module:ol/events/condition~singleClick. Other defaults are exactly what I need
const singleMapClick = new Select({});

worldclockMap.addInteraction(singleMapClick);

sync(worldclockMap);
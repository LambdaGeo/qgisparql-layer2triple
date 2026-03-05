# Layer2Triple

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![QGIS](https://img.shields.io/badge/QGIS-3.0%2B-brightgreen)](https://qgis.org)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org)

A QGIS plugin to export geographic vector layers as RDF triples in Turtle (`.ttl`) format, enabling integration with linked data ecosystems.

Part of the **QGISParQL** suite — see also [Triple2Layer](https://github.com/LambdaGeo/qgisparql-triple2layer).

---

## Overview

**Layer2Triple** converts QGIS vector layers (points, lines, polygons) into RDF (Resource Description Framework) data using the GeoSPARQL standard. Users can map layer attributes to ontology concepts, define namespaces and prefixes, and export the results as Turtle (`.ttl`) or XML files ready for ingestion into triple stores or linked data portals.

The plugin bridges GIS and Semantic Web workflows, enabling geospatial data to be published as linked open data.

## Features

- Export QGIS vector layers to RDF Turtle (`.ttl`) or XML format
- Load custom OWL vocabularies from remote URLs to map layer attributes
- Map attributes to ontology properties (Constant Value, Layer Attribute, or Vocabulary)
- Define base URL, RDF type, and namespace prefix for generated resources
- Save and reload export configurations as JSON files
- Filter and select specific features or all features in the layer
- Generate unique resource identifiers (UUID) or use an existing layer attribute as ID
- Group observations into a named dataset (`qb:DataSet`) via constant aggregations

## Requirements

- QGIS 3.0 or higher
- Python 3.x (tested on Python 3.10–3.12)
- Python packages: `rdflib`

## Installation

### From QGIS Plugin Repository (recommended)

1. Open QGIS and go to **Plugins → Manage and Install Plugins**
2. Search for `Layer2Triple`
3. Click **Install**

### Manual installation

1. Download or clone this repository
2. Copy the folder to your QGIS plugins directory:
   - **Linux:** `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Windows:** `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
3. Restart QGIS and enable the plugin under **Plugins → Manage and Install Plugins**

## Installing Python Dependencies

QGIS does **not** install external Python packages automatically. You must install them manually in your QGIS Python environment to avoid `ModuleNotFoundError`.

### On Windows

Open the **OSGeo4W Shell** as Administrator and run:

```bash
pip install rdflib
```

### On Linux / macOS

Open your terminal and run:

```bash
pip install rdflib --break-system-packages
```

### requirements.txt

```
rdflib
```

## Usage

1. Open a QGIS project containing at least one vector layer
2. Go to **Vector → QGISParQL → Layer2Triple**
3. Select the layer to export in the **Layer** dropdown
4. *(Optional)* Load an OWL vocabulary via **Vocabulary → Load Vocabulary**
5. Click **Load Layer** to populate the attribute table
6. Map each attribute by selecting a concept and its type (Constant Value, Layer Attribute, or Vocabulary)
7. Set the **Base URL**, **Prefix**, and **RDF Type** for the output resources
8. *(Optional)* Save the configuration via **Settings → Save** for reuse
9. Click **Save** and choose the output file path

For a full walkthrough with screenshots, see the [documentation](docs/).

### Example output (Turtle format)

```turtle
@prefix obs: <https://purl.org/dbcells/observation#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix dbc: <https://purl.org/linked-data/dbcells#> .

obs:a1b2c3d4 a qb:Observation ;
    dbc:resolution 8.3e-02 ;
    geo:asWKT "Polygon ((-34.83 -6.92, ...))" .
```

## Related Plugin

**[Triple2Layer](https://github.com/LambdaGeo/qgisparql-triple2layer)** — the companion plugin that imports SPARQL query results from triple stores back into QGIS as vector layers.

## Authors

- **Sérgio Souza Costa** — [@profsergiocosta](https://github.com/profsergiocosta) — sergio.costa@ufma.br
- **Nerval Junior** — [@nervaljunior](https://github.com/nervaljunior)

Universidade Federal do Maranhão (UFMA) — LambdaGeo Research Group

## Citation

If you use this plugin in your research, please cite:

```bibtex
@software{costa2024layer2triple,
  author  = {Costa, Sérgio Souza and Junior, Nerval},
  title   = {Layer2Triple: A QGIS Plugin for Exporting Geographic Data as RDF Triples},
  year    = {2024},
  url     = {https://github.com/LambdaGeo/qgisparql-layer2triple}
}
```

## License

This project is licensed under the **GNU General Public License v2.0** — see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an [issue](https://github.com/LambdaGeo/qgisparql-layer2triple/issues) or submit a pull request.

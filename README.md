# PyNoco

![](https://github.com/TalaatHasanin/nocodb-python-client/actions/workflows/deploy.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/pynoco.svg)](https://pypi.org/project/pynoco/)

A Python client for [NocoDB](https://nocodb.com/), The Open Source Airtable Alternative. 
This library provides an easy-to-use interface for interacting with NocoDB's API, allowing you to manage your databases, tables, and records seamlessly.

## Features

- [X] Connect to NocoDB and perform CRUD operations on bases. 
- [ ] Fetch, create, update, and delete records with simple method calls.
- [ ] Support for custom queries and filters.

### Installation

To install the SDK, use pip:

```bash
pip install pynoco
```

### Getting Started

1. Initialize the Client

To get started, you'll need to initialize the Client with your API access token. If you're using a different server, you can also specify a custom base URL.

```python
from pynoco.client import Client

# Custom NocoDB Server
base_url = 'https://app.nocodb.com'
client = Client("YOUR_TOKEN", base_url)
```

2. Creating a Source

You can connect to various sources, such as MySQL, by configuring your source data. Use the Source object to define the connection details for your data source.

```python
from pynoco.source import Source

mysql_source = Source(
    id='my_unique_id',
    base_id='base_id',
    type='mysql',
    inflection_column='camelize',
    inflection_table='camelize',
    order=2,
    config='YOUR_DATABASE_CONFIG'
)
```

3. Creating a Base

You can create a `base` and associate it with a source.

```python
# Create a base with a source
base = client.bases.create('base_name', sources=[mysql_source])
```

You can also add a source to an existing base:

```python
# Create a base without a source
base2 = client.bases.create('base_name')

# Add a source to the base
base2.add_source(mysql_source)
```

### Managing Bases

You can create a base.

```python
base = client.bases.create(base_name='base_name', sources=[mysql_source])
```

To update a base, specify the new name, color, and order.

```python
base.update(
    title='new_name',
    order=4,
    color='#24716E'
)
```

#### List Bases

You can list all the bases you’ve created.

```python
print(client.bases.list())
```

#### Get a Base by ID

You can fetch details of a base by its id.

```python
base = client.bases.get('p#######')
```

#### Remove a Base

To delete a base, use the following command:

```python
client.bases.drop('p#######')
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

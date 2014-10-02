import json
import xml.dom.minidom

import jsonx


def test_jsonx_dumps():
    raw = r"""
    {
      "name":"John Smith",
      "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": 10021
      },
      "phoneNumbers": [
        "212 555-1111",
        "212 555-2222"
      ],
      "additionalInfo": null,
      "remote": false,
      "height": 62.4,
      "ficoScore": " > 640"
    }
    """

    from collections import OrderedDict

    obj = json.loads(raw, object_pairs_hook=OrderedDict)
    result = jsonx.dumps(obj)

    doc = xml.dom.minidom.parseString(result)
    pretty = doc.toprettyxml()
    print(pretty)

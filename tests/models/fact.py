import logging


class Fact:
    def __init__(self, **kwargs):
        self._id = str(kwargs.get('_id', ''))
        self.__v = kwargs.get('__v') or kwargs.get('_Fact__v')
        self.sendDate = kwargs.get('sendDate')
        self.source = kwargs.get('source')
        self.user = kwargs.get('user')
        self.text = kwargs.get('text')
        self.updatedAt = kwargs.get('updatedAt')
        self.createdAt = kwargs.get('createdAt')
        self.deleted = kwargs.get('deleted')
        self.type = kwargs.get('type')
        self.status = kwargs.get('status') or {"verified": None, "sentCount": 0}

    @staticmethod
    def get_default_schema():
        """
        Get the schema of the Fact object.
        """
        schema = {
            "_id": "str",
            "__v": "int",
            "user": "str",
            "text": "str",
            "updatedAt": "str",
            "sendDate": "str",
            "deleted": "bool",
            "source": "str",
            "type": "str",
            "status": {
                "verified": "bool",
                "feedback": "str",
                "sentCount": "int"
            }
        }
        return schema

    def get_instance_schema(self):
        """
        Get the schema of the Fact object.
        """
        schema = {
            "_id": self._id,
            "__v": self.__v,
            "sendDate": self.sendDate,
            "source": self.source,
            "user": self.user,
            "text": self.text,
            "updatedAt": self.updatedAt,
            "createdAt": self.createdAt,
            "deleted": self.deleted,
            "type": self.type,
            "status": self.status
        }
        return schema

    @staticmethod
    def _compare_schema(schema, fact):
        """
        Compare the schema with the fact object.
        """
        for key, value in schema.items():
            fact_value = getattr(fact, key, None)  # Get the value of the attribute

            if fact_value is None:
                logging.warning(f"Attribute '{key}' is missing in the fact object")
            elif isinstance(value, dict):  # Check if the schema value is a dictionary
                if not isinstance(fact_value, dict):  # Check if the fact value is also a dictionary
                    assert False, f"Type mismatch for attribute '{key}': Expected dict, but got {type(fact_value).__name__}"
                else:
                    for nested_key, nested_value in value.items():
                        nested_fact_value = fact_value.get(nested_key)
                        if nested_fact_value is None:
                            assert False, f"Attribute '{key}.{nested_key}' is missing in the fact object"
                        elif nested_fact_value != nested_value:
                            assert False, f"Value mismatch for attribute '{key}.{nested_key}': Expected {nested_value}, but got {nested_fact_value}"
            elif fact_value != value:
                assert False, f"Value mismatch for attribute '{key}': Expected {value}, but got {fact_value}"

        return True
class Fact:
    def __init__(self, **kwargs):
        self._id = kwargs.get("_id", "")
        self.__v = kwargs.get("__v") or kwargs.get("_v")
        self.sendDate = kwargs.get("sendDate")
        self.source = kwargs.get("source")
        self.user = kwargs.get("user")
        self.text = kwargs.get("text")
        self.updatedAt = kwargs.get("updatedAt")
        self.createdAt = kwargs.get("createdAt")
        self.deleted = kwargs.get("deleted")
        self.type = kwargs.get("type")
        self.status = kwargs.get("status") or {"verified": None, "sentCount": 0}

    def get_instance_types(self):
        """
        Get the types of the Fact object attribute.
        """
        instance_types = {
            "_id": type(self._id),
            "__v": type(self.__v),
            "sendDate": type(self.sendDate),
            "source": type(self.source),
            "user": type(self.user),
            "text": type(self.text),
            "updatedAt": type(self.updatedAt),
            "createdAt": type(self.createdAt),
            "deleted": type(self.deleted),
            "type": type(self.type),
            "status": type(self.status),
        }
        return instance_types

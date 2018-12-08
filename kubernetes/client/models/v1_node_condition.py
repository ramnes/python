# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NodeCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'last_heartbeat_time': 'datetime',
        'last_transition_time': 'datetime',
        'message': 'str',
        'reason': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'last_heartbeat_time': 'lastHeartbeatTime',
        'last_transition_time': 'lastTransitionTime',
        'message': 'message',
        'reason': 'reason',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, last_heartbeat_time=None, last_transition_time=None, message=None, reason=None, status=None, type=None):
        """
        V1NodeCondition - a model defined in Swagger
        """

        self._last_heartbeat_time = None
        self._last_transition_time = None
        self._message = None
        self._reason = None
        self._status = None
        self._type = None
        self.discriminator = None

        if last_heartbeat_time is not None:
          self.last_heartbeat_time = last_heartbeat_time
        if last_transition_time is not None:
          self.last_transition_time = last_transition_time
        if message is not None:
          self.message = message
        if reason is not None:
          self.reason = reason
        self.status = status
        self.type = type

    @property
    def last_heartbeat_time(self):
        """
        Gets the last_heartbeat_time of this V1NodeCondition.
        Last time we got an update on a given condition.

        :return: The last_heartbeat_time of this V1NodeCondition.
        :rtype: datetime
        """
        return self._last_heartbeat_time

    @last_heartbeat_time.setter
    def last_heartbeat_time(self, last_heartbeat_time):
        """
        Sets the last_heartbeat_time of this V1NodeCondition.
        Last time we got an update on a given condition.

        :param last_heartbeat_time: The last_heartbeat_time of this V1NodeCondition.
        :type: datetime
        """

        self._last_heartbeat_time = last_heartbeat_time

    @property
    def last_transition_time(self):
        """
        Gets the last_transition_time of this V1NodeCondition.
        Last time the condition transit from one status to another.

        :return: The last_transition_time of this V1NodeCondition.
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """
        Sets the last_transition_time of this V1NodeCondition.
        Last time the condition transit from one status to another.

        :param last_transition_time: The last_transition_time of this V1NodeCondition.
        :type: datetime
        """

        self._last_transition_time = last_transition_time

    @property
    def message(self):
        """
        Gets the message of this V1NodeCondition.
        Human readable message indicating details about last transition.

        :return: The message of this V1NodeCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1NodeCondition.
        Human readable message indicating details about last transition.

        :param message: The message of this V1NodeCondition.
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this V1NodeCondition.
        (brief) reason for the condition's last transition.

        :return: The reason of this V1NodeCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1NodeCondition.
        (brief) reason for the condition's last transition.

        :param reason: The reason of this V1NodeCondition.
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """
        Gets the status of this V1NodeCondition.
        Status of the condition, one of True, False, Unknown.

        :return: The status of this V1NodeCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1NodeCondition.
        Status of the condition, one of True, False, Unknown.

        :param status: The status of this V1NodeCondition.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def type(self):
        """
        Gets the type of this V1NodeCondition.
        Type of node condition.

        :return: The type of this V1NodeCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1NodeCondition.
        Type of node condition.

        :param type: The type of this V1NodeCondition.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1NodeCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BulkRecipientsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bulk_recipients=None, end_position=None, next_uri=None, previous_uri=None, result_set_size=None, start_position=None, total_set_size=None):
        """
        BulkRecipientsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bulk_recipients': 'list[BulkRecipient]',
            'end_position': 'str',
            'next_uri': 'str',
            'previous_uri': 'str',
            'result_set_size': 'str',
            'start_position': 'str',
            'total_set_size': 'str'
        }

        self.attribute_map = {
            'bulk_recipients': 'bulkRecipients',
            'end_position': 'endPosition',
            'next_uri': 'nextUri',
            'previous_uri': 'previousUri',
            'result_set_size': 'resultSetSize',
            'start_position': 'startPosition',
            'total_set_size': 'totalSetSize'
        }

        self._bulk_recipients = bulk_recipients
        self._end_position = end_position
        self._next_uri = next_uri
        self._previous_uri = previous_uri
        self._result_set_size = result_set_size
        self._start_position = start_position
        self._total_set_size = total_set_size

    @property
    def bulk_recipients(self):
        """
        Gets the bulk_recipients of this BulkRecipientsResponse.
        A complex type containing information about the bulk recipients in the response.

        :return: The bulk_recipients of this BulkRecipientsResponse.
        :rtype: list[BulkRecipient]
        """
        return self._bulk_recipients

    @bulk_recipients.setter
    def bulk_recipients(self, bulk_recipients):
        """
        Sets the bulk_recipients of this BulkRecipientsResponse.
        A complex type containing information about the bulk recipients in the response.

        :param bulk_recipients: The bulk_recipients of this BulkRecipientsResponse.
        :type: list[BulkRecipient]
        """

        self._bulk_recipients = bulk_recipients

    @property
    def end_position(self):
        """
        Gets the end_position of this BulkRecipientsResponse.
        The last position in the result set. 

        :return: The end_position of this BulkRecipientsResponse.
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """
        Sets the end_position of this BulkRecipientsResponse.
        The last position in the result set. 

        :param end_position: The end_position of this BulkRecipientsResponse.
        :type: str
        """

        self._end_position = end_position

    @property
    def next_uri(self):
        """
        Gets the next_uri of this BulkRecipientsResponse.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :return: The next_uri of this BulkRecipientsResponse.
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """
        Sets the next_uri of this BulkRecipientsResponse.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :param next_uri: The next_uri of this BulkRecipientsResponse.
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """
        Gets the previous_uri of this BulkRecipientsResponse.
        The postal code for the billing address.

        :return: The previous_uri of this BulkRecipientsResponse.
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """
        Sets the previous_uri of this BulkRecipientsResponse.
        The postal code for the billing address.

        :param previous_uri: The previous_uri of this BulkRecipientsResponse.
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """
        Gets the result_set_size of this BulkRecipientsResponse.
        The number of results returned in this response. 

        :return: The result_set_size of this BulkRecipientsResponse.
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """
        Sets the result_set_size of this BulkRecipientsResponse.
        The number of results returned in this response. 

        :param result_set_size: The result_set_size of this BulkRecipientsResponse.
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """
        Gets the start_position of this BulkRecipientsResponse.
        Starting position of the current result set.

        :return: The start_position of this BulkRecipientsResponse.
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """
        Sets the start_position of this BulkRecipientsResponse.
        Starting position of the current result set.

        :param start_position: The start_position of this BulkRecipientsResponse.
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """
        Gets the total_set_size of this BulkRecipientsResponse.
        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.

        :return: The total_set_size of this BulkRecipientsResponse.
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """
        Sets the total_set_size of this BulkRecipientsResponse.
        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.

        :param total_set_size: The total_set_size of this BulkRecipientsResponse.
        :type: str
        """

        self._total_set_size = total_set_size

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

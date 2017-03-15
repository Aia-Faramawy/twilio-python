# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ConnectAppList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the ConnectAppList

        :param Version version: Version that contains the resource
        :param account_sid: The unique sid that identifies this account

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppList
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppList
        """
        super(ConnectAppList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/ConnectApps.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams ConnectAppInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.connect_app.ConnectAppInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ConnectAppInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.connect_app.ConnectAppInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ConnectAppInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppPage
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ConnectAppPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ConnectAppContext

        :param sid: Fetch by unique connect-app Sid

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        return ConnectAppContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ConnectAppContext

        :param sid: Fetch by unique connect-app Sid

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        return ConnectAppContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConnectAppList>'


class ConnectAppPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ConnectAppPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique sid that identifies this account

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppPage
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppPage
        """
        super(ConnectAppPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConnectAppInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        return ConnectAppInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConnectAppPage>'


class ConnectAppContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the ConnectAppContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param sid: Fetch by unique connect-app Sid

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        super(ConnectAppContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/ConnectApps/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ConnectAppInstance

        :returns: Fetched ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ConnectAppInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, authorize_redirect_url=values.unset, company_name=values.unset,
               deauthorize_callback_method=values.unset,
               deauthorize_callback_url=values.unset, description=values.unset,
               friendly_name=values.unset, homepage_url=values.unset,
               permissions=values.unset):
        """
        Update the ConnectAppInstance

        :param unicode authorize_redirect_url: URIL Twilio sends requests when users authorize
        :param unicode company_name: The company name set for this Connect App.
        :param unicode deauthorize_callback_method: HTTP method Twilio WIll use making requests to the url
        :param unicode deauthorize_callback_url: URL Twilio will send a request when a user de-authorizes this app
        :param unicode description: A more detailed human readable description
        :param unicode friendly_name: A human readable name for the Connect App.
        :param unicode homepage_url: The URL users can obtain more information
        :param connect_app.permission permissions: The set of permissions that your ConnectApp requests.

        :returns: Updated ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        data = values.of({
            'AuthorizeRedirectUrl': authorize_redirect_url,
            'CompanyName': company_name,
            'DeauthorizeCallbackMethod': deauthorize_callback_method,
            'DeauthorizeCallbackUrl': deauthorize_callback_url,
            'Description': description,
            'FriendlyName': friendly_name,
            'HomepageUrl': homepage_url,
            'Permissions': permissions,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ConnectAppInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ConnectAppContext {}>'.format(context)


class ConnectAppInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the ConnectAppInstance

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        super(ConnectAppInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'authorize_redirect_url': payload['authorize_redirect_url'],
            'company_name': payload['company_name'],
            'deauthorize_callback_method': payload['deauthorize_callback_method'],
            'deauthorize_callback_url': payload['deauthorize_callback_url'],
            'description': payload['description'],
            'friendly_name': payload['friendly_name'],
            'homepage_url': payload['homepage_url'],
            'permissions': payload['permissions'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ConnectAppContext for this ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        if self._context is None:
            self._context = ConnectAppContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def authorize_redirect_url(self):
        """
        :returns: URIL Twilio sends requests when users authorize
        :rtype: unicode
        """
        return self._properties['authorize_redirect_url']

    @property
    def company_name(self):
        """
        :returns: The company name set for this Connect App.
        :rtype: unicode
        """
        return self._properties['company_name']

    @property
    def deauthorize_callback_method(self):
        """
        :returns: HTTP method Twilio WIll use making requests to the url
        :rtype: unicode
        """
        return self._properties['deauthorize_callback_method']

    @property
    def deauthorize_callback_url(self):
        """
        :returns: URL Twilio will send a request when a user de-authorizes this app
        :rtype: unicode
        """
        return self._properties['deauthorize_callback_url']

    @property
    def description(self):
        """
        :returns: A more detailed human readable description
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def friendly_name(self):
        """
        :returns: A human readable name for the Connect App.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def homepage_url(self):
        """
        :returns: The URL users can obtain more information
        :rtype: unicode
        """
        return self._properties['homepage_url']

    @property
    def permissions(self):
        """
        :returns: The set of permissions that your ConnectApp requests.
        :rtype: connect_app.permission
        """
        return self._properties['permissions']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this connect-apps
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The URI for this resource
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a ConnectAppInstance

        :returns: Fetched ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        return self._proxy.fetch()

    def update(self, authorize_redirect_url=values.unset, company_name=values.unset,
               deauthorize_callback_method=values.unset,
               deauthorize_callback_url=values.unset, description=values.unset,
               friendly_name=values.unset, homepage_url=values.unset,
               permissions=values.unset):
        """
        Update the ConnectAppInstance

        :param unicode authorize_redirect_url: URIL Twilio sends requests when users authorize
        :param unicode company_name: The company name set for this Connect App.
        :param unicode deauthorize_callback_method: HTTP method Twilio WIll use making requests to the url
        :param unicode deauthorize_callback_url: URL Twilio will send a request when a user de-authorizes this app
        :param unicode description: A more detailed human readable description
        :param unicode friendly_name: A human readable name for the Connect App.
        :param unicode homepage_url: The URL users can obtain more information
        :param connect_app.permission permissions: The set of permissions that your ConnectApp requests.

        :returns: Updated ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        return self._proxy.update(
            authorize_redirect_url=authorize_redirect_url,
            company_name=company_name,
            deauthorize_callback_method=deauthorize_callback_method,
            deauthorize_callback_url=deauthorize_callback_url,
            description=description,
            friendly_name=friendly_name,
            homepage_url=homepage_url,
            permissions=permissions,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ConnectAppInstance {}>'.format(context)

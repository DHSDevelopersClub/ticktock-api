"""The endpoints server."""

import endpoints

from calendarsapi import CalendarsAPI
from eventsapi import EventsAPI
from publicapi import PublicAPI
from redirect import explorer_redirect

__author__ = "Alexander Otavka"
__copyright__ = "Copyright (C) 2015 DHS Developers Club"


server = endpoints.api_server([CalendarsAPI, EventsAPI, PublicAPI])

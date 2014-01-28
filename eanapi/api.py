__author__ = 'alex parij'


import requests
import simplejson as json



class API(object):


    def __init__(self, base_url=None, api_key=None, cid=None, minor_rev=None, locale='en_US', currency_code='USD'):
        self._base_url = base_url
        self._store = {
            "apiKey": api_key,
            "cid": cid,
            "minor_rev": minor_rev,
            "locale": locale,
            "currency_code": currency_code
        }

    def _serialize_response(self, data):
        return json.loads(data)

    def GetHotelInfo(self, hotel_id=None):
        """
        HotelInfo end point  
            


        :param hotel_id:
        
        :return:
            JSON response  

        Usage::

        previous config
        API_KEY = 'SAMPLE KEY esdfsdfdsfdsfsdfvfftkg5'
        CID = '55505'
        LOCALE='en_US'
        CURRENCY_CODE='USD'
        MINOR_REV = '20'
        API_ENDPOINT = 'http://api.ean.com/ean-services/rs/hotel/v3/'

        >>> from eanapi import api
        >>> api_service = api.API(API_ENDPOINT, API_KEY, CID, MINOR_REV)
        >>> req = ape_service.GetHotelInfo(566671)
        <Response >

        """

        url  = '%sinfo' % self._base_url
        payload = {}
        for key, value in self._store.iteritems():
            payload[key] = value
        payload['hotelId'] = hotel_id
        try:
            resp = requests.get(url, params=payload)
        except Exception ,exc:
            print exc.message
            raise exc
       

        if 200 <= resp.status_code <= 299:
            return self._serialize_response(resp.text)
        else:
            raise Exception("Request error")

    def GetRoomAvailability(self, hotel_id=None, arrival_date=None, departure_date=None, room_occupancy=[]):
        """
         RoomAvailability end point
         
        :param hotel_id:
        :param arrival_date: date string "%m/%d/%Y" for arrival/start query request
        :param departure_date: date string "%m/%d/%Y" for departure/end query request
        :param room_occupancy:  number of people in each room
        
        :return:
            JSON response  

        Usage::

        previous config
        API_KEY = 'SAMPLE KEY efsdfdsfdsfsdfvfftkg5'
        CID = '55505'
        LOCALE='en_US'
        CURRENCY_CODE='USD'
        MINOR_REV = '20'
        API_ENDPOINT = 'http://api.ean.com/ean-services/rs/hotel/v3/'

        >>> from eanapi import api
        >>> api_service = api.API(API_ENDPOINT, API_KEY, CID, MINOR_REV)
        >>> req = ape_service.GetRoomAvailability(566671,'01/22/2014','01/27/2014',[1])
        <Response >
        """

        url = '%savail' % self._base_url
        payload = {}
        for key, value in self._store.iteritems():
            payload[key] = value
        payload['arrivalDate'] = arrival_date
        payload['departureDate'] = departure_date
        payload['hotelId'] = hotel_id
        for i, v in enumerate(room_occupancy):
            payload['room'+str(i+1)] = v
        try:
            resp = requests.get(url, params=payload)
        except Exception ,exc:
            print exc.message
            raise exc


        if 200 <= resp.status_code <= 299:
            return self._serialize_response(resp.text)
        else:
            raise Exception("Request error")



class ErrorEAN(object):
    def __init__(self, e):
        """
        :param e: JSON response object
        """
        self.category = ''
        self.hotel_id = ''
        self.message = ''
        self.handling = ''
        self.verbose_message = ''
        
        if 'hotelId' in e:
            self.hotel_id = e['hotelId']
        if 'EanWsError' in e:
            self.category = e['EanWsError']['category']
            self.message = e['EanWsError']['presentationMessage']
            self.handling = e['EanWsError']['handling']
            if 'verboseMessage' in e['EanWsError']:
                self.verbose_message = e['EanWsError']['verboseMessage']

    def __str__(self):
        return "%s (%s)" % (self.category, self.message)

class Room(object):
    def __init__(self, r):
        """
           :param r: JSON response 
        """
        
        self.allotment = r['currentAllotment']
        self.room_code = r['roomTypeCode']

    def __str__(self):
        return "%s (%s)" % (self.room_code)



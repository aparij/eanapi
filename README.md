eanapi
======

very simple EAN Expedia api wrapper. For now support only HotelInfo and RoomAvailability end points.

Usage :
define this config data 
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





requirements

requests==2.1.0
simplejson==3.3.1

import datetime
from astral import Astral

if __name__ == '__main__':
    astral = Astral()
    city_name = "New York"
    astral.solar_depression = "civil"
    city = astral[city_name]
    sun_data = city.sun(date=datetime.date.today(), local=True)
    print('Sunset:  %s' % str(sun_data['sunset']))
    print('Dusk:    %s' % str(sun_data['dusk']))

from typing import TypeAlias, Any

import geocoder
from datetime import datetime

from shared.print_header import print_section_header

LocationInfo: TypeAlias = dict[str, Any]


def get_location_info() -> LocationInfo:
    g = geocoder.ip('me')

    latitude = g.latlng[0]
    longitude = g.latlng[1]
    lat_dir = 'N' if latitude >= 0 else 'S'
    long_dir = 'E' if longitude >= 0 else 'W'
    lat_deg, lat_remainder = divmod(abs(latitude), 1)
    lat_min, lat_sec = divmod(lat_remainder * 60, 1)
    lat_sec *= 60
    long_deg, long_remainder = divmod(abs(longitude), 1)
    long_min, long_sec = divmod(long_remainder * 60, 1)
    long_sec *= 60
    coordinates = f"{int(lat_deg)}° {int(lat_min)}' {lat_sec:.2f}\" {lat_dir}, " \
                  f"{int(long_deg)}° {int(long_min)}' {long_sec:.2f}\" {long_dir}"

    isp = g.org
    hostname = g.hostname
    country = g.country
    region = g.state
    city = g.city
    timezone = datetime.now().astimezone().tzinfo

    return {
        'ISP': isp,
        'Hostname': hostname,
        'Country': country,
        'Region/State': region,
        'City': city,
        'Latitude': latitude,
        'Longitude': longitude,
        'Coordinates': coordinates,
        'Timezone': timezone,
    }


def print_location_info(location_info: LocationInfo):
    print()
    print_section_header("Location Information")

    for key, value in location_info.items():
        print(f"  {key}: {value}")

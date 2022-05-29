import httpx
import xmltodict


class IrishRail:
    def _request(self, url):
        response = httpx.get(url)
        data = xmltodict.parse(response.content)
        return data

    def next_trains(self, station):
        data = self._request(
            f"http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc={station}"
        )
        try:
            data = data["ArrayOfObjStationData"]["objStationData"]
        except KeyError:
            # IrishRail API returns 202 for stations that doesn't exists.
            return []

        return sorted(data, key=lambda s: s["Duein"])

    def list_stations(self):
        data = self._request(
            "http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML"
        )
        data = data["ArrayOfObjStation"]["objStation"]
        return sorted(data, key=lambda s: s["StationDesc"])

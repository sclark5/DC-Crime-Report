def fetch_crime_data(api_url, params=None):
    """
    Fetches data from the given API endpoint. But generally made to fetch data from OpenDataDC's arcgis endpoint
    https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/8/query?where=1%3D1&outFields=*&outSR=4326&f=json

    :param api_url: URL of the API endpoint.
    :param params: Optional dictionary of query parameters.
    :return: A dictionary containing the response data.
    """

    try:
        # Make the API call
        response = requests.get(api_url, params=params)

        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API request failed with status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error during API request: {e}")
        return None
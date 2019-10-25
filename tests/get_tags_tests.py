from unittest import TestCase

from tag_app import app
from constants import ResponseStatus


class GetTagsTest(TestCase):
    ad_text_1 = """
    New Toyota  Corolla LE  2007,   Air Conditioning,   Leather seaters,    Auxillary   Gear/4  
    Wheel   Drive,SRS-Airbags,  Alloy   Wheels,
    Abs System, AM/FM   Radio,  Anti-Lock   Brakes, Armrests,   CD  &   DVD Player,Reverse  
    Camera  And Navigation  system,Good-Engine,
    First-Body, Good-Interior,Cup   Holders,    Electric    Mirrors,    Electric    Windows,    Fog 
    Lights, Front   Fog Lamps,  Power   Steering,
    Roof    Rack,   Spoiler,Tinted  Windows,    Wheel   Locks,  Jack,   Wheel   Spanners,   Spare   
    Tire,   LIMITED Edition.
    Also    Available   in  Different   Colours.
    Beware  Of  Fraudsters, therefore   do  not send    money   or  picture to  any dealer  or  
    individual  you have    not gone    to  inspect
    the car first,Please    See What    You Want    To  Buy Before  Any Payment .
    """

    ad_text_2 = """
    New Toyota  Corolla LE  year  year  2007,   Air Conditioning,   Leather
    seaters,    Auxillary   Gear/4
    Wheel   Drive,SRS-Airbags,  Alloy   Wheels,
    Abs System, AM/FM   Radio,  Anti-Lock   Brakes, Armrests,   CD
      &   DVD Player,Reverse Camera  And Navigation  system,Good-Engine,
    First-Body, Good-Interior,Cup   Holders,    Electric    Mirrors,
        Electric    Windows,    Fog
    Lights, Front   Fog Lamps,  Power   Steering,
    Roof    Rack,   Spoiler,Tinted  Windows,    Wheel   Locks,  Jack,
       Wheel           Spanners,   Spare  Tire,   LIMITED Edition.
    Also    Available   in  Different   Colours. Toyota Toyota  .,. car
         auris
         black
    Beware 2015 Of  Fraudsters, therefore   do  not send    money   or
      picture to  any dealer  or  2015 individual  you have    not gone
          to  inspect  the car first,Please    See What    You Want
              To  Buy Before  Any Payment ."""

    def _send_post_request(self, route, data):
        with app.test_client() as c:
            rv = c.post(route, json=data)
            return rv

    def test_get_tags_success_1(self):
        data = {"ad_text": self.ad_text_1}
        response = self._send_post_request("/get_tags", data=data)
        print(response.json)
        self.assertEqual(response.status_code, 200,
                         msg="Response status code is not 200")
        self.assertTrue(response.is_json, msg="Response is not JSON")
        expected_tags = ["toyota", "toyota corolla", "toyota corolla 2007"]
        for tag in expected_tags:
            self.assertIn(tag, response.json.get("data"),
                          msg="Response data is missing expected tag(s)")
        self.assertEqual(ResponseStatus.OK, response.json.get("status"))
        self.assertIn("time_taken", response.json)
        self.assertLess(float(response.json.get("time_taken")), 0.001)

    def test_get_tags_success_2(self):
        data = {"ad_text": self.ad_text_2}
        response = self._send_post_request("/get_tags", data=data)
        print(response.json)
        self.assertEqual(response.status_code, 200,
                         msg="Response status code is not 200")
        self.assertTrue(response.is_json, msg="Response is not JSON")
        expected_tags = ["toyota", "toyota corolla"]
        for tag in expected_tags:
            self.assertIn(tag, response.json.get("data"),
                          msg="Response data is missing expected tag(s)")
        self.assertEqual(ResponseStatus.OK, response.json.get("status"))
        self.assertIn("time_taken", response.json)
        self.assertLess(float(response.json.get("time_taken")), 0.001)

    def test_missing_ad_text_parameter(self):
        data = {}
        response = self._send_post_request("/get_tags", data=data)
        print(response.get_data())
        self.assertEqual(response.status_code, 500,
                         msg="Response status code is not 500")
        self.assertIn("Please specify advertisment text.",
                      response.json.get("error"),
                      msg="Response has no expected error message.")
        self.assertEqual(ResponseStatus.Error, response.json.get("status"))
        self.assertIn("time_taken", response.json)
        self.assertLess(float(response.json.get("time_taken")), 0.001)

    def test_empty_ad_text(self):
        data = {"ad_text": ""}
        response = self._send_post_request("/get_tags", data=data)
        print(response.get_data())
        self.assertEqual(response.status_code, 500,
                         msg="Response status code is not 500")
        self.assertIn("Please specify advertisment text.",
                      response.json.get("error"),
                      msg="Response has no expected error message.")
        self.assertEqual(ResponseStatus.Error, response.json.get("status"))
        self.assertIn("time_taken", response.json)
        self.assertLess(float(response.json.get("time_taken")), 0.001)

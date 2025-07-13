class FwQueryConfig:
    def __init__(self, requests, non_essential_ecus=None, extra_ecus=None, match_fw_to_car_fuzzy=None):
        self.requests = requests
        self.non_essential_ecus = non_essential_ecus or {}
        self.extra_ecus = extra_ecus or []
        self.match_fw_to_car_fuzzy = match_fw_to_car_fuzzy

class Request:
    def __init__(self, req, resp, whitelist_ecus=None, bus=None):
        self.req = req
        self.resp = resp
        self.whitelist_ecus = whitelist_ecus or []
        self.bus = bus

class StdQueries:
    SHORT_TESTER_PRESENT_REQUEST = b''
    SHORT_TESTER_PRESENT_RESPONSE = b''
    OBD_VERSION_REQUEST = b''
    OBD_VERSION_RESPONSE = b''
    TESTER_PRESENT_REQUEST = b''
    TESTER_PRESENT_RESPONSE = b''
    DEFAULT_DIAGNOSTIC_REQUEST = b''
    DEFAULT_DIAGNOSTIC_RESPONSE = b''
    EXTENDED_DIAGNOSTIC_REQUEST = b''
    EXTENDED_DIAGNOSTIC_RESPONSE = b''
    UDS_VERSION_REQUEST = b''
    UDS_VERSION_RESPONSE = b''

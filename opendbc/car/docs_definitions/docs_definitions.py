class CarFootnote:
    def __init__(self, text, column):
        self.text = text
        self.column = column

class CarDocs:
    def __init__(self, name, package=None, video=None, footnotes=None, min_enable_speed=None):
        self.name = name
        self.package = package
        self.video = video
        self.footnotes = footnotes or []
        self.min_enable_speed = min_enable_speed

class Column:
    FSR_LONGITUDINAL = 'FSR_LONGITUDINAL'

class CarParts:
    @staticmethod
    def common(parts):
        return parts

class CarHarness:
    toyota_a = 'toyota_a'

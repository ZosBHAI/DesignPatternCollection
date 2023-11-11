import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)

class SongSerializer01:

    """
     Refactoring the above code
    """

    def serialize(self, song, format):
        if format == 'JSON':
            return self._serialize_to_json(song)
        elif format == 'XML':
            return self._serialize_to_xml(song)
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')

class SongSerializer02:
    """
    Basic Factory implementation
        Note ._get_serializer() method does not call the concrete implementation, and it just
         returns the function object itself.
        ._serialize_to_json() and ._serialize_to_xml() methods are concrete implementations of the product.

    """

    def serialize(self, song, format):
        """
         interface defined is referred to as the product component.
         In our case, the product is a function that takes a Song and
         returns a string representation.
        :param song:
        :param format:
        :return:
        """
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format):
        #Create Component of Factory Method,decides which concrete implementation to use

        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')


class SongSerializer03:

    def serialize(self, song, format):
        serializer = SongSerializer03.get_serializer(format)
        return serializer(song)


    def get_serializer(format):
        if format == 'JSON':
            return _serialize_to_json
        elif format == 'XML':
            return _serialize_to_xml
        else:
            raise ValueError(format)

    @staticmethod
    def _serialize_to_json(song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    @staticmethod
    def _serialize_to_xml(song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')

if __name__ == '__main__':
    song = Song('1', 'Water of Love', 'Dire Straits')
    serializer = SongSerializer01()

    print(serializer.serialize(song, 'JSON'))

"""
    problem with this design:SongSerializer
    
    
    IF we are adding new properties to Song object then, SongSerializer has to be changes
    Creatiing a new format, then we need to add its defintion in serialize method
    
    Resolution:
        Look for a common interface - here  we need to convert a object;object can be 
        Song , Music, Album to JSON/XML  format
    
    
    
    Opputunity for Factory Method 
    Replacing complex logical code
    

"""
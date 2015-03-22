import urllib2
 
# A class to communicate with the EasyN IP Camera
class EasyN:
 
   # A Basic Class Constructor
   def __init__(self, ip, port, user, password, resolution=Resolutions["640x480"], frame_rate=Rate["20"], debug=True):
      self.ip = ip
      self.port = str(port)
      self.user = user
      self.password = password
      self.resolution = resolution
      self.frame_rate = frame_rate
      self._debug = debug
      self._connection = None
      self._connection_url = None

#camera resolutions
      Resolutions = {
      "160x120": 2,
      "320x240": 8,
      "640x480": 32,
   }
 
   #camera frame rate
      Rate = {
      "full": 0,
      "20": 1,
      "15": 3,
      "10": 6,
      "5": 11,
      "4": 12,
      "3": 13,
      "2": 14,
      "1": 15,
      "1p2": 17,
      "1p3": 19,
      "1p4": 21,
      "1p5": 23,
   }


 # A local function to generate the video stream url
   def _get_stream_url(self):
      return "http://%s:%s/videostream.cgi?user=%s&pwd=%s&resolution=%s&rate=%s" % (
         self.ip,
         self.port,
         self.user,
         self.password,
         self.resolution,
         self.frame_rate
      )


# Open a Stream Connection to a url
   def _connect(self, url):
 
      if self._connection is None:
         self._connection_url = url
         self._connection = urllib2.urlopen(self._connection_url)
      else:
         if not self._connection_url == url:
            self._connection = None
            self._connection_url = url
            self._connection = urllib2.urlopen(self._connection_url)
 
   # Close a Connection
   def _close(self):
      self._connection = None
      self._connection_url = None
 
   # A user accessible close connection function
   def close(self):
      self._close()
 

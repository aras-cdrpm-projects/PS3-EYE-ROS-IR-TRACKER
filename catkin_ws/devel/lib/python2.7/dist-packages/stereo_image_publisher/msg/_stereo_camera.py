# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from stereo_image_publisher/stereo_camera.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import std_msgs.msg

class stereo_camera(genpy.Message):
  _md5sum = "011355df31d75f770441e46832dac259"
  _type = "stereo_image_publisher/stereo_camera"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
sensor_msgs/Image leftCamera
sensor_msgs/Image rightCamera
sensor_msgs/CameraInfo leftCameraInfo
sensor_msgs/CameraInfo rightCameraInfo

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: sensor_msgs/CameraInfo
# This message defines meta information for a camera. It should be in a
# camera namespace on topic "camera_info" and accompanied by up to five
# image topics named:
#
#   image_raw - raw data from the camera driver, possibly Bayer encoded
#   image            - monochrome, distorted
#   image_color      - color, distorted
#   image_rect       - monochrome, rectified
#   image_rect_color - color, rectified
#
# The image_pipeline contains packages (image_proc, stereo_image_proc)
# for producing the four processed image topics from image_raw and
# camera_info. The meaning of the camera parameters are described in
# detail at http://www.ros.org/wiki/image_pipeline/CameraInfo.
#
# The image_geometry package provides a user-friendly interface to
# common operations using this meta information. If you want to, e.g.,
# project a 3d point into image coordinates, we strongly recommend
# using image_geometry.
#
# If the camera is uncalibrated, the matrices D, K, R, P should be left
# zeroed out. In particular, clients may assume that K[0] == 0.0
# indicates an uncalibrated camera.

#######################################################################
#                     Image acquisition info                          #
#######################################################################

# Time of image acquisition, camera coordinate frame ID
Header header    # Header timestamp should be acquisition time of image
                 # Header frame_id should be optical frame of camera
                 # origin of frame should be optical center of camera
                 # +x should point to the right in the image
                 # +y should point down in the image
                 # +z should point into the plane of the image


#######################################################################
#                      Calibration Parameters                         #
#######################################################################
# These are fixed during camera calibration. Their values will be the #
# same in all messages until the camera is recalibrated. Note that    #
# self-calibrating systems may "recalibrate" frequently.              #
#                                                                     #
# The internal parameters can be used to warp a raw (distorted) image #
# to:                                                                 #
#   1. An undistorted image (requires D and K)                        #
#   2. A rectified image (requires D, K, R)                           #
# The projection matrix P projects 3D points into the rectified image.#
#######################################################################

# The image dimensions with which the camera was calibrated. Normally
# this will be the full camera resolution in pixels.
uint32 height
uint32 width

# The distortion model used. Supported models are listed in
# sensor_msgs/distortion_models.h. For most cameras, "plumb_bob" - a
# simple model of radial and tangential distortion - is sufficient.
string distortion_model

# The distortion parameters, size depending on the distortion model.
# For "plumb_bob", the 5 parameters are: (k1, k2, t1, t2, k3).
float64[] D

# Intrinsic camera matrix for the raw (distorted) images.
#     [fx  0 cx]
# K = [ 0 fy cy]
#     [ 0  0  1]
# Projects 3D points in the camera coordinate frame to 2D pixel
# coordinates using the focal lengths (fx, fy) and principal point
# (cx, cy).
float64[9]  K # 3x3 row-major matrix

# Rectification matrix (stereo cameras only)
# A rotation matrix aligning the camera coordinate system to the ideal
# stereo image plane so that epipolar lines in both stereo images are
# parallel.
float64[9]  R # 3x3 row-major matrix

# Projection/camera matrix
#     [fx'  0  cx' Tx]
# P = [ 0  fy' cy' Ty]
#     [ 0   0   1   0]
# By convention, this matrix specifies the intrinsic (camera) matrix
#  of the processed (rectified) image. That is, the left 3x3 portion
#  is the normal camera intrinsic matrix for the rectified image.
# It projects 3D points in the camera coordinate frame to 2D pixel
#  coordinates using the focal lengths (fx', fy') and principal point
#  (cx', cy') - these may differ from the values in K.
# For monocular cameras, Tx = Ty = 0. Normally, monocular cameras will
#  also have R = the identity and P[1:3,1:3] = K.
# For a stereo pair, the fourth column [Tx Ty 0]' is related to the
#  position of the optical center of the second camera in the first
#  camera's frame. We assume Tz = 0 so both cameras are in the same
#  stereo image plane. The first camera always has Tx = Ty = 0. For
#  the right (second) camera of a horizontal stereo pair, Ty = 0 and
#  Tx = -fx' * B, where B is the baseline between the cameras.
# Given a 3D point [X Y Z]', the projection (x, y) of the point onto
#  the rectified image is given by:
#  [u v w]' = P * [X Y Z 1]'
#         x = u / w
#         y = v / w
#  This holds for both images of a stereo pair.
float64[12] P # 3x4 row-major matrix


#######################################################################
#                      Operational Parameters                         #
#######################################################################
# These define the image region actually captured by the camera       #
# driver. Although they affect the geometry of the output image, they #
# may be changed freely without recalibrating the camera.             #
#######################################################################

# Binning refers here to any camera setting which combines rectangular
#  neighborhoods of pixels into larger "super-pixels." It reduces the
#  resolution of the output image to
#  (width / binning_x) x (height / binning_y).
# The default values binning_x = binning_y = 0 is considered the same
#  as binning_x = binning_y = 1 (no subsampling).
uint32 binning_x
uint32 binning_y

# Region of interest (subwindow of full camera resolution), given in
#  full resolution (unbinned) image coordinates. A particular ROI
#  always denotes the same window of pixels on the camera sensor,
#  regardless of binning settings.
# The default setting of roi (all values 0) is considered the same as
#  full resolution (roi.width = width, roi.height = height).
RegionOfInterest roi

================================================================================
MSG: sensor_msgs/RegionOfInterest
# This message is used to specify a region of interest within an image.
#
# When used to specify the ROI setting of the camera when the image was
# taken, the height and width fields should either match the height and
# width fields for the associated image; or height = width = 0
# indicates that the full resolution image was captured.

uint32 x_offset  # Leftmost pixel of the ROI
                 # (0 if the ROI includes the left edge of the image)
uint32 y_offset  # Topmost pixel of the ROI
                 # (0 if the ROI includes the top edge of the image)
uint32 height    # Height of ROI
uint32 width     # Width of ROI

# True if a distinct rectified ROI should be calculated from the "raw"
# ROI in this message. Typically this should be False if the full image
# is captured (ROI not used), and True if a subwindow is captured (ROI
# used).
bool do_rectify
"""
  __slots__ = ['header','leftCamera','rightCamera','leftCameraInfo','rightCameraInfo']
  _slot_types = ['std_msgs/Header','sensor_msgs/Image','sensor_msgs/Image','sensor_msgs/CameraInfo','sensor_msgs/CameraInfo']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,leftCamera,rightCamera,leftCameraInfo,rightCameraInfo

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(stereo_camera, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.leftCamera is None:
        self.leftCamera = sensor_msgs.msg.Image()
      if self.rightCamera is None:
        self.rightCamera = sensor_msgs.msg.Image()
      if self.leftCameraInfo is None:
        self.leftCameraInfo = sensor_msgs.msg.CameraInfo()
      if self.rightCameraInfo is None:
        self.rightCameraInfo = sensor_msgs.msg.CameraInfo()
    else:
      self.header = std_msgs.msg.Header()
      self.leftCamera = sensor_msgs.msg.Image()
      self.rightCamera = sensor_msgs.msg.Image()
      self.leftCameraInfo = sensor_msgs.msg.CameraInfo()
      self.rightCameraInfo = sensor_msgs.msg.CameraInfo()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.leftCamera.header.seq, _x.leftCamera.header.stamp.secs, _x.leftCamera.header.stamp.nsecs))
      _x = self.leftCamera.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.leftCamera.height, _x.leftCamera.width))
      _x = self.leftCamera.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.leftCamera.is_bigendian, _x.leftCamera.step))
      _x = self.leftCamera.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.rightCamera.header.seq, _x.rightCamera.header.stamp.secs, _x.rightCamera.header.stamp.nsecs))
      _x = self.rightCamera.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rightCamera.height, _x.rightCamera.width))
      _x = self.rightCamera.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.rightCamera.is_bigendian, _x.rightCamera.step))
      _x = self.rightCamera.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.leftCameraInfo.header.seq, _x.leftCameraInfo.header.stamp.secs, _x.leftCameraInfo.header.stamp.nsecs))
      _x = self.leftCameraInfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.leftCameraInfo.height, _x.leftCameraInfo.width))
      _x = self.leftCameraInfo.distortion_model
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.leftCameraInfo.D)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.leftCameraInfo.D))
      buff.write(_get_struct_9d().pack(*self.leftCameraInfo.K))
      buff.write(_get_struct_9d().pack(*self.leftCameraInfo.R))
      buff.write(_get_struct_12d().pack(*self.leftCameraInfo.P))
      _x = self
      buff.write(_get_struct_6IB3I().pack(_x.leftCameraInfo.binning_x, _x.leftCameraInfo.binning_y, _x.leftCameraInfo.roi.x_offset, _x.leftCameraInfo.roi.y_offset, _x.leftCameraInfo.roi.height, _x.leftCameraInfo.roi.width, _x.leftCameraInfo.roi.do_rectify, _x.rightCameraInfo.header.seq, _x.rightCameraInfo.header.stamp.secs, _x.rightCameraInfo.header.stamp.nsecs))
      _x = self.rightCameraInfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rightCameraInfo.height, _x.rightCameraInfo.width))
      _x = self.rightCameraInfo.distortion_model
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.rightCameraInfo.D)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.rightCameraInfo.D))
      buff.write(_get_struct_9d().pack(*self.rightCameraInfo.K))
      buff.write(_get_struct_9d().pack(*self.rightCameraInfo.R))
      buff.write(_get_struct_12d().pack(*self.rightCameraInfo.P))
      _x = self
      buff.write(_get_struct_6IB().pack(_x.rightCameraInfo.binning_x, _x.rightCameraInfo.binning_y, _x.rightCameraInfo.roi.x_offset, _x.rightCameraInfo.roi.y_offset, _x.rightCameraInfo.roi.height, _x.rightCameraInfo.roi.width, _x.rightCameraInfo.roi.do_rectify))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.leftCamera is None:
        self.leftCamera = sensor_msgs.msg.Image()
      if self.rightCamera is None:
        self.rightCamera = sensor_msgs.msg.Image()
      if self.leftCameraInfo is None:
        self.leftCameraInfo = sensor_msgs.msg.CameraInfo()
      if self.rightCameraInfo is None:
        self.rightCameraInfo = sensor_msgs.msg.CameraInfo()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.leftCamera.header.seq, _x.leftCamera.header.stamp.secs, _x.leftCamera.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCamera.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.leftCamera.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.leftCamera.height, _x.leftCamera.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCamera.encoding = str[start:end].decode('utf-8')
      else:
        self.leftCamera.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.leftCamera.is_bigendian, _x.leftCamera.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.leftCamera.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.rightCamera.header.seq, _x.rightCamera.header.stamp.secs, _x.rightCamera.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCamera.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.rightCamera.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rightCamera.height, _x.rightCamera.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCamera.encoding = str[start:end].decode('utf-8')
      else:
        self.rightCamera.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.rightCamera.is_bigendian, _x.rightCamera.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.rightCamera.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.leftCameraInfo.header.seq, _x.leftCameraInfo.header.stamp.secs, _x.leftCameraInfo.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCameraInfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.leftCameraInfo.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.leftCameraInfo.height, _x.leftCameraInfo.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCameraInfo.distortion_model = str[start:end].decode('utf-8')
      else:
        self.leftCameraInfo.distortion_model = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.leftCameraInfo.D = struct.unpack(pattern, str[start:end])
      start = end
      end += 72
      self.leftCameraInfo.K = _get_struct_9d().unpack(str[start:end])
      start = end
      end += 72
      self.leftCameraInfo.R = _get_struct_9d().unpack(str[start:end])
      start = end
      end += 96
      self.leftCameraInfo.P = _get_struct_12d().unpack(str[start:end])
      _x = self
      start = end
      end += 37
      (_x.leftCameraInfo.binning_x, _x.leftCameraInfo.binning_y, _x.leftCameraInfo.roi.x_offset, _x.leftCameraInfo.roi.y_offset, _x.leftCameraInfo.roi.height, _x.leftCameraInfo.roi.width, _x.leftCameraInfo.roi.do_rectify, _x.rightCameraInfo.header.seq, _x.rightCameraInfo.header.stamp.secs, _x.rightCameraInfo.header.stamp.nsecs,) = _get_struct_6IB3I().unpack(str[start:end])
      self.leftCameraInfo.roi.do_rectify = bool(self.leftCameraInfo.roi.do_rectify)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCameraInfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.rightCameraInfo.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rightCameraInfo.height, _x.rightCameraInfo.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCameraInfo.distortion_model = str[start:end].decode('utf-8')
      else:
        self.rightCameraInfo.distortion_model = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.rightCameraInfo.D = struct.unpack(pattern, str[start:end])
      start = end
      end += 72
      self.rightCameraInfo.K = _get_struct_9d().unpack(str[start:end])
      start = end
      end += 72
      self.rightCameraInfo.R = _get_struct_9d().unpack(str[start:end])
      start = end
      end += 96
      self.rightCameraInfo.P = _get_struct_12d().unpack(str[start:end])
      _x = self
      start = end
      end += 25
      (_x.rightCameraInfo.binning_x, _x.rightCameraInfo.binning_y, _x.rightCameraInfo.roi.x_offset, _x.rightCameraInfo.roi.y_offset, _x.rightCameraInfo.roi.height, _x.rightCameraInfo.roi.width, _x.rightCameraInfo.roi.do_rectify,) = _get_struct_6IB().unpack(str[start:end])
      self.rightCameraInfo.roi.do_rectify = bool(self.rightCameraInfo.roi.do_rectify)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.leftCamera.header.seq, _x.leftCamera.header.stamp.secs, _x.leftCamera.header.stamp.nsecs))
      _x = self.leftCamera.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.leftCamera.height, _x.leftCamera.width))
      _x = self.leftCamera.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.leftCamera.is_bigendian, _x.leftCamera.step))
      _x = self.leftCamera.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.rightCamera.header.seq, _x.rightCamera.header.stamp.secs, _x.rightCamera.header.stamp.nsecs))
      _x = self.rightCamera.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rightCamera.height, _x.rightCamera.width))
      _x = self.rightCamera.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.rightCamera.is_bigendian, _x.rightCamera.step))
      _x = self.rightCamera.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.leftCameraInfo.header.seq, _x.leftCameraInfo.header.stamp.secs, _x.leftCameraInfo.header.stamp.nsecs))
      _x = self.leftCameraInfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.leftCameraInfo.height, _x.leftCameraInfo.width))
      _x = self.leftCameraInfo.distortion_model
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.leftCameraInfo.D)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.leftCameraInfo.D.tostring())
      buff.write(self.leftCameraInfo.K.tostring())
      buff.write(self.leftCameraInfo.R.tostring())
      buff.write(self.leftCameraInfo.P.tostring())
      _x = self
      buff.write(_get_struct_6IB3I().pack(_x.leftCameraInfo.binning_x, _x.leftCameraInfo.binning_y, _x.leftCameraInfo.roi.x_offset, _x.leftCameraInfo.roi.y_offset, _x.leftCameraInfo.roi.height, _x.leftCameraInfo.roi.width, _x.leftCameraInfo.roi.do_rectify, _x.rightCameraInfo.header.seq, _x.rightCameraInfo.header.stamp.secs, _x.rightCameraInfo.header.stamp.nsecs))
      _x = self.rightCameraInfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rightCameraInfo.height, _x.rightCameraInfo.width))
      _x = self.rightCameraInfo.distortion_model
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.rightCameraInfo.D)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.rightCameraInfo.D.tostring())
      buff.write(self.rightCameraInfo.K.tostring())
      buff.write(self.rightCameraInfo.R.tostring())
      buff.write(self.rightCameraInfo.P.tostring())
      _x = self
      buff.write(_get_struct_6IB().pack(_x.rightCameraInfo.binning_x, _x.rightCameraInfo.binning_y, _x.rightCameraInfo.roi.x_offset, _x.rightCameraInfo.roi.y_offset, _x.rightCameraInfo.roi.height, _x.rightCameraInfo.roi.width, _x.rightCameraInfo.roi.do_rectify))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.leftCamera is None:
        self.leftCamera = sensor_msgs.msg.Image()
      if self.rightCamera is None:
        self.rightCamera = sensor_msgs.msg.Image()
      if self.leftCameraInfo is None:
        self.leftCameraInfo = sensor_msgs.msg.CameraInfo()
      if self.rightCameraInfo is None:
        self.rightCameraInfo = sensor_msgs.msg.CameraInfo()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.leftCamera.header.seq, _x.leftCamera.header.stamp.secs, _x.leftCamera.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCamera.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.leftCamera.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.leftCamera.height, _x.leftCamera.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCamera.encoding = str[start:end].decode('utf-8')
      else:
        self.leftCamera.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.leftCamera.is_bigendian, _x.leftCamera.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.leftCamera.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.rightCamera.header.seq, _x.rightCamera.header.stamp.secs, _x.rightCamera.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCamera.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.rightCamera.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rightCamera.height, _x.rightCamera.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCamera.encoding = str[start:end].decode('utf-8')
      else:
        self.rightCamera.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.rightCamera.is_bigendian, _x.rightCamera.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.rightCamera.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.leftCameraInfo.header.seq, _x.leftCameraInfo.header.stamp.secs, _x.leftCameraInfo.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCameraInfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.leftCameraInfo.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.leftCameraInfo.height, _x.leftCameraInfo.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.leftCameraInfo.distortion_model = str[start:end].decode('utf-8')
      else:
        self.leftCameraInfo.distortion_model = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.leftCameraInfo.D = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 72
      self.leftCameraInfo.K = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=9)
      start = end
      end += 72
      self.leftCameraInfo.R = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=9)
      start = end
      end += 96
      self.leftCameraInfo.P = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=12)
      _x = self
      start = end
      end += 37
      (_x.leftCameraInfo.binning_x, _x.leftCameraInfo.binning_y, _x.leftCameraInfo.roi.x_offset, _x.leftCameraInfo.roi.y_offset, _x.leftCameraInfo.roi.height, _x.leftCameraInfo.roi.width, _x.leftCameraInfo.roi.do_rectify, _x.rightCameraInfo.header.seq, _x.rightCameraInfo.header.stamp.secs, _x.rightCameraInfo.header.stamp.nsecs,) = _get_struct_6IB3I().unpack(str[start:end])
      self.leftCameraInfo.roi.do_rectify = bool(self.leftCameraInfo.roi.do_rectify)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCameraInfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.rightCameraInfo.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rightCameraInfo.height, _x.rightCameraInfo.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rightCameraInfo.distortion_model = str[start:end].decode('utf-8')
      else:
        self.rightCameraInfo.distortion_model = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.rightCameraInfo.D = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 72
      self.rightCameraInfo.K = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=9)
      start = end
      end += 72
      self.rightCameraInfo.R = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=9)
      start = end
      end += 96
      self.rightCameraInfo.P = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=12)
      _x = self
      start = end
      end += 25
      (_x.rightCameraInfo.binning_x, _x.rightCameraInfo.binning_y, _x.rightCameraInfo.roi.x_offset, _x.rightCameraInfo.roi.y_offset, _x.rightCameraInfo.roi.height, _x.rightCameraInfo.roi.width, _x.rightCameraInfo.roi.do_rectify,) = _get_struct_6IB().unpack(str[start:end])
      self.rightCameraInfo.roi.do_rectify = bool(self.rightCameraInfo.roi.do_rectify)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6IB = None
def _get_struct_6IB():
    global _struct_6IB
    if _struct_6IB is None:
        _struct_6IB = struct.Struct("<6IB")
    return _struct_6IB
_struct_6IB3I = None
def _get_struct_6IB3I():
    global _struct_6IB3I
    if _struct_6IB3I is None:
        _struct_6IB3I = struct.Struct("<6IB3I")
    return _struct_6IB3I
_struct_12d = None
def _get_struct_12d():
    global _struct_12d
    if _struct_12d is None:
        _struct_12d = struct.Struct("<12d")
    return _struct_12d
_struct_9d = None
def _get_struct_9d():
    global _struct_9d
    if _struct_9d is None:
        _struct_9d = struct.Struct("<9d")
    return _struct_9d
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I

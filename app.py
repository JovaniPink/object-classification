import os, sys
from struct import unpack, pack
import numpy as np
import cv2
import cvlib as cv
import json

# 16-bytes uuid for image id
UUID4_SIZE = 16

# https://docs.python.org/3/library/os.html
# https://stackoverflow.com/questions/15039528/what-is-the-difference-between-os-open-and-os-fdopen-in-python/15039662
# we open the file descriptors 3 and 4 in binary mode with os.fdopen
# setup of FD 3 for input (instead of stdin)
# FD 4 for output (instead of stdout)
def setup_io():
    """TODO: Very functional style but I should really add try statements to handle errors"""
    return os.fdopen(3, "rb"), os.fdopen(4, "wb")


# the input_f (the input file object connected to the file descriptor 3) and unpack("!I", header)
def read_message(input_f):
    # reading the first 4 bytes with the length of the data
    # the other 32 bytes are the UUID string,
    # the rest is the image

    header = input_f.read(4)
    if len(header) != 4:
        return None  # EOF

    # https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
    (total_msg_size,) = unpack("!I", header)
    # image id
    image_id = input_f.read(UUID4_SIZE)

    # read image data
    image_data = input_f.read(total_msg_size - UUID4_SIZE)

    # converting the binary to a opencv image
    nparr = np.fromstring(image_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # OpenCV image and returns a dictionary with image and id
    return {"id": image_id, "image": image}


# detects the objects using cvlib and returns a tuple
def detect(image, model):
    boxes, labels, _conf = cv.detect_common_objects(image, model=model)
    return boxes, labels


# encode the result into a json string and we write to output_f the message’s total size total_msg_size,
# which is the result string len + 16 (the UUID4 size)
def write_result(output, image_id, image_shape, boxes, labels):
    result = json.dumps(
        {"shape": image_shape, "boxes": boxes, "labels": labels}
    ).encode("ascii")

    header = pack("!I", len(result) + UUID4_SIZE)
    output.write(header)
    output.write(image_id)
    output.write(result)
    output.flush()


# main function to keep running the model code
def run(model):
    input_f, output_f = setup_io()

    while True:
        msg = read_message(input_f)
        if msg is None:
            break

        # image shape
        height, width, _ = msg["image"].shape
        shape = {"width": width, "height": height}

        # detect object
        boxes, labels = detect(msg["image"], model)

        # send result back to elixir
        write_result(output_f, msg["id"], shape, boxes, labels)


# I need to refactor to handle errors
if __name__ == "__main__":
    # This is the full model and computational expensive!
    model = "yolov3"
    if len(sys.argv) > 1:
        model = sys.argv[1]

    run(model)

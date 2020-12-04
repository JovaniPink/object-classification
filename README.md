# Object Classification

> Trying to figure out how to detect objects in images and video streams.

I wanted to create a service that if given an image OR capuring frames from a video stream our system would be able to detect material objects and/or people. After research I fell into a couple of python libraries that would help me achieve the system's goal:

- [cvlib](https://docs.cvlib.net/) cvlib is a simple, high level, easy to use, open source Computer Vision library for Python.
- [opencv-python](https://github.com/skvark/opencv-python) Unofficial pre-built CPU-only OpenCV packages for Python.
- [TensorFlow](https://www.tensorflow.org/guide/effective_tf2) An end-to-end open source machine learning platform
- [Keras](https://keras.io/guides/) Deep learning for humans.

... and look into https://www.tensorflow.org/hub/tutorials/tf2_image_retraining

BUT the biggest find I've made to leading to a solution is [COCO (Common Objects in Context)](https://cocodataset.org/#home)

## Features

- All I know is that I've fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)

## Installation

Using my machine's [Conda Environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) I've Included in our repository is our "environment.yml" With this file in the repository, you can create the new environment by running:

```bash
conda env create
source activate objects
```

## Example

Showcasing how the project can be used:

```python
# Still work in Progress
```

## Todo Checklist

A helpful checklist to gauge how your README is coming on what I would like to finish:

- [ ] Double check that the model I found actually works.
- [ ] Use click cli to walk through images in a folder. [Click Blog](https://medium.com/better-programming/python-click-building-your-first-command-line-interface-application-6947d5319ef7)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

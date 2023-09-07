# ndx-depth-moseq Extension for NWB

ndx-depth-moseq is a standardized format for storing the output of [depth-moseq](https://dattalab.github.io/moseq2-website/index.html), an automatic motion sequencing algorithm, in NWB.  Currently, this extension only supports the output of depth-moseq-extract, but will be extended as needed to cover the other types of depth-moseq outputs.

This extension consists of 3 new neurodata types:

- `DepthImageSeries`, which is a simple extension of `pynwb.image.ImageSeries` for depth video with a constant reference depth.
- `MoSeqExtractParameterGroup`, which stores all the various parameters from the depth-moseq-extract algorithm.
- `MoSeqExtractGroup`, which stores all the relevant depth-moseq outputs including the `DepthImageSeries`, `MoSeqExtractParameterGroup`, as well as various native neurodata types such as the `Position`.

## Installation
TODO: Publish in PyPI

## Usage

```python
```

---
This extension was created using [ndx-template](https://github.com/nwb-extensions/ndx-template).

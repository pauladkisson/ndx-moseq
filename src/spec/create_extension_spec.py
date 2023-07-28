# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec, NWBLinkSpec
# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""Extension for MoSeq-extract output""",
        name="""ndx-moseq""",
        version="""0.1.0""",
        author=list(map(str.strip, """Adkisson, Paul""".split(','))),
        contact=list(map(str.strip, """paul.wesley.adkisson@gmail.com""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found.
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # all types included or used by the types specified here will also be
    # included.
    ns_builder.include_type('ImageSeries', namespace='core')
    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('GrayscaleImage', namespace='core')
    ns_builder.include_type('Device', namespace='core')
    ns_builder.include_type('ImageMaskSeries', namespace='core')
    ns_builder.include_type('TimeSeries', namespace='core')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information
    depth_image_series = NWBGroupSpec(
        neurodata_type_def='DepthImageSeries',
        neurodata_type_inc='ImageSeries',
        doc=(
            'An extension of ImageSeries that includes the depth of the most distant depth for reference.'
        ),
        attributes=[
            NWBAttributeSpec(
                name='distant_depth',
                doc='The depth of the most distant depth for reference.',
                dtype='float32'
            )
        ],
    )
    moseq_extract_group = NWBGroupSpec(
        neurodata_type_def='MoSeqExtractGroup',
        neurodata_type_inc='NWBDataInterface',
        doc='Defines a group of all the MoSeq-extract outputs.',
        attributes=[
            NWBAttributeSpec(
                name='version',
                doc='Version of moseq2-extract.',
                dtype='text'
            )
        ],
        datasets=[
            NWBDatasetSpec(
                name='background',
                doc='Computed background image.',
                neurodata_type_inc='GrayscaleImage',
            ),
            NWBDatasetSpec(
                name='roi',
                doc='Region of interest in the raw depth video.',
                neurodata_type_inc='GrayscaleImage',
            ),
        ],
        groups=[
            NWBGroupSpec(
                name='flipped_series',
                doc='Boolean array indicating whether the image was flipped left/right.',
                neurodata_type_inc='TimeSeries',
            ),
            NWBGroupSpec(
                name='processed_depth_video',
                doc='Extracted depth video with aligned animal.',
                neurodata_type_inc='DepthImageSeries',
            ),
            NWBGroupSpec(
                name='loglikelihood_video',
                doc='Log-likelihood that the animal was detected for each pixel.',
                neurodata_type_inc='ImageMaskSeries',
            ),
        ],
        links=[
            NWBLinkSpec(
                name='depth_camera',
                doc='Link to the device (camera) that was used to record the original depth video.',
                target_type='Device',
            ),
        ],
    )

    # TODO: add all of your new data types to this list
    new_data_types = [depth_image_series, moseq_extract_group]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)
    print('Spec files generated. Please make sure to rerun `pip install .` to load the changes.')


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()

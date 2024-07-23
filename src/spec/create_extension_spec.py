# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec, NWBLinkSpec
# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""Extension for MoSeq-extract output""",
        name="""ndx-depth-moseq""",
        version="""0.1.2""",
        author=list(map(str.strip, """Paul Adkisson""".split(','))),
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
    ns_builder.include_type('Position', namespace='core')
    ns_builder.include_type('CompassDirection', namespace='core')
    ns_builder.include_type('DynamicTable', namespace='core')

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
    moseq_extract_parameter_group = NWBGroupSpec(
        neurodata_type_def='MoSeqExtractParameterGroup',
        neurodata_type_inc='NWBDataInterface',
        doc='A group of all the parameters used by moseq-extract.',
        attributes=[
            NWBAttributeSpec(
                name="angle_hampel_sig",
                doc="Angle filter sig",
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='angle_hampel_span',
                doc='Angle filter span',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_depth_range_min',
                doc='Minimum depth to search for floor of arena (in mm)',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_depth_range_max',
                doc='Maximum depth to search for floor of arena (in mm)',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_dilate_x',
                doc='Size of the mask dilation (to include environment walls) in the x dimension',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_dilate_y',
                doc='Size of the mask dilation (to include environment walls) in the y dimension',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_fill_holes',
                doc='If True, fill holes in ROI',
                dtype='bool',
            ),
            NWBAttributeSpec(
                name='bg_roi_gradient_filter',
                doc='If True, exclude walls with gradient filtering',
                dtype='bool',
            ),
            NWBAttributeSpec(
                name='bg_roi_gradient_kernel',
                doc='Kernel size for Sobel gradient filtering',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_gradient_threshold',
                doc='Gradient must be < this to include points',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_index',
                doc='Index of which background mask(s) to use.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='bg_roi_shape',
                doc='Shape to use for the mask dilation (ellipse or rect).',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='bg_roi_weight_area',
                doc='Feature weighting (area) of the background mask.',
                dtype='float64',
            ),
            NWBAttributeSpec(
                name='bg_roi_weight_extent',
                doc='Feature weighting (extent) of the background mask.',
                dtype='float64',
            ),
            NWBAttributeSpec(
                name='bg_roi_weight_dist',
                doc='Feature weighting (dist) of the background mask.',
                dtype='float64',
            ),
            NWBAttributeSpec(
                name='cable_filter_iters',
                doc='Number of cable filter iterations.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='cable_filter_shape',
                doc='Cable filter shape (rectangle or ellipse).',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='cable_filter_size_x',
                doc='Cable filter size (in pixels, x-direction).',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='cable_filter_size_y',
                doc='Cable filter size (in pixels, x-direction).',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='centroid_hampel_sig',
                doc='Hampel filter sig.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='centroid_hampel_span',
                doc='Hampel filter span.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='chunk_overlap',
                doc='Frames overlapped in each chunk. Useful for cable tracking.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='chunk_size',
                doc='Number of frames for each processing iteration.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='compress',
                doc='Convert .dat to .avi after successful extraction.',
                dtype='bool',
            ),
            NWBAttributeSpec(
                name='compress_chunk_size',
                doc='Chunk size for .avi compression.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='compress_threads',
                doc='Number of threads for encoding.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='config_file',
                doc='Location of the config file.',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='crop_size_width',
                doc='Width of cropped mouse image.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='crop_size_height',
                doc='Height of cropped mouse image.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='flip_classifier',
                doc='Location of the flip classifier used to properly orient the mouse (.pkl file).',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='flip_classifier_smoothing',
                doc='Number of frames to smooth flip classifier probabilities.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='fps',
                doc='Frame rate of camera.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='frame_dtype',
                doc='Data type for processed frames.',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='frame_trim_beginning',
                doc='Frames to trim from beginning of data.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='frame_trim_end',
                doc='Frames to trim from end of data.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='max_height',
                doc='Max mouse height from floor (mm).',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='min_height',
                doc='Min mouse height from floor (mm).',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='model_smoothing_clips_x',
                doc='Model smoothing clips in the x-direction.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='model_smoothing_clips_y',
                doc='Model smoothing clips in the y-direction.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='spatial_filter_size',
                doc='Space prefilter kernel (median filter, must be odd).',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='tail_filter_iters',
                doc='Number of tail filter iterations.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='tail_filter_shape',
                doc='Tail filter shape.',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='tail_filter_size_x',
                doc='Tail filter size in the x-direction.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='tail_filter_size_y',
                doc='Tail filter size in the y-direction.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='temporal_filter_size',
                doc='Time prefilter kernel (median filter, must be odd).',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='tracking_model_init',
                doc='Method for tracking model initialization.',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='tracking_model_ll_clip',
                doc='Clip log-likelihoods below this value.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='tracking_model_ll_threshold',
                doc='Threshold on log-likelihood for pixels to use for update during tracking.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='tracking_model_mask_threshold',
                doc='Threshold on log-likelihood to include pixels for centroid and angle calculation.',
                dtype='int64',
            ),
            NWBAttributeSpec(
                name='tracking_model_segment',
                doc='If True, segment likelihood mask from tracking model.',
                dtype='bool',
            ),
            NWBAttributeSpec(
                name='use_plane_bground',
                doc="If True, Use a plane fit for the background. Useful for mice that don't move much.",
                dtype='bool',
            ),
            NWBAttributeSpec(
                name='use_tracking_model',
                doc="Use an expectation-maximization style model to aid mouse tracking. Useful for data with cables.",
                dtype='bool',
            ),
            NWBAttributeSpec(
                name='write_movie',
                doc="Write a results output movie including an extracted mouse.",
                dtype='bool',
            ),
        ]
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
            ),
        ],
        datasets=[
            NWBDatasetSpec(
                name='background',
                doc='Computed background image of the raw depth video.',
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
                name='parameters',
                doc='A group of all the parameters used by moseq-extract.',
                neurodata_type_inc='MoSeqExtractParameterGroup',
            ),
            NWBGroupSpec(
                name='flipped_series',
                doc='Boolean array indicating whether the image was flipped left/right.',
                neurodata_type_inc='TimeSeries',
            ),
            NWBGroupSpec(
                name='processed_depth_video',
                doc='Extracted depth video with aligned subject.',
                neurodata_type_inc='DepthImageSeries',
            ),
            NWBGroupSpec(
                name='loglikelihood_video',
                doc='Log-likelihood that the subject was detected for each pixel.',
                neurodata_type_inc='ImageMaskSeries',
            ),
            NWBGroupSpec(
                name='position',
                doc='3D Position (x, y, height) of the subject in the depth video.',
                neurodata_type_inc='Position',
            ),
            NWBGroupSpec(
                name='heading_2d',
                doc="Overall orientation of the subject (head-side) in 2D (x, y).",
                neurodata_type_inc='CompassDirection',
            ),
            NWBGroupSpec(
                name='speed_2d',
                doc='2D (x, y) Speed of the subject in the depth video.',
                neurodata_type_inc='TimeSeries',
            ),
            NWBGroupSpec(
                name='speed_3d',
                doc='3D (x, y, height) Speed of the subject in the depth video.',
                neurodata_type_inc='TimeSeries',
            ),
            NWBGroupSpec(
                name='angular_velocity_2d',
                doc='2D (x, y) Angular velocity of the subject in the depth video.',
                neurodata_type_inc='TimeSeries',
            ),
            NWBGroupSpec(
                name='length',
                doc='Length of the subject in the depth video.',
                neurodata_type_inc='TimeSeries',
            ),
            NWBGroupSpec(
                name='width',
                doc='Width of the subject in the depth video.',
                neurodata_type_inc='TimeSeries',
            ),
            NWBGroupSpec(
                name='area',
                doc='Pixel-wise area of the subject in the depth video.',
                neurodata_type_inc='TimeSeries',
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
    new_data_types = [depth_image_series, moseq_extract_parameter_group, moseq_extract_group]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)
    print('Spec files generated. Please make sure to rerun `pip install .` to load the changes.')


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()

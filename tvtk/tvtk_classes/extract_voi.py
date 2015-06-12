# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ExtractVOI(ImageAlgorithm):
    """
    ExtractVOI - select piece (e.g., volume of interest) and/or
    subsample structured points dataset
    
    Superclass: ImageAlgorithm
    
    ExtractVOI is a filter that selects a portion of an input
    structured points dataset, or subsamples an input dataset. (The
    selected portion of interested is referred to as the Volume Of
    Interest, or VOI.) The output of this filter is a structured points
    dataset. The filter treats input data of any topological dimension
    (i.e., point, line, image, or volume) and can generate output data of
    any topological dimension.
    
    To use this filter set the VOI ivar which are i-j-k min/max indices
    that specify a rectangular region in the data. (Note that these are
    0-offset.) You can also specify a sampling rate to subsample the
    data.
    
    Typical applications of this filter are to extract a slice from a
    volume for image processing, subsampling large volumes to reduce data
    size, or extracting regions of a volume with interesting data.
    
    See Also:
    
    GeometryFilter ExtractGeometry ExtractGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractVOI, obj, update, **traits)
    
    sample_rate = traits.Array(shape=(3,), value=(1, 1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _sample_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleRate,
                        self.sample_rate)

    voi = traits.Array(shape=(6,), value=(0, 2147483647, 0, 2147483647, 0, 2147483647), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _voi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVOI,
                        self.voi)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('voi', 'GetVOI'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'), ('sample_rate',
    'GetSampleRate'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'sample_rate', 'voi'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractVOI, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractVOI properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['sample_rate', 'voi']),
            title='Edit ExtractVOI properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractVOI properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

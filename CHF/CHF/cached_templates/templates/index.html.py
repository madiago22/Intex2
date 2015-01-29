# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422084847.110051
_enable_loop = True
_template_filename = 'C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n <div id="myCarousel" class="carousel slide" data-ride="carousel">\r\n  <!-- Indicators -->\r\n  <ol class="carousel-indicators">\r\n    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>\r\n    <li data-target="#myCarousel" data-slide-to="1"></li>\r\n    <li data-target="#myCarousel" data-slide-to="2"></li>\r\n    <li data-target="#myCarousel" data-slide-to="3"></li>\r\n  </ol>\r\n\r\n  <!-- Wrapper for slides -->\r\n  <div class="carousel-inner" role="listbox">\r\n    <div class="item active">\r\n      <img src="https://marriottschool.byu.edu/msmadmin/securefile/empphoto/?file=b0%2F5487.jpg" alt="Gove">\r\n    </div>\r\n\r\n    <div class="item">\r\n      <img src="https://marriottschool.byu.edu/msmadmin/securefile/empphoto/?file=b0%2F5352.jpg" alt="Stephen">\r\n    </div>\r\n\r\n    <div class="item">\r\n      <img src="https://marriottschool.byu.edu/msmadmin/securefile/empphoto/?file=b0%2F5293.jpg" alt="Flower">\r\n    </div>\r\n\r\n    <div class="item">\r\n      <img src="https://marriottschool.byu.edu/msmadmin/securefile/empphoto/?file=b0%2F5325.jpg" alt="Marshall">\r\n    </div>\r\n  </div>\r\n\r\n  <!-- Left and right controls -->\r\n  <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">\r\n    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>\r\n    <span class="sr-only">Previous</span>\r\n  </a>\r\n  <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">\r\n    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>\r\n    <span class="sr-only">Next</span>\r\n  </a>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n\r\n\r\n      <h1>HTML Ipsum Presents</h1>\r\n\r\n<p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href="#">Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p>\r\n<p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href="#">Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p>\r\n<p><strong>Pellentesque habitant morbi tristique</strong> senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. <em>Aenean ultricies mi vitae est.</em> Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, <code>commodo vitae</code>, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. <a href="#">Donec non enim</a> in turpis pulvinar facilisis. Ut felis.</p>\r\n\r\n<h2>Header Level 2</h2>\r\n\r\n<ol>\r\n   <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li>\r\n   <li>Aliquam tincidunt mauris eu risus.</li>\r\n</ol>\r\n\r\n<blockquote><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus turpis elit sit amet quam. Vivamus pretium ornare est.</p></blockquote>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/index.html", "line_map": {"34": 1, "51": 3, "39": 23, "57": 51, "27": 0, "45": 3}, "source_encoding": "ascii", "uri": "index.html"}
__M_END_METADATA
"""

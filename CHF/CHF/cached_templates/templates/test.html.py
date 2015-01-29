# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422061532.50552
_enable_loop = True
_template_filename = 'C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/test.html'
_template_uri = 'test.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


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
    return runtime._inherit_from(context, 'manage.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/test.html", "line_map": {"32": 1, "27": 0, "38": 32}, "uri": "test.html"}
__M_END_METADATA
"""

# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422890598.072372
_enable_loop = True
_template_filename = 'C:\\Dev\\Intex2\\CHF\\CHF\\templates/manage.htm'
_template_uri = 'manage.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['form', 'content', 'bottomList', 'list', 'listTitle']


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
        def bottomList():
            return render_bottomList(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def form():
            return render_form(context._locals(__M_locals))
        def list():
            return render_list(context._locals(__M_locals))
        def listTitle():
            return render_listTitle(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def form():
            return render_form(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bottomList():
            return render_bottomList(context)
        def content():
            return render_content(context)
        def form():
            return render_form(context)
        def list():
            return render_list(context)
        def listTitle():
            return render_listTitle(context)
        __M_writer = context.writer()
        __M_writer('\r\n   <table class="manageTable">\r\n       <tr>\r\n           <td class="listCol">\r\n              <h3>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'listTitle'):
            context['self'].listTitle(**pageargs)
        

        __M_writer('</h3>\r\n               <div class="list">\r\n                    <table class="listTable">\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'list'):
            context['self'].list(**pageargs)
        

        __M_writer('\r\n                    </table>\r\n\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bottomList'):
            context['self'].bottomList(**pageargs)
        

        __M_writer('\r\n\r\n                <div class="input-group" id="searchBar">\r\n                  <span class="input-group-btn">\r\n                    <button class="btn btn-default" type="button">Go!</button>\r\n                  </span>\r\n                  <input type="text" class="form-control" placeholder="Search for...">\r\n                </div>\r\n               </div>\r\n           </td>\r\n            <td class="spacer">&nbsp</td>\r\n           <td class="crudCol">\r\n                <div class="crudBox ">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'form'):
            context['self'].form(**pageargs)
        

        __M_writer('\r\n               </div>\r\n           </td>\r\n            <td class="spacer">&nbsp</td>\r\n       </tr>\r\n   </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottomList(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bottomList():
            return render_bottomList(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                         ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def list():
            return render_list(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                         ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_listTitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def listTitle():
            return render_listTitle(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 3, "122": 10, "98": 32, "128": 7, "104": 15, "42": 1, "139": 128, "78": 3, "83": 7, "52": 30, "110": 15, "88": 12, "116": 10, "58": 30, "27": 0, "93": 17}, "filename": "C:\\Dev\\Intex2\\CHF\\CHF\\templates/manage.htm", "uri": "manage.htm"}
__M_END_METADATA
"""

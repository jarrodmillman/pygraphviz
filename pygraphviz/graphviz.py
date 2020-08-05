# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _graphviz
else:
    import _graphviz

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def agopen(name, kind, disc):
    return _graphviz.agopen(name, kind, disc)

def agraphnew(name,strict=False,directed=False):
    if strict:
       if directed:
            return _graphviz.agopen(name,cvar.Agstrictdirected,None)
       else:
            return _graphviz.agopen(name,cvar.Agstrictundirected,None)
    else:
        if directed:
            return _graphviz.agopen(name,cvar.Agdirected,None)
        else:		 
            return _graphviz.agopen(name,cvar.Agundirected,None)


def agclose(g):
    return _graphviz.agclose(g)

def agread(file, arg2):
    return _graphviz.agread(file, arg2)

def agwrite(g, file):
    return _graphviz.agwrite(g, file)

def agisundirected(g):
    return _graphviz.agisundirected(g)

def agisdirected(g):
    return _graphviz.agisdirected(g)

def agisstrict(g):
    return _graphviz.agisstrict(g)

def agnode(g, name, createflag):
    return _graphviz.agnode(g, name, createflag)

def agidnode(g, id, createflag):
    return _graphviz.agidnode(g, id, createflag)

def agsubnode(g, n, createflag):
    return _graphviz.agsubnode(g, n, createflag)

def agfstnode(g):
    return _graphviz.agfstnode(g)

def agnxtnode(g, n):
    return _graphviz.agnxtnode(g, n)

def aglstnode(g):
    return _graphviz.aglstnode(g)

def agprvnode(g, n):
    return _graphviz.agprvnode(g, n)

def agedge(g, t, h, name, createflag):
    return _graphviz.agedge(g, t, h, name, createflag)

def agidedge(g, t, h, id, createflag):
    return _graphviz.agidedge(g, t, h, id, createflag)

def agsubedge(g, e, createflag):
    return _graphviz.agsubedge(g, e, createflag)

def agfstin(g, n):
    return _graphviz.agfstin(g, n)

def agnxtin(g, e):
    return _graphviz.agnxtin(g, e)

def agfstout(g, n):
    return _graphviz.agfstout(g, n)

def agnxtout(g, e):
    return _graphviz.agnxtout(g, e)

def agfstedge(g, n):
    return _graphviz.agfstedge(g, n)

def agnxtedge(g, e, n):
    return _graphviz.agnxtedge(g, e, n)

def aghead(e):
    return _graphviz.aghead(e)

def agtail(e):
    return _graphviz.agtail(e)

def agattr(g, kind, name, value):
    return _graphviz.agattr(g, kind, name, value)

def agattrsym(obj, name):
    return _graphviz.agattrsym(obj, name)

def agnxtattr(g, kind, attr):
    return _graphviz.agnxtattr(g, kind, attr)

def agget(obj, name):
    return _graphviz.agget(obj, name)

def agxget(obj, sym):
    return _graphviz.agxget(obj, sym)

def agset(obj, name, value):
    return _graphviz.agset(obj, name, value)

def agxset(obj, sym, value):
    return _graphviz.agxset(obj, sym, value)

def agsafeset(obj, name, value, _def):
    return _graphviz.agsafeset(obj, name, value, _def)

def agattrname(atsym):
    return _graphviz.agattrname(atsym)

def agattrdefval(atsym):
    return _graphviz.agattrdefval(atsym)

def agsafeset_label(g, obj, name, val, _def):
    return _graphviz.agsafeset_label(g, obj, name, val, _def)

def agattr_label(g, kind, name, val):
    return _graphviz.agattr_label(g, kind, name, val)

def agsubg(g, name, createflag):
    return _graphviz.agsubg(g, name, createflag)

def agfstsubg(g):
    return _graphviz.agfstsubg(g)

def agnxtsubg(subg):
    return _graphviz.agnxtsubg(subg)

def agparent(g):
    return _graphviz.agparent(g)

def agroot(g):
    return _graphviz.agroot(g)

def agdelsubg(g, sub):
    return _graphviz.agdelsubg(g, sub)

def agnnodes(g):
    return _graphviz.agnnodes(g)

def agnedges(g):
    return _graphviz.agnedges(g)

def agdegree(g, n, _in, out):
    return _graphviz.agdegree(g, n, _in, out)

def agraphof(arg1):
    return _graphviz.agraphof(arg1)

def agnameof(arg1):
    return _graphviz.agnameof(arg1)

def agdelnode(g, arg_n):
    return _graphviz.agdelnode(g, arg_n)

def agdeledge(g, arg_e):
    return _graphviz.agdeledge(g, arg_e)

def agnameof(handle):
  name=_graphviz.agnameof(handle)
  if name is None:
     return None
  if name==b'' or name.startswith(b'%'):
    return None
  else:
    return name 

AGRAPH = _graphviz.AGRAPH
AGNODE = _graphviz.AGNODE
AGOUTEDGE = _graphviz.AGOUTEDGE
AGINEDGE = _graphviz.AGINEDGE
AGEDGE = _graphviz.AGEDGE

cvar = _graphviz.cvar
Agdirected = cvar.Agdirected
Agstrictdirected = cvar.Agstrictdirected
Agundirected = cvar.Agundirected
Agstrictundirected = cvar.Agstrictundirected


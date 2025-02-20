from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/rounding.scad'}", use_not_include=False)

class round_corners(_Bosl2Base):
    def __init__(self, path=None, method=None, radius=None, r=None, cut=None, joint=None, width=None, k=None, closed=None, verbose=None, **kwargs):
       super().__init__("round_corners", {"path" : path, "method" : method, "radius" : radius, "r" : r, "cut" : cut, "joint" : joint, "width" : width, "k" : k, "closed" : closed, "verbose" : verbose, **kwargs})

class _smooth_bez_fill(_Bosl2Base):
    def __init__(self, points=None, k=None, **kwargs):
       super().__init__("_smooth_bez_fill", {"points" : points, "k" : k, **kwargs})

class _bezcorner(_Bosl2Base):
    def __init__(self, points=None, parm=None, **kwargs):
       super().__init__("_bezcorner", {"points" : points, "parm" : parm, **kwargs})

class _chamfcorner(_Bosl2Base):
    def __init__(self, points=None, parm=None, **kwargs):
       super().__init__("_chamfcorner", {"points" : points, "parm" : parm, **kwargs})

class _circlecorner(_Bosl2Base):
    def __init__(self, points=None, parm=None, **kwargs):
       super().__init__("_circlecorner", {"points" : points, "parm" : parm, **kwargs})

class _rounding_offsets(_Bosl2Base):
    def __init__(self, edgespec=None, z_dir=None, **kwargs):
       super().__init__("_rounding_offsets", {"edgespec" : edgespec, "z_dir" : z_dir, **kwargs})

class smooth_path(_Bosl2Base):
    def __init__(self, path=None, tangents=None, size=None, relsize=None, splinesteps=None, uniform=None, closed=None, **kwargs):
       super().__init__("smooth_path", {"path" : path, "tangents" : tangents, "size" : size, "relsize" : relsize, "splinesteps" : splinesteps, "uniform" : uniform, "closed" : closed, **kwargs})

class _scalar_to_vector(_Bosl2Base):
    def __init__(self, value=None, length=None, varname=None, **kwargs):
       super().__init__("_scalar_to_vector", {"value" : value, "length" : length, "varname" : varname, **kwargs})

class path_join(_Bosl2Base):
    def __init__(self, paths=None, joint=None, k=None, relocate=None, closed=None, **kwargs):
       super().__init__("path_join", {"paths" : paths, "joint" : joint, "k" : k, "relocate" : relocate, "closed" : closed, **kwargs})

class _path_join(_Bosl2Base):
    def __init__(self, paths=None, joint=None, k=None, i=None, result=None, relocate=None, closed=None, **kwargs):
       super().__init__("_path_join", {"paths" : paths, "joint" : joint, "k" : k, "i" : i, "result" : result, "relocate" : relocate, "closed" : closed, **kwargs})

class offset_stroke(_Bosl2Base):
    def __init__(self, path=None, width=None, rounded=None, start=None, end=None, check_valid=None, quality=None, chamfer=None, closed=None, atype=None, anchor=None, spin=None, cp=None, **kwargs):
       super().__init__("offset_stroke", {"path" : path, "width" : width, "rounded" : rounded, "start" : start, "end" : end, "check_valid" : check_valid, "quality" : quality, "chamfer" : chamfer, "closed" : closed, "atype" : atype, "anchor" : anchor, "spin" : spin, "cp" : cp, **kwargs})

class os_pointed(_Bosl2Base):
    def __init__(self, dist=None, loc=None, **kwargs):
       super().__init__("os_pointed", {"dist" : dist, "loc" : loc, **kwargs})

class os_round(_Bosl2Base):
    def __init__(self, cut=None, angle=None, abs_angle=None, k=None, r=None, **kwargs):
       super().__init__("os_round", {"cut" : cut, "angle" : angle, "abs_angle" : abs_angle, "k" : k, "r" : r, **kwargs})

class os_flat(_Bosl2Base):
    def __init__(self, angle=None, abs_angle=None, **kwargs):
       super().__init__("os_flat", {"angle" : angle, "abs_angle" : abs_angle, **kwargs})

class angle_between_lines(_Bosl2Base):
    def __init__(self, line1=None, line2=None, **kwargs):
       super().__init__("angle_between_lines", {"line1" : line1, "line2" : line2, **kwargs})

class _parse_stroke_end(_Bosl2Base):
    def __init__(self, spec=None, name=None, **kwargs):
       super().__init__("_parse_stroke_end", {"spec" : spec, "name" : name, **kwargs})

class _stroke_end(_Bosl2Base):
    def __init__(self, width=None, left=None, right=None, spec=None, **kwargs):
       super().__init__("_stroke_end", {"width" : width, "left" : left, "right" : right, "spec" : spec, **kwargs})

class _path_line_intersection(_Bosl2Base):
    def __init__(self, path=None, line=None, ind=None, **kwargs):
       super().__init__("_path_line_intersection", {"path" : path, "line" : line, "ind" : ind, **kwargs})

class _make_offset_polyhedron(_Bosl2Base):
    def __init__(self, path=None, offsets=None, offset_type=None, flip_faces=None, quality=None, check_valid=None, offsetind=None, vertexcount=None, vertices=None, faces=None, **kwargs):
       super().__init__("_make_offset_polyhedron", {"path" : path, "offsets" : offsets, "offset_type" : offset_type, "flip_faces" : flip_faces, "quality" : quality, "check_valid" : check_valid, "offsetind" : offsetind, "vertexcount" : vertexcount, "vertices" : vertices, "faces" : faces, **kwargs})

class _struct_valid(_Bosl2Base):
    def __init__(self, spec=None, func=None, name=None, **kwargs):
       super().__init__("_struct_valid", {"spec" : spec, "func" : func, "name" : name, **kwargs})

class offset_sweep(_Bosl2Base):
    def __init__(self, path=None, height=None, bottom=None, top=None, h=None, l=None, length=None, offset=None, r=None, steps=None, quality=None, check_valid=None, extra=None, cut=None, chamfer_width=None, chamfer_height=None, joint=None, k=None, angle=None, **kwargs):
       super().__init__("offset_sweep", {"path" : path, "height" : height, "bottom" : bottom, "top" : top, "h" : h, "l" : l, "length" : length, "offset" : offset, "r" : r, "steps" : steps, "quality" : quality, "check_valid" : check_valid, "extra" : extra, "cut" : cut, "chamfer_width" : chamfer_width, "chamfer_height" : chamfer_height, "joint" : joint, "k" : k, "angle" : angle, **kwargs})

class os_circle(_Bosl2Base):
    def __init__(self, r=None, cut=None, extra=None, check_valid=None, quality=None, steps=None, offset=None, **kwargs):
       super().__init__("os_circle", {"r" : r, "cut" : cut, "extra" : extra, "check_valid" : check_valid, "quality" : quality, "steps" : steps, "offset" : offset, **kwargs})

class os_teardrop(_Bosl2Base):
    def __init__(self, r=None, cut=None, extra=None, check_valid=None, quality=None, steps=None, offset=None, **kwargs):
       super().__init__("os_teardrop", {"r" : r, "cut" : cut, "extra" : extra, "check_valid" : check_valid, "quality" : quality, "steps" : steps, "offset" : offset, **kwargs})

class os_chamfer(_Bosl2Base):
    def __init__(self, height=None, width=None, cut=None, angle=None, extra=None, check_valid=None, quality=None, steps=None, offset=None, **kwargs):
       super().__init__("os_chamfer", {"height" : height, "width" : width, "cut" : cut, "angle" : angle, "extra" : extra, "check_valid" : check_valid, "quality" : quality, "steps" : steps, "offset" : offset, **kwargs})

class os_smooth(_Bosl2Base):
    def __init__(self, cut=None, joint=None, k=None, extra=None, check_valid=None, quality=None, steps=None, offset=None, **kwargs):
       super().__init__("os_smooth", {"cut" : cut, "joint" : joint, "k" : k, "extra" : extra, "check_valid" : check_valid, "quality" : quality, "steps" : steps, "offset" : offset, **kwargs})

class os_profile(_Bosl2Base):
    def __init__(self, points=None, extra=None, check_valid=None, quality=None, offset=None, **kwargs):
       super().__init__("os_profile", {"points" : points, "extra" : extra, "check_valid" : check_valid, "quality" : quality, "offset" : offset, **kwargs})

class os_mask(_Bosl2Base):
    def __init__(self, mask=None, out=None, extra=None, check_valid=None, quality=None, offset=None, **kwargs):
       super().__init__("os_mask", {"mask" : mask, "out" : out, "extra" : extra, "check_valid" : check_valid, "quality" : quality, "offset" : offset, **kwargs})

class convex_offset_extrude(_Bosl2Base):
    def __init__(self, height=None, bottom=None, top=None, h=None, l=None, length=None, offset=None, r=None, steps=None, extra=None, cut=None, chamfer_width=None, chamfer_height=None, joint=None, k=None, angle=None, convexity=None, thickness=None, **kwargs):
       super().__init__("convex_offset_extrude", {"height" : height, "bottom" : bottom, "top" : top, "h" : h, "l" : l, "length" : length, "offset" : offset, "r" : r, "steps" : steps, "extra" : extra, "cut" : cut, "chamfer_width" : chamfer_width, "chamfer_height" : chamfer_height, "joint" : joint, "k" : k, "angle" : angle, "convexity" : convexity, "thickness" : thickness, **kwargs})

class _remove_undefined_vals(_Bosl2Base):
    def __init__(self, list=None, **kwargs):
       super().__init__("_remove_undefined_vals", {"list" : list, **kwargs})

class _rp_compute_patches(_Bosl2Base):
    def __init__(self, top=None, bot=None, rtop=None, rsides=None, ktop=None, ksides=None, concave=None, **kwargs):
       super().__init__("_rp_compute_patches", {"top" : top, "bot" : bot, "rtop" : rtop, "rsides" : rsides, "ktop" : ktop, "ksides" : ksides, "concave" : concave, **kwargs})

class rounded_prism(_Bosl2Base):
    def __init__(self, bottom=None, top=None, joint_bot=None, joint_top=None, joint_sides=None, k_bot=None, k_top=None, k_sides=None, k=None, splinesteps=None, h=None, length=None, l=None, height=None, debug=None, **kwargs):
       super().__init__("rounded_prism", {"bottom" : bottom, "top" : top, "joint_bot" : joint_bot, "joint_top" : joint_top, "joint_sides" : joint_sides, "k_bot" : k_bot, "k_top" : k_top, "k_sides" : k_sides, "k" : k, "splinesteps" : splinesteps, "h" : h, "length" : length, "l" : l, "height" : height, "debug" : debug, **kwargs})

class _cyl_hole(_Bosl2Base):
    def __init__(self, r=None, path=None, **kwargs):
       super().__init__("_cyl_hole", {"r" : r, "path" : path, **kwargs})

class _circle_mask(_Bosl2Base):
    def __init__(self, r=None, **kwargs):
       super().__init__("_circle_mask", {"r" : r, **kwargs})

class bent_cutout_mask(_Bosl2Base):
    def __init__(self, r=None, thickness=None, path=None, radius=None, convexity=None, **kwargs):
       super().__init__("bent_cutout_mask", {"r" : r, "thickness" : thickness, "path" : path, "radius" : radius, "convexity" : convexity, **kwargs})

class join_prism(_Bosl2Base):
    def __init__(self, polygon=None, base=None, base_r=None, base_d=None, base_T=None, scale=None, prism_end_T=None, short=None, length=None, l=None, height=None, h=None, aux=None, aux_T=None, aux_r=None, aux_d=None, overlap=None, base_overlap=None, aux_overlap=None, n=None, base_n=None, aux_n=None, end_n=None, fillet=None, base_fillet=None, aux_fillet=None, end_round=None, k=None, base_k=None, aux_k=None, end_k=None, uniform=None, base_uniform=None, aux_uniform=None, debug=None, return_axis=None, **kwargs):
       super().__init__("join_prism", {"polygon" : polygon, "base" : base, "base_r" : base_r, "base_d" : base_d, "base_T" : base_T, "scale" : scale, "prism_end_T" : prism_end_T, "short" : short, "length" : length, "l" : l, "height" : height, "h" : h, "aux" : aux, "aux_T" : aux_T, "aux_r" : aux_r, "aux_d" : aux_d, "overlap" : overlap, "base_overlap" : base_overlap, "aux_overlap" : aux_overlap, "n" : n, "base_n" : base_n, "aux_n" : aux_n, "end_n" : end_n, "fillet" : fillet, "base_fillet" : base_fillet, "aux_fillet" : aux_fillet, "end_round" : end_round, "k" : k, "base_k" : base_k, "aux_k" : aux_k, "end_k" : end_k, "uniform" : uniform, "base_uniform" : base_uniform, "aux_uniform" : aux_uniform, "debug" : debug, "return_axis" : return_axis, **kwargs})

class _fix_angle_list(_Bosl2Base):
    def __init__(self, list=None, ind=None, result=None, **kwargs):
       super().__init__("_fix_angle_list", {"list" : list, "ind" : ind, "result" : result, **kwargs})

class _cyl_line_intersection(_Bosl2Base):
    def __init__(self, R=None, line=None, ref=None, **kwargs):
       super().__init__("_cyl_line_intersection", {"R" : R, "line" : line, "ref" : ref, **kwargs})

class _sphere_line_isect_best(_Bosl2Base):
    def __init__(self, R=None, line=None, ref=None, **kwargs):
       super().__init__("_sphere_line_isect_best", {"R" : R, "line" : line, "ref" : ref, **kwargs})

class _prism_line_isect(_Bosl2Base):
    def __init__(self, poly_pairs=None, line=None, ref=None, **kwargs):
       super().__init__("_prism_line_isect", {"poly_pairs" : poly_pairs, "line" : line, "ref" : ref, **kwargs})

class _prism_fillet(_Bosl2Base):
    def __init__(self, name=None, base=None, R=None, bot=None, top=None, d=None, k=None, N=None, overlap=None, uniform=None, debug=None, **kwargs):
       super().__init__("_prism_fillet", {"name" : name, "base" : base, "R" : R, "bot" : bot, "top" : top, "d" : d, "k" : k, "N" : N, "overlap" : overlap, "uniform" : uniform, "debug" : debug, **kwargs})

class _prism_fillet_plane(_Bosl2Base):
    def __init__(self, name=None, bot=None, top=None, d=None, k=None, N=None, overlap=None, debug=None, **kwargs):
       super().__init__("_prism_fillet_plane", {"name" : name, "bot" : bot, "top" : top, "d" : d, "k" : k, "N" : N, "overlap" : overlap, "debug" : debug, **kwargs})

class _prism_fillet_plane(_Bosl2Base):
    def __init__(self, name=None, bot=None, top=None, d=None, k=None, N=None, overlap=None, debug=None, **kwargs):
       super().__init__("_prism_fillet_plane", {"name" : name, "bot" : bot, "top" : top, "d" : d, "k" : k, "N" : N, "overlap" : overlap, "debug" : debug, **kwargs})

class _prism_fillet_cyl(_Bosl2Base):
    def __init__(self, name=None, R=None, bot=None, top=None, d=None, k=None, N=None, overlap=None, uniform=None, debug=None, **kwargs):
       super().__init__("_prism_fillet_cyl", {"name" : name, "R" : R, "bot" : bot, "top" : top, "d" : d, "k" : k, "N" : N, "overlap" : overlap, "uniform" : uniform, "debug" : debug, **kwargs})

class _prism_fillet_sphere(_Bosl2Base):
    def __init__(self, name=None, R=None, bot=None, top=None, d=None, k=None, N=None, overlap=None, uniform=None, debug=None, **kwargs):
       super().__init__("_prism_fillet_sphere", {"name" : name, "R" : R, "bot" : bot, "top" : top, "d" : d, "k" : k, "N" : N, "overlap" : overlap, "uniform" : uniform, "debug" : debug, **kwargs})

class _getnormal(_Bosl2Base):
    def __init__(self, polygon=None, index=None, u=None, **kwargs):
       super().__init__("_getnormal", {"polygon" : polygon, "index" : index, "u" : u, **kwargs})

class _polygon_step(_Bosl2Base):
    def __init__(self, poly=None, ind=None, u=None, dir=None, length=None, **kwargs):
       super().__init__("_polygon_step", {"poly" : poly, "ind" : ind, "u" : u, "dir" : dir, "length" : length, **kwargs})

class _prism_fillet_prism(_Bosl2Base):
    def __init__(self, name=None, basepoly=None, bot=None, top=None, d=None, k=None, N=None, overlap=None, uniform=None, debug=None, **kwargs):
       super().__init__("_prism_fillet_prism", {"name" : name, "basepoly" : basepoly, "bot" : bot, "top" : top, "d" : d, "k" : k, "N" : N, "overlap" : overlap, "uniform" : uniform, "debug" : debug, **kwargs})

class round_corners(_Bosl2Base):
    def __init__(self, path=None, method=None, radius=None, r=None, cut=None, joint=None, width=None, k=None, closed=None, verbose=None, **kwargs):
       super().__init__("round_corners", {"path" : path, "method" : method, "radius" : radius, "r" : r, "cut" : cut, "joint" : joint, "width" : width, "k" : k, "closed" : closed, "verbose" : verbose, **kwargs})

class smooth_path(_Bosl2Base):
    def __init__(self, path=None, tangents=None, size=None, relsize=None, splinesteps=None, uniform=None, closed=None, **kwargs):
       super().__init__("smooth_path", {"path" : path, "tangents" : tangents, "size" : size, "relsize" : relsize, "splinesteps" : splinesteps, "uniform" : uniform, "closed" : closed, **kwargs})

class path_join(_Bosl2Base):
    def __init__(self, paths=None, joint=None, k=None, relocate=None, closed=None, **kwargs):
       super().__init__("path_join", {"paths" : paths, "joint" : joint, "k" : k, "relocate" : relocate, "closed" : closed, **kwargs})

class offset_stroke(_Bosl2Base):
    def __init__(self, path=None, width=None, rounded=None, start=None, end=None, check_valid=None, quality=None, chamfer=None, closed=None, atype=None, anchor=None, spin=None, cp=None, **kwargs):
       super().__init__("offset_stroke", {"path" : path, "width" : width, "rounded" : rounded, "start" : start, "end" : end, "check_valid" : check_valid, "quality" : quality, "chamfer" : chamfer, "closed" : closed, "atype" : atype, "anchor" : anchor, "spin" : spin, "cp" : cp, **kwargs})

class offset_sweep(_Bosl2Base):
    def __init__(self, path=None, height=None, bottom=None, top=None, h=None, l=None, offset=None, r=None, steps=None, quality=None, check_valid=None, extra=None, cut=None, chamfer_width=None, chamfer_height=None, joint=None, k=None, angle=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("offset_sweep", {"path" : path, "height" : height, "bottom" : bottom, "top" : top, "h" : h, "l" : l, "offset" : offset, "r" : r, "steps" : steps, "quality" : quality, "check_valid" : check_valid, "extra" : extra, "cut" : cut, "chamfer_width" : chamfer_width, "chamfer_height" : chamfer_height, "joint" : joint, "k" : k, "angle" : angle, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class convex_offset_extrude(_Bosl2Base):
    def __init__(self, height=None, bottom=None, top=None, h=None, l=None, length=None, offset=None, r=None, steps=None, extra=None, cut=None, chamfer_width=None, chamfer_height=None, joint=None, k=None, angle=None, convexity=None, thickness=None, **kwargs):
       super().__init__("convex_offset_extrude", {"height" : height, "bottom" : bottom, "top" : top, "h" : h, "l" : l, "length" : length, "offset" : offset, "r" : r, "steps" : steps, "extra" : extra, "cut" : cut, "chamfer_width" : chamfer_width, "chamfer_height" : chamfer_height, "joint" : joint, "k" : k, "angle" : angle, "convexity" : convexity, "thickness" : thickness, **kwargs})

class rounded_prism(_Bosl2Base):
    def __init__(self, bottom=None, top=None, joint_bot=None, joint_top=None, joint_sides=None, k_bot=None, k_top=None, k_sides=None, k=None, splinesteps=None, h=None, length=None, l=None, height=None, convexity=None, debug=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("rounded_prism", {"bottom" : bottom, "top" : top, "joint_bot" : joint_bot, "joint_top" : joint_top, "joint_sides" : joint_sides, "k_bot" : k_bot, "k_top" : k_top, "k_sides" : k_sides, "k" : k, "splinesteps" : splinesteps, "h" : h, "length" : length, "l" : l, "height" : height, "convexity" : convexity, "debug" : debug, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class bent_cutout_mask(_Bosl2Base):
    def __init__(self, r=None, thickness=None, path=None, radius=None, convexity=None, **kwargs):
       super().__init__("bent_cutout_mask", {"r" : r, "thickness" : thickness, "path" : path, "radius" : radius, "convexity" : convexity, **kwargs})

class join_prism(_Bosl2Base):
    def __init__(self, polygon=None, base=None, base_r=None, base_d=None, base_T=None, scale=None, prism_end_T=None, short=None, length=None, l=None, height=None, h=None, aux=None, aux_T=None, aux_r=None, aux_d=None, overlap=None, base_overlap=None, aux_overlap=None, n=None, base_n=None, end_n=None, aux_n=None, fillet=None, base_fillet=None, aux_fillet=None, end_round=None, k=None, base_k=None, aux_k=None, end_k=None, uniform=None, base_uniform=None, aux_uniform=None, debug=None, anchor=None, extent=None, cp=None, atype=None, orient=None, spin=None, convexity=None, **kwargs):
       super().__init__("join_prism", {"polygon" : polygon, "base" : base, "base_r" : base_r, "base_d" : base_d, "base_T" : base_T, "scale" : scale, "prism_end_T" : prism_end_T, "short" : short, "length" : length, "l" : l, "height" : height, "h" : h, "aux" : aux, "aux_T" : aux_T, "aux_r" : aux_r, "aux_d" : aux_d, "overlap" : overlap, "base_overlap" : base_overlap, "aux_overlap" : aux_overlap, "n" : n, "base_n" : base_n, "end_n" : end_n, "aux_n" : aux_n, "fillet" : fillet, "base_fillet" : base_fillet, "aux_fillet" : aux_fillet, "end_round" : end_round, "k" : k, "base_k" : base_k, "aux_k" : aux_k, "end_k" : end_k, "uniform" : uniform, "base_uniform" : base_uniform, "aux_uniform" : aux_uniform, "debug" : debug, "anchor" : anchor, "extent" : extent, "cp" : cp, "atype" : atype, "orient" : orient, "spin" : spin, "convexity" : convexity, **kwargs})


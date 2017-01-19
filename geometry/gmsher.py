class Gmsher(object):
    
    def __init__(self):
        self._POINT_ID = 0
        self._LINE_ID = 0
        self._LINELOOP_ID = 0        
        self._SURFACE_ID = 0 
        self._PHYSICALGROUP_ID = 0
        self._id_map = {'p': self._POINT_ID, 
                        'l': self._LINE_ID, 
                        'll': self._LINELOOP_ID,
                        's': self._SURFACE_ID,
                        'pg': self._PHYSICALGROUP_ID}
        
        self._GMSH_CODE = []
        
    def get_code(self):
        return '\n'.join(self._GMSH_CODE)
    
    def add_point(self, pos, lcar):
        name = self._get_next('p')
        self._GMSH_CODE.append(
            '{} = newp;'.format(name))
        self._GMSH_CODE.append(
            'Point({0}) = {{ {1}, {2}, {3}, {4} }};'.format(
                name, pos[0], pos[1], pos[2], lcar))
        return name
    
    def add_line(self, p0, p1):
        name = self._get_next('l')
        self._GMSH_CODE.append(
            '{} = newl;'.format(name))
        self._GMSH_CODE.append(
            'Line({0}) = {{ {1}, {2} }};'.format(
                name, p0, p1))
        return name
    
    def add_line_loop(self, lines):
        name = self._get_next('ll')
        self._GMSH_CODE.append(
            '{} = newll;'.format(name))
        self._GMSH_CODE.append(
            'Line Loop({0}) = {{ {1} }};'.format(
                name, ', '.join(lines)))
        return name
    
    def add_surface(self, line_loop):
        name = self._get_next('s')
        self._GMSH_CODE.append(
            '{} = news;'.format(name))
        if isinstance(line_loop, list):
            self._GMSH_CODE.append(
                'Plane Surface({0}) = {{ {1} }};'.format(
                    name, ', '.join(line_loop)))
        else:
            self._GMSH_CODE.append(
                'Plane Surface({0}) = {{ {1} }};'.format(
                    name, line_loop))
        return name
    
    def add_physical_surface(self, surface, label):
        if isinstance(surface, list):
            self._GMSH_CODE.append(
                'Physical Surface("{0}") = {{ {1} }};'.format(
                    label, ', '.join(surface)))
        else:
            self._GMSH_CODE.append(
                'Physical Surface("{0}") = {{ {1} }};'.format(
                    label, surface))
            
        
    
    def _get_next(self, gmsh_type):
        self._id_map[gmsh_type] += 1
        return '{0}{1}'.format(gmsh_type, self._id_map[gmsh_type])

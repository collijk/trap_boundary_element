from collections import OrderedDict

class MeshData(object):
    
    # Mesh sizes in microns
    tiny = 0.5
    small = 1
    medium = 3
    large = 5
    huge = 10
        
    @staticmethod
    def default_mesh():
        mesh_sizes = OrderedDict()
        mesh_sizes['G01'] = MeshData.large
        mesh_sizes['G02'] = MeshData.large
        mesh_sizes['G03'] = MeshData.large
        mesh_sizes['G04'] = MeshData.large
        mesh_sizes['G05'] = MeshData.large
        mesh_sizes['G06'] = MeshData.large
        mesh_sizes['G07'] = MeshData.large
        mesh_sizes['G08'] = MeshData.large
        
        mesh_sizes['Q01'] = MeshData.large
        mesh_sizes['Q02'] = MeshData.large
        mesh_sizes['Q03'] = MeshData.large
        mesh_sizes['Q04'] = MeshData.large
        mesh_sizes['Q05'] = MeshData.large
        mesh_sizes['Q06'] = MeshData.large
        mesh_sizes['Q07'] = MeshData.large
        mesh_sizes['Q08'] = MeshData.large
        mesh_sizes['Q09'] = MeshData.large
        mesh_sizes['Q10'] = MeshData.large
        mesh_sizes['Q11'] = MeshData.large
        mesh_sizes['Q12'] = MeshData.large
        mesh_sizes['Q13'] = MeshData.large
        mesh_sizes['Q14'] = MeshData.large
        mesh_sizes['Q15'] = MeshData.large
        mesh_sizes['Q16'] = MeshData.large
        mesh_sizes['Q17'] = MeshData.large
        mesh_sizes['Q18'] = MeshData.large
        mesh_sizes['Q19'] = MeshData.large
        mesh_sizes['Q20'] = MeshData.large
        mesh_sizes['Q21'] = MeshData.large
        mesh_sizes['Q22'] = MeshData.large
        mesh_sizes['Q23'] = MeshData.large
        mesh_sizes['Q24'] = MeshData.large
        mesh_sizes['Q25'] = MeshData.large
        mesh_sizes['Q26'] = MeshData.large
        mesh_sizes['Q27'] = MeshData.large
        mesh_sizes['Q28'] = MeshData.large
        mesh_sizes['Q29'] = MeshData.large
        mesh_sizes['Q30'] = MeshData.large
        mesh_sizes['Q31'] = MeshData.large
        mesh_sizes['Q32'] = MeshData.large
        mesh_sizes['Q33'] = MeshData.large
        mesh_sizes['Q34'] = MeshData.large
        mesh_sizes['Q35'] = MeshData.large
        mesh_sizes['Q36'] = MeshData.large
        mesh_sizes['Q37'] = MeshData.large
        mesh_sizes['Q38'] = MeshData.large
        mesh_sizes['Q39'] = MeshData.large
        mesh_sizes['Q40'] = MeshData.large
        
        mesh_sizes['T01'] = MeshData.large
        mesh_sizes['T02'] = MeshData.large
        mesh_sizes['T03'] = MeshData.large
        mesh_sizes['T04'] = MeshData.large
        mesh_sizes['T05'] = MeshData.large
        mesh_sizes['T06'] = MeshData.large
        
        mesh_sizes['Y01'] = MeshData.large
        mesh_sizes['Y02'] = MeshData.large
        mesh_sizes['Y03'] = MeshData.large
        mesh_sizes['Y04'] = MeshData.large
        mesh_sizes['Y05'] = MeshData.large
        mesh_sizes['Y06'] = MeshData.large
        mesh_sizes['Y07'] = MeshData.large
        mesh_sizes['Y08'] = MeshData.large
        mesh_sizes['Y09'] = MeshData.large
        mesh_sizes['Y10'] = MeshData.large
        mesh_sizes['Y11'] = MeshData.large
        mesh_sizes['Y12'] = MeshData.large
        mesh_sizes['Y13'] = MeshData.large
        mesh_sizes['Y14'] = MeshData.large
        mesh_sizes['Y15'] = MeshData.large
        mesh_sizes['Y16'] = MeshData.large
        mesh_sizes['Y17'] = MeshData.large
        mesh_sizes['Y18'] = MeshData.large
        mesh_sizes['Y19'] = MeshData.large
        mesh_sizes['Y20'] = MeshData.large
        mesh_sizes['Y21'] = MeshData.large
        mesh_sizes['Y22'] = MeshData.large
        mesh_sizes['Y23'] = MeshData.large
        mesh_sizes['Y24'] = MeshData.large
        
        mesh_sizes['L01'] = MeshData.large
        mesh_sizes['L02'] = MeshData.large
        mesh_sizes['L03'] = MeshData.large
        mesh_sizes['L04'] = MeshData.large
        mesh_sizes['L05'] = MeshData.large
        mesh_sizes['L06'] = MeshData.large
        mesh_sizes['L07'] = MeshData.large
        mesh_sizes['L08'] = MeshData.large
        mesh_sizes['L09'] = MeshData.large
        mesh_sizes['L10'] = MeshData.large
        mesh_sizes['L11'] = MeshData.large
        mesh_sizes['L12'] = MeshData.large
        mesh_sizes['L13'] = MeshData.large
        mesh_sizes['L14'] = MeshData.large
        mesh_sizes['L15'] = MeshData.large
        mesh_sizes['L16'] = MeshData.large
        
        mesh_sizes['RF']     = MeshData.large
        mesh_sizes['Top']    = MeshData.large
        mesh_sizes['Trench'] = MeshData.large
        mesh_sizes['Hole']   = MeshData.large
        mesh_sizes['Base']   = MeshData.large
        return mesh_sizes
        

import os
import lit.formats

# iree-tv directory
iree_tv: str = os.path.join(config.my_obj_root, "iree-tv")

config.name = 'MLIR'
config.test_source_root = os.path.join(config.my_src_root, "tests/cases")
config.test_exec_root = os.path.join(config.my_obj_root, "tests")
config.test_format = lit.formats.MLIRTest(iree_tv)
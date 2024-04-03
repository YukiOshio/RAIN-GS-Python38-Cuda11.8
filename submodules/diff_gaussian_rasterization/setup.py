
from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension, _get_build_directory, load
import os
os.path.dirname(os.path.abspath(__file__))

# setup(
#     name="diff_gaussian_rasterization",
#     packages=['diff_gaussian_rasterization'],
#     ext_modules=[
#         CUDAExtension(
#             name="diff_gaussian_rasterization._C",
#             sources=[
#             "cuda_rasterizer/rasterizer_impl.cu",
#             "cuda_rasterizer/forward.cu",
#             "cuda_rasterizer/backward.cu",
#             "rasterize_points.cu",
#             "ext.cpp"],
#             extra_compile_args={"nvcc": ["-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")]})
#         ],
#     cmdclass={
#         'build_ext': BuildExtension
#     }
# )

name="diff_gaussian_rasterization"
build_dir = _get_build_directory(name, verbose=False)
_C = load(
    name=name,
    sources=[
            "E:/UpHash/GaussianSplatting/RAIN-GS/submodules/diff_gaussian_rasterization/cuda_rasterizer/rasterizer_impl.cu",
            "E:/UpHash/GaussianSplatting/RAIN-GS/submodules/diff_gaussian_rasterization/cuda_rasterizer/forward.cu",
            "E:/UpHash/GaussianSplatting/RAIN-GS/submodules/diff_gaussian_rasterization/cuda_rasterizer/backward.cu",
            "E:/UpHash/GaussianSplatting/RAIN-GS/submodules/diff_gaussian_rasterization/rasterize_points.cu",
            "E:/UpHash/GaussianSplatting/RAIN-GS/submodules/diff_gaussian_rasterization/ext.cpp"],
    extra_cuda_cflags=["-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")],
)


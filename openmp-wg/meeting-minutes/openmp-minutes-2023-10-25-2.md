### 2023, Oct 25

Agenda

New 

  * Intel's interop implementation
  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.2 Update 2, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246051897&usg=AOvVaw17XlzyPeJOos9LdV_OgYDO) (-DLLVM_ENABLE_PROJECTS=openmp): 42 failed tests (up from 2 in 3523f94bfa8773a7dfe7b9a634fcf06fcd2ac3e3)


  * api/ompx_3d: Cannot form a team with 2 threads, using 1 instead.
  * nvlink error   : Prototype doesn't match for 'llvm_omp_target_dynamic_shared_alloc', 'omp_get_num_procs'
  * api/omp_host_pinned_memory: "CUDA" error: Failure to alloc memory: Error in cuMemAlloc[Host|Managed]: invalid device context
  * mappin/reduction_implicit_map, offloading/bug64959_compile_only: ptxas /tmp/lit-tmp-hj1du5qk/reduction_implicit_map.cpp.tmp.nvptx64-nvidia-cuda.sm_61-115f57.s, line 29960; error   : Feature 'activemask' requires PTX ISA .version 6.2 or later
  * offloading/barrier_fence: nvlink error   : entry function '__omp_offloading_820_4365e_main_l26' with max regcount of 128 calls function '__kmpc_parallel_51' with regcount of 252
  * mapping/target_uses_allocator: Clang SEGFAULT:  clang::CodeGen::CodeGenFunction::EmitLValueForLambdaField
  * unified_shared_memory/shared_update: "PluginInterface" error: Failure to synchronize stream (nil): Error in cuStreamSynchronize: an illegal memory access was encountered


  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246053055&usg=AOvVaw2TXjVwsxRYMy5fFA9JF-kE) (-DLLVM_ENABLE_RUNTIMES=openmp): 286 failed tests`


  * ptxas not found; should honor -DCUDA_TOOLKIT_ROOT_DIR=/opt/cuda setting


  * SOLLVE V&V not running, requires -DSYSTEM_GPU=NVIDIA/AMD (https://github.com/llvm/llvm-test-suite/pull/24, https://github.com/llvm/llvm-test-suite/pull/28)


  * Should run all tests when not specified
  * Why not autodetect?


  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246053651&usg=AOvVaw39TPd2hsuACP6PZAfahTwF)

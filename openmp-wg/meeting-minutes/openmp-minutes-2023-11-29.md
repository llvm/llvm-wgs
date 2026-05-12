### 2023, Nov 29

Agenda  (Nov 15 meeting canceled)

New 

  * Performance implications of [[OpenMP] Introduce the KernelLaunchEnvironment as implicit argument by jdoerfert * Pull Request #70401 * llvm/llvm-project (github.com)](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/70401&sa=D&source=editors&ust=1778600246048056&usg=AOvVaw3g8nZVS3i4g3PwSnTkZ-6N)
  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246048297&usg=AOvVaw3RQpXLuIsq6EZ0hxqkC8oi) (-DLLVM_ENABLE_PROJECTS=openmp): 34 failed tests
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246048436&usg=AOvVaw0o0gnsj6Y9LogBIhm7Oij9) (-DLLVM_ENABLE_RUNTIMES=openmp): 34 failed tests
  * [[libomptarget][tests] Maximum assumed device heap size. * Issue #71747](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/71747&sa=D&source=editors&ust=1778600246048607&usg=AOvVaw2XxExWTQfa4T0kbPoLt3k7) (4 tests)


  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246048837&usg=AOvVaw0nZ5SoIny09YRneuq_Er3d)
